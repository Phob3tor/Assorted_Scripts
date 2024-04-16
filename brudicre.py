import os
import sys
import string
from tqdm import tqdm

digit_list = [*string.digits]
punct_list = [*string.punctuation]
whole_list = digit_list + punct_list

if len(sys.argv) != 2:
    print("You have to specify exactly 1 argument for the file name!")
else:
    file_name = sys.argv[1]

def start_script():
    print("Welcome to the dictionary creator!")
    print("Please specify all the words the dictionary should contain seperated by: ?")
    user_input = input("Your words: ")
    
    return user_input

def create_list(user_input):
    if "?" in user_input:
        try:
            user_list = user_input.split("?")
            return user_list
        except:
            print("It seems your input doesn't meet the conditions!")
    elif len(user_input) > 0:
        return list(user_input)
    else:
        print("You have to provide some input!")

def arg_string(entry, *args):
    string_list = []
    str_args = []

    for arg in args:
        str_args.append(str(arg))

    con_args = "".join(str_args)

    string_list.append(f"{entry}{con_args}")
    string_list.append(f"{entry.upper()}{con_args}")
    string_list.append(f"{entry.capitalize()}{con_args}")
    
    string_list.append(f"{con_args}{entry}")
    string_list.append(f"{con_args}{entry.upper()}")
    string_list.append(f"{con_args}{entry.capitalize()}")

    if len(con_args) == 1:
        string_list.append(f"{entry}{con_args[0]}")
        string_list.append(f"{entry.upper()}{con_args[0]}")
        string_list.append(f"{entry.capitalize()}{con_args[0]}")
            
        string_list.append(f"{con_args[0]}{entry}")
        string_list.append(f"{con_args[0]}{entry.upper()}")
        string_list.append(f"{con_args[0]}{entry.capitalize()}")

    if len(con_args) == 2:
        string_list.append(f"{con_args[0]}{entry}{con_args[1]}")
        string_list.append(f"{con_args[0]}{entry.upper()}{con_args[1]}")
        string_list.append(f"{con_args[0]}{entry.capitalize()}{con_args[1]}")
            
        string_list.append(f"{con_args[1]}{entry}{con_args[0]}")
        string_list.append(f"{con_args[1]}{entry.upper()}{con_args[0]}")
        string_list.append(f"{con_args[1]}{entry.capitalize()}{con_args[0]}")

    if len(con_args) == 3:
        string_list.append(f"{con_args[0]}{con_args[1]}{entry}{con_args[2]}")
        string_list.append(f"{con_args[0]}{con_args[1]}{entry.upper()}{con_args[2]}")
        string_list.append(f"{con_args[0]}{con_args[1]}{entry.capitalize()}{con_args[2]}")
            
        string_list.append(f"{con_args[0]}{entry}{con_args[1]}{con_args[2]}")
        string_list.append(f"{con_args[0]}{entry.upper()}{con_args[1]}{con_args[2]}")
        string_list.append(f"{con_args[0]}{entry.capitalize()}{con_args[1]}{con_args[2]}")

    if len(con_args) == 4:
        string_list.append(f"{con_args[0]}{entry}{con_args[1]}{con_args[2]}{con_args[3]}")
        string_list.append(f"{con_args[0]}{entry.upper()}{con_args[1]}{con_args[2]}{con_args[3]}")
        string_list.append(f"{con_args[0]}{entry.capitalize()}{con_args[1]}{con_args[2]}{con_args[3]}")

        string_list.append(f"{con_args[0]}{con_args[1]}{entry}{con_args[2]}{con_args[3]}")
        string_list.append(f"{con_args[0]}{con_args[1]}{entry.upper()}{con_args[2]}{con_args[3]}")
        string_list.append(f"{con_args[0]}{con_args[1]}{entry.capitalize()}{con_args[2]}{con_args[3]}")
            
        string_list.append(f"{con_args[0]}{con_args[1]}{con_args[2]}{entry}{con_args[3]}")
        string_list.append(f"{con_args[0]}{con_args[1]}{con_args[2]}{entry.upper()}{con_args[3]}")
        string_list.append(f"{con_args[0]}{con_args[1]}{con_args[2]}{entry.capitalize()}{con_args[3]}")



    return string_list

def make_brute_dict(user_list):
    full_list = []
    
    for entry in user_list:
        full_list.append(entry)
        full_list.append(entry.upper())
        full_list.append(entry.capitalize())
        
        
        
        for i1 in tqdm(whole_list, desc=f"Processing word '{entry}'"):
            full_list += arg_string(entry, i1)
            
            for i2 in range(0, len(whole_list)):
                full_list += arg_string(entry, i1, i2)
            
                for i3 in range(0, len(whole_list)):
                    full_list += arg_string(entry, i1, i2, i3)
            
                    for i4 in range(0, len(whole_list)):
                        full_list += arg_string(entry, i1, i2, i3, i4)
                        
    return full_list
    
def write_to_file(file_name, user_list):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, f"{file_name}.txt")
    
    with open(file_path, "a", encoding="utf-8") as file:
        for entry in tqdm(user_list, desc="Writing to file"):
            file.write(str(entry) + "\n")

def execute_script():
    user_input = start_script()
    
    user_list = create_list(user_input)
    
    full_list = make_brute_dict(user_list)
    
    write_to_file(file_name, full_list)

execute_script()
