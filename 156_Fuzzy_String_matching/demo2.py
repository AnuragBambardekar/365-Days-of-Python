from thefuzz import fuzz, process

things = ["Programming Language", "Nativ Language", "React Native", "Some Stuff", "Hello World", "Coding and Stuff"]

print(process.extract("language", things, limit=2))

print(process.extractOne("programming", things))