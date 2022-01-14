"""
1 - Write a Python program to import built-in array module and display the namespace of the said module.
"""

import array

for n in array.__dict__:
    print(n)

# for n in array.__dict__:
#     if not n.startswith('_'):
#         print(n)
