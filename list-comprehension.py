# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# Listing those files from the directory that ends with .jpg format

import os 

files=[file for file in os.listdir('D:\\Temp') if file.endswith('.jpg')]
print(files)


# +
#TO filter those numbers greater than 5

numbers=[numb for numb in [1,2,3,4,5,6,7,8,9,10] if numb>5]
numbers


# -

# TO list pairs
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print(pairs)


# +
# To list all files 

files=[file for file in os.listdir('D:\\Temp') if file.endswith('.jpg')]
files


# +
# TO convert a;; of them in upper casing 

file=[f.upper() for f in files]
file

# +
# To list those files with name length smaller than 8

l5=[file for file in files if len(file)<=8]
l5

# +
# Write a list comprehension to create a list of the squares of even numbers from 0 to 20.

sqn_num=[n*n for n in range(0,21) if n%2==0]
sqn_num



# +
# Extract filenames that contain the letter 'a'

file_with_a=[f for f in files if 'a' in f]
file_with_a

