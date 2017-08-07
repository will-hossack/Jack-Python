"""
A function to format a number of seconds into a string of the form H:M:S.M. This type of function might be
useful if you were measuring the time it takes for your code to run and wanted to print it in a nice format.
"""

def formatSeconds(time):

    # The implementation of the formatting is perhaps a little confusing at first. Here we are using the int
    # conversion in order to round down the time after dividing by the corresponding demonination for that unit
    # we use the mod operator to unsure we dont "spill over" into the smaller units

    hours   = (int(time/3600.0))%24
    minutes = (int(time/60.0))%60
    seconds = (int(time))%60
    millis  = (int(time*1000.0))%1000

    # use the .format function to get the appropriate decimal places for the numbers.
    formattedTime = "{0:0.0f}:{1:0.0f}:{2:0.0f}.{3:0.0f}".format(hours,minutes,seconds,millis)

    return  formattedTime

# short main method to test our function for a given user input.
def main():
    # prompt user for input
    t = float(input("Enter a number of seconds: "))
    #print user input formatted by our function
    print(str(t)+"s is: "+formatSeconds(t))

main()


