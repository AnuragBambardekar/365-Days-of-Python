import yaml

data = {
    "name":"Bob",
    "age": 25,
    "languages": ["Python", "C", "Java"],
    "address": {
        "city": "NYC",
        "country": "US",
        "zip": "40091"
    }
}

with open("somefile.yaml","w") as f:
    yaml.dump(data, f, default_flow_style=False)