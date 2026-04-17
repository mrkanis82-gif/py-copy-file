import os


def copy_file(command: str) -> None:
    try:
        file_name = command.split()[1]
        new_file_name = command.split()[2]
    except IndexError:
        return
    if (file_name == new_file_name
            or command.split()[0] != "cp"
            or file_name not in os.listdir(".")) :
        pass
    else:
        with (open(file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())
