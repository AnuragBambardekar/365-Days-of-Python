import yaml

with open("250_YAML_files/complex.yaml","r") as f:
    data = yaml.safe_load(f)

print(data)