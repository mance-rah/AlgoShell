def read_file(file_name):
    # Open file and read contents
    file=open(file_name, "r")
    contents = file.read()

    return contents

def create_file_data(file_name):
    
    file_contents = read_file(file_name)
    
    file_data = {
        "name": file_name,
        "contents": file_contents
    }

    return file_data

file_name = "palindrome_check.py"
file_data = create_file_data(file_name)
solution_str = file_data['contents']
exec(solution_str)
