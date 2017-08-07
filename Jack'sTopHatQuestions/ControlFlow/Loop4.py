def main():
    animals = ["cat", "dog", "horse"]
    for animal in animals:
        if len(animal) > 3:
            animals.insert(0,animal)

        print(animals)
main()

"""
Question: What is the output of this program?:
A. [cat,dog,horse]
B. [horse,cat,dog,horse]
C. error
Purpose: Check understanding that iterating over a sequence does not implicitly make a copy, here we edited the list 
         animals, making the loop infinite since it will keep inserting "horse" at the start of the list as it has a
         length greater than three letters
Answer: C.
"""