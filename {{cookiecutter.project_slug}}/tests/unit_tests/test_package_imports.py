def test_package_imports():
    import {{ cookiecutter.package_name }}

from {{ cookiecutter.package_name }}.commons.utils import normalize_project_name


def test_package_imports():
    import {{ cookiecutter.package_name }}


def test_normalize_project_name():
    assert normalize_project_name(" Salary Prediction ") == "salary_prediction"