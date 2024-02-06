import requests
from Helpers.JsonHelper import JsonHelper
import base64

class AzureHelper:
    def __init__(self, data):
        self.pat = data["PAT"]
        self.organization = data["Organization"]
        self.project = data["Project"]
        self.repo = data["Repo"]
        self.base_url = f"https://dev.azure.com/{self.organization}/{self.project}/_apis/git/repositories/{self.repo}/commits"

    def _get_headers(self):
        """Prepare authorization headers with Base64 encoded PAT."""
        pat_token = ':' + self.pat  # Username is empty, PAT is the password
        base64_pat = base64.b64encode(pat_token.encode()).decode()
        return {'Authorization': f'Basic {base64_pat}'}

    def get_all_commit_data(self):
        response = requests.get(f"{self.base_url}?api-version=6.0", headers=self._get_headers())
        if response.status_code == 200:
            data = response.json()
            if 'value' in data:
                commit_ids = [commit['commitId'] for commit in data['value']]
                return commit_ids  # Return a list of commit IDs
            else:
                return {"error": "No commits found."}
        else:
            return {"error": f"Failed to retrieve commits. Status code: {response.status_code}"}

    def get_last_commit_data(self):
        response = requests.get(f"{self.base_url}?api-version=6.0&top=1", headers=self._get_headers())
        if response.status_code == 200:
            data = response.json()
            if 'value' in data and len(data['value']) > 0:
                return data['value'][0]  # Return the first (latest) commit
            else:
                return {"error": "No commits found."}
        else:
            return {"error": f"Failed to retrieve the last commit. Status code: {response.status_code}"}
