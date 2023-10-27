import pynecone as pc

class ClockConfig(pc.Config):
    pass

config = ClockConfig(
    app_name="clock",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)