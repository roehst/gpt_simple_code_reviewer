import subprocess
import sys
import openai

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

def ask_for_feedback_from_openai(code):

    # response = openai.Edit.create(
    #     model="text-davinci-edit-001",
    #     input=code,
    #     instruction="Add types.",
    #     temperature=0.5,
    # )

    # Ask GPT if we can improve the code and how.
    prompt = f"""
    Please, act as a senior code reviewer and give feedback on the following code by taking into account
    the following aspects:

    1. Is the code easy to read?
    2. Does it have documentation?
    3. Are the variable names adequate?

    The code is:

    {code}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }])
    



    return response.choices[0]['message']['content']

def main():

    # The filename to read is in the first argument.
    filename = sys.argv[1]

    # Get the hash of the git object for the filename.
    hash = get_git_object_hash_for_filename(filename).decode('utf-8').strip()

    contents = read_git_object(hash).decode('utf-8')

    new_contents = ask_for_feedback_from_openai(contents)

    print(new_contents)


if __name__ == '__main__':
    main()