from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from datamodel_code_generator import DataModelType

class SettingsModel(BaseSettings):
    ModelType: DataModelType = Field(default=DataModelType.PydanticV2BaseModel)

    model_config = SettingsConfigDict(
        cli_parse_args=True,
        env_prefix="BUILDER_",
    )

Settings = SettingsModel()