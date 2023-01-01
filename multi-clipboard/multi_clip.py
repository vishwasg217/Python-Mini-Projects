import clipboard
import sys
import json

FILENAME = "clip.json"

def save(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load(filepath):
    try:
        with open(filepath, "r") as f:
            data=json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data=load(FILENAME)

    if command == "save":
        print("---")
        key = input("Enter a key: ")
        data[key]=clipboard.paste()
        save(FILENAME, data)
        print("Data saved")

    elif command == "load":
        key=input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard")
        else: 
            print("key doesn't exist")

    elif command == "list":
        print(data)

    else:
        print("Invalid command")

else:
    print("print only one command")