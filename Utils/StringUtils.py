def get_commit_id(file_path):
    """
    Extracts the commit id from a given file path formatted like 'commits/<commit_id>.txt'.
    
    :param file_path: The file path containing the commit hash.
    :return: The extracted commit hash or an empty string if not found.
    """
    # Split the path by '/' and get the last segment (filename)
    segments = file_path.split('/')
    if len(segments) > 1:
        filename = segments[-1]
        commit_id = filename.split('.')[0]
        return commit_id
    else:
        print("Invalid file path format.")
        return ""