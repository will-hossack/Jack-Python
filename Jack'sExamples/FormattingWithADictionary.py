"""
Dictionaries can be used to store information in a sequence of Key:Value 's this can then be used to print using the
.format() to format our information nicely
"""

table = {"Adam":123,"Ben":456,"Charlie":789}
# .items() returns the key:value pairs in a container that we can iterate over in the for loop
for name, number in table.items():
    print("{0:10} ==> {1:10d}".format(name,number))

