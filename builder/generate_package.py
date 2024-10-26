from pathlib import Path
import re
from tempfile import TemporaryDirectory
from datamodel_code_generator import InputFileType, generate, OpenAPIScope
from datamodel_code_generator import DataModelType, PythonVersion
import json
import warnings

from ruamel.yaml import YAML
from ruamel.yaml.error import ReusedAnchorWarning
from config import Settings
from toml_generator import generate_toml

# fix errors from ruamel.yaml
warnings.simplefilter("ignore", ReusedAnchorWarning)

# convert the yaml into json
yaml = YAML(typ="safe", pure=True)

with open("openapi.yaml") as stream:
    data = yaml.load(stream)

openapi_json = json.dumps(data)

# create a path for the new package
release_pkg_dir = Path('lmos_openai_types/')
release_pkg_dir.mkdir(parents=True, exist_ok=True)

# create types

def gen(path):
    # this is only supported for pydantic
    reuse_model = Settings.ModelType == DataModelType.PydanticV2BaseModel

    generate(
        input_=openapi_json,
        input_file_type=InputFileType.OpenAPI,
        output=path,
        output_model_type=Settings.ModelType,
        target_python_version=PythonVersion.PY_312,
        apply_default_values_for_required_fields=False,
        use_field_description=True,
        use_schema_description=True,
        use_subclass_enum=True,
        enum_field_as_literal="all",
        reuse_model=reuse_model,
        # use_default_kwarg=True,
        field_constraints=True,
        # openapi_scopes=[OpenAPIScope.Parameters, OpenAPIScope.Paths, OpenAPIScope.Schemas, OpenAPIScope.Tags],
        strict_nullable=True # https://github.com/koxudaxi/datamodel-code-generator/issues/327
    )

with TemporaryDirectory() as temporary_directory:
    tmp_dir_path = Path(temporary_directory)
    output = Path(tmp_dir_path / 'model.py')
    gen(output)
    model: str = output.read_text()

pattern = r'(.*?: Optional\[.*\] = Field\(\n?)\.\.\.'
replace = r'\1None'

model = re.sub(pattern, replace, model)

output = Path(release_pkg_dir / '__init__.py')
with open(output, "w+") as file:
    file.write(model)

TomlPath = Path(release_pkg_dir / '../pyproject.toml')
with open(TomlPath, "w+") as pyproject :
    pyproject.write(generate_toml())

pytyped = Path(release_pkg_dir / 'py.typed')
with open(pytyped, 'w+') :
    pass
