# -*- coding: utf-8 -*-
"""minimalNLP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oQNnAX6lZ1cWSgCgDBw-Elz0hq-TiGC3
"""

print("i'm okay")

print("i'm okay \nso what? \n okay")

print("i'm okay \nso what? \tokay")

print("i'm okay \nso what? \rokay")

print("i'm okay what? \rokay")

import re

"""## re.match()"""

string="007 james bond wants"
pattern=r'\d+'
matching=re.match(pattern,string)
matching.group()

string= "123456789 james bond wants"
pattern=r'\d+'
matching=re.search(pattern,string)
matching.group()

"""##re.findall"""

string= "123456789 james bond wants"
pattern=r'\d+'
matching=re.findall(pattern,string)
matching

string= "** james bond wants"
pattern=r'\d+'
matching=re.findall(pattern,string)
matching

"""##re.sub()"""

string= "1 2 3 456789 james bond wants"
pattern=r'\d+'
matching=re.sub(pattern,'#',string)
matching

# Test case
text = """
Hello world! Contact us at info@example.com or support123@company.org. Follow us on social media: #AI #MachineLearning.
Visit <a href="http://example.com">our website</a> for more details. This is a test with number 1234.
"""

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern, text)
print(emails)

hash_tags = re.findall(r'#\w+',text)
hash_tags

