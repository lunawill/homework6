# SI 206
# HW6 - Regular Expressions
# Name: William Luna
# Who did you work with:　Angel Ranjel, Hamza Asad

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
    x = r"\b[1-9][0-2]?:[0-5][0-9]\s[ap]m" 
    s_list = []
    for lines in string_list:
        strings = re.findall(x, lines)
        for index in strings:
            s_list.append(index)

    return s_list





def find_urls(string_list):

    """ Return a list of valid urls in the list of strings """
    #new line character to watch out, potential r strip

    x = r"\b(?:http|https):\/\/www\..+\w(?:.com|.org).*"
    s_list = []
    for lines in string_list:
        strings = re.findall(x, lines)
        for index in strings:
            s_list.append(index)

    return s_list



def find_dates(string_list):
    """ Return a list of dates in the list of strings """ 
    x = r"\b[0-3][0-9]+(?:\/|\-|\.)+[0-3][0-9]+(?:\/|\-|\.)+\d{4}"

    s_list = []
    for lines in string_list:
        strings = re.findall(x, lines)
        for index in strings:
            s_list.append(index)

    return s_list

def count_char(string_list, char):
    """  return a count of the number of times a specified character appears in a list of strings. 
         It should match the character when it starts or ends a word 
         (It should not match any characters in the middle of a word)
    
        string_list -- the list of strings to count the char in
        char -- the character to look for
        return -- a count of the number of times the word or its plural appears in the file 
    """
    count = 0
    x = rf"^{char}"
    y = rf"{char}$"

    for lines in string_list:
        words = lines.split()
        print (words)
        
        for i in words:
            if re.search(x, i) != None:
                count +=1
            elif re.search(y, i) !=None:
                count +=1
            else:
                count = count       



    


# Implement your own tests.    
class TestAllMethods(unittest.TestCase):


    def test_find_times(self):
        string_list = read_file('alice_in_wonderland.txt')
        timesTest = find_time(string_list)
        self.assertEqual(len(timesTest), 5)
        self.assertEqual(timesTest, ["6:00 pm", "12:25 am", "12:00 pm", "11:11 pm",  "10:05 am"])
        self.assertIsNot(len(timesTest), 0)
        

    def test_find_urls(self):
        string_list = read_file('alice_in_wonderland.txt')
        urlTest = find_urls(string_list)
        self.assertEqual(len(urlTest), 5)
        self.assertEqual(urlTest, ["https://www.goodreads.com/work/quotes/2933712-alice-in-wonderland", "https://www.youtube.com/watch?v=rPK67tnsfZc", "https://www.youtube.com/watch?v=msvOUUgv6m8", "https://www.pythex.com",  "http://www.gutenberg.org/1/11/"])
        self.assertIsNot(len(urlTest), 0)

    def test_find_dates(self):
        string_list = read_file('alice_in_wonderland.txt')
        dateTest = find_dates(string_list)
        self.assertEqual(len(dateTest), 7)
        self.assertEqual(dateTest, ["06/08/2020", "06-08-2020", "06-05-2010", "26/07/1951",  "04-05-1865", "26.11.1865", "26.11.1865"])
        self.assertIsNot(len(dateTest), 0)

    def test_char(self):
        char = 'a'
        string_list = read_file('alice_in_wonderland.txt')
        charTest = count_char(string_list, char)
        self.assertEqual(charTest, 3850)


        




def main():
	# Use main to test your function. 
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()