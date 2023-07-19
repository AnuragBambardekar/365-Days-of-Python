from collections import defaultdict

constant_default_dict = defaultdict(lambda: "hello world")
print(constant_default_dict["hello"])