import random
iseed = 1
random.seed(iseed)
print(random.random())


"""
Question: Given that the program is run sequentially 5 times what are the outputs?:
A. 892, 148963, 12, 4442, 778
B. 0.12422222489610935, 0.65478925289263591, 0.83638623986325610, 0.99723567219071353, 0.22244785139801790
C. 0.13436424411240122, 0.13436424411240122, 0.13436424411240122, 0.13436424411240122, 0.13436424411240122
Purpose: Check understanding that pseudo-random number generators need to be seeded and that the seed 
         determines the series of random numbers completely. 
Answer: C.
"""