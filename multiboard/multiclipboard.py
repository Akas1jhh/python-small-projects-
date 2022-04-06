import sys
import clipboard
import json

# creating a json file
SAVED_DATA = 'clipboard.json'

# saving the data to clipboard
def save_data(filename, data):
    with open(filename, 'w') as f:
      json.dump(data, f)

# loading the data from clipboard
def load_data(filename):
  try:
    with open(filename, 'r') as f:
      data = json.load(f)
      return data
  except:
    return {}    

# checking we only have one command
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
   # if command is save 
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print('Data saved')

    # if command is load    
    elif command == "load":
      key = input("Enter a key: ")
      if key in data:
        clipboard.copy(data[key])
        print('Data copied to clipboard')
      else:
        print('key does not exist')  

    # if command is list    
    elif command == "list":
      print(data)
    else:
      print('unknown command')
else:
  print('please enter a single command')            
