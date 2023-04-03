import subprocess

def read_git_object(hash):
    """Read a git object from the object store.

    Args:
        hash: The hash of the object to read.

    Returns:
        The object data.
    """
    return subprocess.check_output(['git', 'cat-file', '-p', hash])

def get_git_object_hash_for_filename(filename):
    """Get the hash of the git object for a given filename.

    Args:
        filename: The filename to get the hash for.

    Returns:
        The hash of the git object.
    """
    return subprocess.check_output(['git', 'rev-parse', 'HEAD:' + filename])

