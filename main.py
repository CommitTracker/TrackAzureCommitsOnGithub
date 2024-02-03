from Helpers.AzureHelper import AzureHelper
from Helpers.GithubHelper import GithubHelper
import time

def main():
    try:
        # Initialize helpers
        azure_helper = AzureHelper()
        github_helper = GithubHelper()

        # Get all commit data from Azure
        azure_commits = azure_helper.get_all_commit_data()
        if isinstance(azure_commits, dict) and 'error' in azure_commits:
            print(f"Error fetching Azure commits: {azure_commits['error']}")
            return None

        # List files in the 'commits' directory on GitHub
        github_commits = github_helper.list_files_in_dir("commits")
        if not github_commits:  # Checks if github_commits is empty or an error occurred
            print("Error or no files found in GitHub 'commits' directory.")
            return None
        
        # Convert lists to sets for comparison
        azure_commits_set = set(azure_commits)
        github_commits_set = set(github_commits)

        # Find commits new to Azure
        new_to_azure = azure_commits_set - github_commits_set
        if not new_to_azure:
            print("No new commits in Azure to update to GitHub.")
            return None

        print(f"{len(new_to_azure)} commits to push.")

        for commit in new_to_azure:
            # Try to commit each new commit to GitHub
            try:
                github_helper.commit(commit, "commits", f"{commit}.txt")
            except Exception as e:
                print(f"Failed to commit {commit} to GitHub: {e}")

        print("Process completed successfully.")
        return None
    
    except Exception as e:
        return f"An unexpected error occurred: {e}"


if __name__ == "__main__":
    main()
        
