import uuid

def generate_uuid1():
    uuid_obj = uuid.uuid1()
    print(f"UUID1: {uuid_obj}")

def generate_uuid3():
    namespace = uuid.UUID('6ba7b810-9dad-11d1-80b4-00c04fd430c8')
    uuid_obj = uuid.uuid3(namespace, 'hello')
    print(f"UUID3: {uuid_obj}")

def generate_uuid4():
    uuid_obj = uuid.uuid4()
    print(f"UUID4: {uuid_obj}")

def generate_uuid5():
    namespace = uuid.UUID('6ba7b811-9dad-11d1-80b4-00c04fd430c8')
    uuid_obj = uuid.uuid5(namespace, 'hello')
    print(f"UUID5: {uuid_obj}")

def main():
    generate_uuid1()
    generate_uuid3()
    generate_uuid4()
    generate_uuid5()

if __name__ == "__main__":
    main()
