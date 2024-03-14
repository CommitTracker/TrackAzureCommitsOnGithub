from git import Repo
import os
from Utils.StringUtils import get_commit_id
from datetime import datetime

class GithubHelper:

    def __init__(self):
        self.repo_path = os.getcwd()
        self.repo = Repo(self.repo_path)
        

    def commit(self, commit_message, commit_location, file_name='Test.txt', file_content='', commit_date: datetime = datetime.now()):
        """
        Creates a new file with the provided content, commits it, and then pushes to the remote repository.
        
        :param commit_message: The commit message.
        :param commit_location: The relative path within the repository where the file should be created. Ensure this path exists or is created.
        :param file_name: The name of the new file.
        :param file_content: The content to write into the new file.
        :param commit_date: The date of the commit. By default, it is the current date and time. Change to make a retroactive commit
        """

        # Build the complete file path
        file_path = os.path.join(self.repo_path, commit_location, file_name)
        
        # Ensure the commit_location directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Create a new file with the content provided
        with open(file_path, 'w') as file:
            file.write(file_content)
        
        # Git add and commit
        self.repo.index.add([file_path])
        self.repo.index.commit(commit_message, commit_date=commit_date)
        #
        ## Push the changes
        origin = self.repo.remote(name='origin')
        origin.push()
        print(f'{commit_message}, Changes pushed successfully.')

    def list_files_in_dir(self, dir_path):
        """
        Lists all files in a specified directory within the repository.
        
        :param dir_path: The relative path within the repository to list files from.
        """
        commit_ids = []
        try:
            commit = self.repo.head.commit
            
            target_dir = commit.tree[dir_path]
                    
            for item in target_dir.blobs:
                file_path = item.path
                commit_id = get_commit_id(file_path)
                commit_ids.append(commit_id)  
                
            return commit_ids
        
        except KeyError:
            print(f"The directory '{dir_path}' does not exist in the current branch.")

        except Exception as e:
            print(f"An error occurred: {e}")
        
        return [] 