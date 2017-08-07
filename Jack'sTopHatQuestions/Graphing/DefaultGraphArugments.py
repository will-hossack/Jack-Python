import matplotlib.pyplot as plt

x = [i for i in range(-100,100)]
xSquared = [i*i for i in range(-100,100)]
plt.plot(x,xSquared)
plt.show()

"""
Question: What colour is the graph?:
          A. Black
          B. Blue
          C. error, plot colour not specified
Purpose:  Check understanding that some functions take default arguments, so that the programmer doesn't need to 
          specify them. In the case of plot it defaults to blue.
Answer: B.
"""
