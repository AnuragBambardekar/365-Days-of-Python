class AppConfig:
    def __init__(self, config_dict):
        # Dynamically set attributes based on the config_dict
        for key, value in config_dict.items():
            setattr(self, key, value)

# Configuration data as a dictionary
config_data = {
    'api_url': 'https://api.example.com',
    'debug_mode': False,
    'timeout': 30
}

# Create an AppConfig instance with the provided configuration data
app_config = AppConfig(config_data)

# Accessing configuration settings dynamically using getattr
api_url = getattr(app_config, 'api_url')
debug_mode = getattr(app_config, 'debug_mode')
timeout = getattr(app_config, 'timeout')

print(api_url)      # Output: https://api.example.com
print(debug_mode)   # Output: False
print(timeout)      # Output: 30

# Check if an attribute exists using hasattr
if hasattr(app_config, 'debug_mode'):
    print("Debug mode is defined.")
else:
    print("Debug mode is not defined.")

# Set a new configuration setting using setattr
setattr(app_config, 'new_setting', 'New Value')
print(app_config.new_setting)  # Output: New Value

# Delete a configuration setting using delattr
delattr(app_config, 'timeout')

# Attempt to access the deleted attribute
# This will raise an AttributeError since 'timeout' no longer exists
try:
    print(app_config.timeout)
except AttributeError as e:
    print(f"AttributeError: {e}")
