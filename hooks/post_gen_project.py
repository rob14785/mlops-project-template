from pathlib import Path

for directory in ("data", "docs", "env", "notebooks", "tasks", "tests"):
    Path(directory).mkdir(parents=True, exist_ok=True)

print("Template generation completed.")