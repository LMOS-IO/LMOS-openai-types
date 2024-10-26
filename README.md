# LMOS-openai-types
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![API Docs](https://img.shields.io/badge/API-Documentation-green)](https://docs.lmos.io)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-brightgreen.svg)](https://github.com/openai/openai-python)

> Python type definitions generated from OpenAI's OpenAPI specification

## Overview
LMOS-openai-types provides strongly-typed Python models generated from OpenAI's official OpenAPI specification. It serves as a foundational package in the LMOS ecosystem, ensuring type safety and consistency across all LMOS services that interact with OpenAI-compatible APIs.

## Features
- 🔄 **Auto-generated Types**: Automatically generates Python types from OpenAI's OpenAPI specification
- 📦 **Multiple Format Support**: Generates both Pydantic and Msgspec models
- 🔍 **Type Safety**: Provides full type hints and validation for OpenAI API objects
- 🔄 **CI/CD Integration**: Automated builds via GitHub Actions

## Generated Packages
This repository automatically generates two Python packages:

1. **Pydantic Models** (branch: `pydantic-gen`)
   - Built using Pydantic v2
   - Full validation support
   - IDE-friendly with complete type hints

2. **Msgspec Models** (branch: `msgspec-gen`)
   - High-performance serialization
   - Optimized for production deployments
   - Reduced overhead compared to Pydantic

## Development
To set up the development environment:

1. Open in Dev Container (recommended)
   ```bash
   # VSCode will automatically detect and open the dev container
   ```

2. Install dependencies
   ```bash
   pip install -r builder/requirements.txt
   ```

3. Generate types
   ```bash
   # Generate Pydantic models
   python builder/generate_package.py

   # Generate Msgspec models
   python builder/generate_package.py --modeltype MsgspecStruct
   ```

## CI/CD Pipeline

The repository includes two GitHub Actions workflows:

1. `build-pydantic.yml`: Generates Pydantic models
2. `build-msgspec.yml`: Generates Msgspec models

Both workflows:
- Trigger on pushes to main/master
- Generate respective Python packages
- Push to separate branches (`pydantic-gen` and `msgspec-gen`)

## OpenAPI Validation

The repository includes validation for the OpenAPI specification:

- Validates the OpenAPI definition using Swagger Editor
- Runs on pull requests
- Ensures specification compliance

## Project Structure
```
├── builder/                 # Type generation scripts
│   ├── requirements.txt    # Python dependencies
│   └── generate_package.py # Main generation script
├── .devcontainer/          # Dev container configuration
├── .github/workflows/      # GitHub Actions workflows
└── openapi.yaml           # OpenAI API specification
```

## Contributing
We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
Apache 2.0 - See [LICENSE](LICENSE) for details

## Part of the LMOS Ecosystem
This package is part of the larger LMOS (Language Model Orchestration System) ecosystem. Visit [LMOS.io](https://lmos.io) to learn more about our other packages and services.