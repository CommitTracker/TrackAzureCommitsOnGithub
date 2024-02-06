import json
import os

class JsonHelper:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(self.root_dir, 'appsettings.json')
        self.apps = self._load_apps()  # Load apps configuration on initialization

    def _load_apps(self):
        """Private method to load app configurations from the JSON file."""
        try:
            with open(self.file_path, 'r') as config_file:
                data = json.load(config_file)
                return data.get('Apps', [])  # Return the list of app configurations
        except FileNotFoundError:
            print("Configuration file not found.")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON from configuration file.")
            return []

    def GetData(self):
        """Public method to get the list of app configurations."""
        return self.apps
