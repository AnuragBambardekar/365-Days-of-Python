import pynecone as pc

class MyprojectConfig(pc.Config):
    pass

config = MyprojectConfig(
    app_name="MyProject",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)