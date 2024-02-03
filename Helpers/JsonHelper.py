import json
import os

class JsonHelper:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.file_path = os.path.join(self.root_dir, 'appsettings.json')
        self.config = self._load_config()

    def _load_config(self):
        try:
            with open(self.file_path, 'r') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            print("Configuration file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error decoding JSON from configuration file.")
            return {}

    def get_pat(self):
        return self.config.get('AppName', {}).get('PAT', None)

    def get_organization(self):
        return self.config.get('AppName', {}).get('Organization', None)

    def get_project(self):
        return self.config.get('AppName', {}).get('Project', None)

    def get_repo(self):
        return self.config.get('AppName', {}).get('Repo', None)
