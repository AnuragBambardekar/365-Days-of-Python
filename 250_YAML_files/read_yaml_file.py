# pip install pyyaml

import yaml

with open("250_YAML_files/example.yml","r") as f:
    data = yaml.safe_load(f)

print(data)