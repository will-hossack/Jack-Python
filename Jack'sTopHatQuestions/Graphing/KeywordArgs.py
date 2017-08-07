import random
import matplotlib.pyplot as plt



point = 10000
gauss_data = []
mean = 20.0
sd = 2.0


while point >= 0:
    gauss_data.append(random.gauss(mean,sd))
    point -= 1


plt.hist(gauss_data, rangge = 40, bines = [mean - 3*sd , mean + 3*sd])
plt.show()

"""
Question: What will the above code plot?:
          A. A histogram with gauss_data,  40 bins, [range mean - 3*sd , mean + 3*sd] 
          B. A blank plot
          C. error
Purpose:  Check understanding that some functions require keyword arguments and that these must be spelt correctly
Answer: C.
"""
