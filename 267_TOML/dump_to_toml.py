config = {
    "user": {
        "player_x": {"symbol": "X", "color": "blue", "ai": True},
        "player_o": {"symbol": "O", "color": "green", "ai": False},
        "ai_skill": 0.85,
    },
    "board_size": 3,
    "server": {"url": "https://tictactoe.example.com"},
}

def _dumps_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, list):
        return f"[{', '.join(_dumps_value(v) for v in value)}]"
    else:
        raise TypeError(f"{type(value).__name__} {value!r} is not supported")
    
def dumps(toml_dict, table=""):
    def tables_at_end(item):
        _, value = item
        return isinstance(value, dict)

    toml = []
    for key, value in sorted(toml_dict.items(), key=tables_at_end):
        if isinstance(value, dict):
            table_key = f"{table}.{key}" if table else key
            toml.append(f"\n[{table_key}]\n{dumps(value, table_key)}")
        else:
            toml.append(f"{key} = {_dumps_value(value)}")
    return "\n".join(toml)


toml_string = dumps(config)
print(toml_string)