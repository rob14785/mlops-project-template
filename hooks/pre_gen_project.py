import re
import sys

project_slug = "{{ cookiecutter.project_slug }}"

if not re.fullmatch(r"^[a-z][a-z0-9_]*$", project_slug):
    print("ERROR: project_slug must contain only lowercase letters, numbers, and underscores.")
    sys.exit(1)