import sys
import string

punctuation_list = [*string.punctuation, "–"]

def read_txt(path):
    with open(path, "r") as file:
        text = file.read()
        return text
    
def strip_txt(text):
    start_list = text.split()
    end_list = []
    for word in start_list:
        word = word.strip()
        for punctuation in punctuation_list:
            if punctuation in word:
                word = word.replace(punctuation, "")
        if word != "":
            end_list.append(word.lower())
                
    return end_list

def count_words(word_list):
    word_dict = {}
    
    for word in word_list:
        if not word in word_dict.keys():
            word_dict[word] = word_list.count(word)
            
    return word_dict

def get_max(word_dict):
    highest_value = max(word_dict.values())
    
    highest = [key for key in word_dict if word_dict[key] == highest_value]
    highest.append(highest_value)
    
    return highest

def pretty_print(highest):
    print("-------------------------------------------------------")
    print(f"The most occuring word is: {highest[0]}")
    print(f"It occurs {highest[1]} times")
    print("-------------------------------------------------------")

def get_highest(path):
    plain_text = read_txt(path)  
    text_list = strip_txt(plain_text)
    text_dict = count_words(text_list)
    highest = get_max(text_dict)
    pretty_print(highest)

if len(sys.argv) == 2:
    if sys.argv[1] != "-h":
        try:
            get_highest(sys.argv[1])
        except:
            print("Incorrect path or the file doesn't exist!")
    else:
        print("Example: python3 show_highest.py /home/user/the_great_gatsby.txt")
elif len(sys.argv) == 1:
    print("You need to specify a path to the text file as the first argument.")
    print("Try -h for help!")
else:
    print("You've provided an incorrect amount of arguments.")
    print("Try -h for help!")
