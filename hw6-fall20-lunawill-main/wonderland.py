# SI 206
# HW6 - Regular Expressions
# Name: William Luna
# Who did you work with:　Angel Ranjel 

import re
import os
import unittest

def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """
    
    # Open the file and get the file object
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, filename)
    infile = open(full_path,'r', encoding='utf-8')
    
    # Read the lines from the file object into a list
    lines = infile.readlines()
    
    # Close the file object
    infile.close()
    
    # return the list of lines
    return lines

            
def find_time(string_list):    
    """ Return a list of valid times from the list of strings. 
    
        string_list -- the name of the file to read from
        return -- the list of all times from a list of strings
    """
    x = "\b[1-9][0-2]?:[0-5][0-9]\s[ap]m" 
    string_list = []
    for lines in string_list:
        strings = re.findall(x, lines)
        for index in strings:
            string_list.append(x)

    return string_list





def find_urls(string_list):

    """ Return a list of valid urls in the list of strings """
    #new line character to watch out, potential r strip

    x = "\b(?:http|https):\/\/www\..+\w(?:.com|.org)"
    string_list = []
    for lines in string_list:
        strings = re.findall(x, lines)
        for index in strings:
            string_list.append(x)

    return string_list



def find_dates(string_list):
    """ Return a list of dates in the list of strings """ 
    x = "\b[0-3][0-9]+(?:\/|\-|\.)+[0-3][0-9]+(?:\/|\-|\.)+\d{4}"

    string_list = []
    for lines in string_list:
        strings = re.findall(x, lines)
        for index in strings:
            string_list.append(x)

    return string_list


# Implement your own tests.    
class TestAllMethods(unittest.TestCase):


    def test_find_times(self):
        string_list = read_file('alice_in_wonderland')

        
        pass


    def test_find_urls(self):
        pass

    def test_find_dates(self):
        pass




def main():
	# Use main to test your function. 
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()