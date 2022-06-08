import re

file = "../assets/madlibTemp.txt"


def opening():
    print("""
  **************************************
  ** Welcome to the Madlib Experience!**
  ***************************************
  """)


def word_list(arr):
    word_array = []
    for i in arr:
        response = input(f'Please enter a {i}:')
        word_array.append(response)
    return word_array


def read_template(template):
    with open(template, 'r') as read_file:
        read_text = read_file.read()
        return read_text


def parse_template(template):
    '''
    This is the parse_template
    it will take a tuple as a input
    with that file it will format out the words Adjective and Noun to {}
    then it will go through that same tuple and find all the words that were taken out and return a list
    it will then convert that new list into a tuple
    it will then return the tuple formated and the words seperated
    parse_template("It was a {Adjective} and {Adjective} {Noun}.") = 'It was a {} and {} {}' and ('dark', 'stormy', 'night')'''
    expected_stripped = r"{([\w ',.-]+)}"
    expected_parts_list = tuple(re.findall(expected_stripped, template))
    expected_parts = re.sub(expected_stripped, '{}', template)
    return expected_parts, expected_parts_list


def merge(string, words):
    '''
    This is the merge function
    it will take a string and a tuple with 3 options
    with that it will format the string to now include the options within the tuple
    then it will return that newly formed string
    merge("It was a {} and {} {}.", ("dark", "stormy", "night") = 'It was a dark and story night'
    '''
    return string.format(*words)


def save_file(mad_lib):
    with open("../assets/output.txt", 'w') as written_file:
        text = written_file.write(mad_lib)


if __name__ == "__main__":
    opening()
    template = read_template(file)
    expected_parts, expected_parts_list = parse_template(template)
    word_text = word_list(expected_parts_list)
    mad_lib = merge(expected_parts, word_text)
    save_file(mad_lib)
    print(mad_lib)
    print('Finished your Madlib!')