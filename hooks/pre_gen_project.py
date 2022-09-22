import os
import subprocess


project_slug = "{{ cookiecutter.project_slug }}"

EEROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if project_slug.startswith("x"):
    print(f"{EEROR_COLOR}ERROR: {project_slug} is not valid name for this template.{RESET_ALL}")

    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")
print(f"Creating project at { os.getcwd()}{RESET_ALL}")

