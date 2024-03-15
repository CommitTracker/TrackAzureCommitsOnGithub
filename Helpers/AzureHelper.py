from bs4 import BeautifulSoup
import json
import requests
import base64

class AzureHelper:
    def __init__(self, data, track_only_master: bool = True):
        self.track_only_master = track_only_master
        self.branches = list()
        self.pat = data["PAT"]
        self.organization = data["Organization"]
        self.project = data["Project"]
        self.repo = data["Repo"]
        self.commits_url = f"https://dev.azure.com/{self.organization}/{self.project}/_apis/git/repositories/{self.repo}/commits"
        self.branches_url = f"https://dev.azure.com/{self.organization}/{self.project}/_git/{self.repo}/branches"
        self.username = data["Username"]

    def _get_headers(self):
        pat_token = ':' + self.pat
        base64_pat = base64.b64encode(pat_token.encode()).decode()
        return {'Authorization': f'Basic {base64_pat}'}
    
    def get_all_branches(self):
        response = requests.get(f"{self.branches_url}", headers=self._get_headers())
        soup = BeautifulSoup(response.text, 'html.parser')
        json_element = json.loads(soup.find('script', id='dataProviders').contents[0])
        if self.track_only_master:
            branches_data = json_element['data']['ms.vss-code-web.my-branches-data-provider']['Git.Branches.Default']
            branches_names = [branches_data['name'].split('/')[-1]]
            print(f'Tracking only {branches_names[0]} branch, if you want to track all branches in {self.repo}, please set "Track_only_master" to false in appsettings.json!')
        else:
            branches_data = json_element['data']['ms.vss-code-web.my-branches-data-provider']['Git.Branches.Mine']
            branches_names = [branch['name'].split('/')[-1] for branch in branches_data]
            print(f'Tracking all branches in {self.repo}: {branches_names}')
        self.branches = branches_names

    def get_all_commit_data(self):
        self.get_all_branches() # Get all branches data
        commits = list()
        for branch in self.branches:
            response = requests.get(f"{self.commits_url}?api-version=7.1&searchCriteria.author={self.username}&searchCriteria.itemVersion.version={branch}", headers=self._get_headers())
            if response.status_code != 200:
                return {"error": f"Failed to retrieve commits. Status code: {response.status_code}"}
            data = response.json()
            if 'value' in data:
                commits.extend(data['value'])
                last_count = data['count']
                commit_offset = last_count
                while last_count == 100: # Paging results
                    response = requests.get(f"{self.commits_url}?api-version=7.1&searchCriteria.author={self.username}&searchCriteria.itemVersion.version={branch}&searchCriteria.$skip={commit_offset}", headers=self._get_headers())
                    data = response.json()
                    commits.extend(data['value'])
                    last_count = data['count']
                    commit_offset += data['count']
                print(f"Found {commit_offset} commits in branch: {branch}") 
            else:
                print(f"No commits found in {branch}")
        return commits

    def get_last_commit_data(self):
        response = requests.get(f"{self.base_url}?api-version=6.0&top=1&searchCriteria.author={self.username}", headers=self._get_headers())
        if response.status_code == 200:
            data = response.json()
            if 'value' in data and len(data['value']) > 0:
                return data['value'][0]
            else:
                return {"error": "No commits found."}
        else:
            return {"error": f"Failed to retrieve the last commit. Status code: {response.status_code}"}
