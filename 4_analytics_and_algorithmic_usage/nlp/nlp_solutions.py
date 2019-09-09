# NLP SOLUTIONS


## Task 2 Write a Python program that matches a word at the beginning of a string.

Make this into a runnable script. Refer to [this](https://stackoverflow.com/questions/4042905/what-is-main-py)

Solution:

import re
def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))


## Task 3
Write a Python program that matches a word at end of string, with optional punctuation.
Make this into a runnable script. Refer to [this](https://stackoverflow.com/questions/4042905/what-is-main-py)

import re
def text_match(text):
        patterns = '\w+\S*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))


## Task 4 : Date Extraction

Write a Python program to extract year, month and day from an url.
Make this into a runnable script. Refer to [this](https://stackoverflow.com/questions/4042905/what-is-main-py)

import re
def extract_date(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1))

## Task 4 : Date Conversion

Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
Make this into a runnable script. Refer to [this](https://stackoverflow.com/questions/4042905/what-is-main-py)

Solution :

import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))
