# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Setup

```bash
uv sync --group test
uv run pytest
```

## Project

- Author: {{ cookiecutter.author_name }}
- Python: {{ cookiecutter.python_version }}
- Package: `{{ cookiecutter.package_name }}`
- Version: {{ cookiecutter.version }}