"""
Simple function to find the maximum value in a list of numbers
"""

def findMax(listToSearch):
    max = 0
    for d in listToSearch:
        if(d>max):
            max=d
    return max

# main method to test our function

def main():
    testList = [1,23,52,27,54,3,78,3,4,36,22,236,22358,235683,38,1]
    print("Maximum value in " + str(testList) + " is " + str(findMax((testList))))

main()

