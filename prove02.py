import os.path
import json
from datetime import datetime


def read_data(filename):
    try:
        with open(filename) as file:
            js_dict = json.load(file)
            return js_dict['array']
    except IOError:
        print("This file doesn't exist.")
        return -1


def advanced_search(array, element):
    start = datetime.now()
    first_member = 0
    last_member = len(array)
    step = 0
    while first_member <= last_member:
        step += 1
        mid = (first_member + last_member) // 2
        if element == array[mid]:
            return mid, datetime.now() - start
        if array[mid] < element:
            first_member = mid + 1
        else:
           last_member = mid - 1
    return -1, datetime.now() - start



def main():
    filename = "filename"
    while filename != 'q':
        filename = str(input("Please input the filename or type q to quit the program: "))
        if filename == 'q' or filename == 'Q':
            break
        else:
            data = read_data(filename)
            data.sort()
            if data == -1:
                pass
            if len(data) == 0:
                print("The file is empty!")
            else:
                word = input("What name are we looking for? ")
                result, time = advanced_search(data, word)
                if result != -1:
                    print("We found {} in {}. Performance: {}".format(word, filename, time))
                else:
                    print("{} is not in {}. Performance: {}".format(word, filename, time))
                print()



if __name__ == "__main__":
    main()
