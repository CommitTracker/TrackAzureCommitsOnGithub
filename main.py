from datetime import datetime
from Helpers.AzureHelper import AzureHelper
from Helpers.GithubHelper import GithubHelper
from Helpers.JsonHelper import JsonHelper
import pytz

def main():
    JsHelper = JsonHelper()
    apps_data = JsHelper.GetData()
    local_tz = datetime.now(pytz.timezone('UTC')).astimezone().tzinfo
    
    try:
        # Initialize helpers
        for data in apps_data:
            print("")
            azure_helper = AzureHelper(data, track_only_master=data['Track_only_master'])
            github_helper = GithubHelper()

            # Get all commit data from Azure
            azure_commits = azure_helper.get_all_commit_data()
            if isinstance(azure_commits, dict) and 'error' in azure_commits:
                print(f"Error fetching Azure commits: {azure_commits['error']}")

            # List files in the 'commits' directory on GitHub
            github_commits = github_helper.list_files_in_dir("commits")
            if not github_commits:  # Checks if github_commits is empty or an error occurred
                print("Error or no files found in GitHub 'commits' directory.")

            # Convert lists to sets for comparison
            azure_commits_set = set([commit['commitId'] for commit in azure_commits])
            github_commits_set = set(github_commits)

            # Find commits new to Azure
            new_to_azure = azure_commits_set - github_commits_set

            new_azure_commits = list(filter(lambda commit: commit['commitId'] in new_to_azure, azure_commits))

            unique_azure_commits = [commit for i, commit in enumerate(new_azure_commits) if commit not in new_azure_commits[:i]]

            print(f"Found {len(unique_azure_commits)} unique commits in {data['Organization']}/{data['Project']}/{data['Repo']}.")

            if not new_to_azure:
                print(f"No new commits in {data['Organization']}/{data['Project']}/{data['Repo']} to update to GitHub.")

            print(f"{len(new_to_azure)} commits to push from {data['Organization']}/{data['Project']}/{data['Repo']}.")

            for commit in unique_azure_commits:
                # Try to commit each new commit to GitHub
                try:
                    date_format = '%Y-%m-%dT%H:%M:%SZ'
                    commit_date = datetime.strptime(commit['committer']['date'], date_format).replace(tzinfo=local_tz)
                    github_helper.commit(commit['comment'], "commits", f"{commit['commitId']}.txt", commit_date=commit_date)
                except Exception as e:
                    print(f"Failed to commit {commit} to GitHub: {e}")

        print("\nProcess completed successfully.")

    
    except Exception as e:
        return f"An unexpected error occurred: {e}"


if __name__ == "__main__":
    main()
        
