import requests


post_url = "http://localhost:5000/fileupload"
get_url = "http://localhost:5000/getfile"


def select_file_for_upload():
    while True:
        file_path = input("Please enter the path/name of the file You'd like to upload:\n")
        try:
            with open(file_path, "r") as file:
                upload = requests.post(post_url, files={'file': file})
                print(upload.text)
            return
        except FileNotFoundError:
            print("There is no such file. Please check your spelling and try again.\n")


def access_server_file():
    filename = input("PLease enter the name of the file You want to access:\n")
    line = input("Please enter the number of the line you'd like to see.\n"
                 "If You want to display the whole file, press enter.\n")
    if line == '':
        line = None
    file = requests.get(get_url, params={'filename': filename, 'line': line})
    print(file.text)


action = 'c'
while action != 'q':
    print(60*"-")
    action = input("Would You like to upload or access a file? (u/a)\n")
    match action:
        case 'u':
            select_file_for_upload()
        case 'a':
            access_server_file()
        case _:
            print("Invalid action. Please try again")
    print("\nWould You like to continue? (c/q)")
    action = input()
    while action != 'c' and action != 'q':
        action = input("Invalid action. Please type c to continue or q to quit.\n")
    print(60*"-")
    print()
