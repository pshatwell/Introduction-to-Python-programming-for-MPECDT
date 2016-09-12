import pylab
import numpy as np

xy_data = open("../data/xy.dat", "r")

# Initialise an empty list to store numbers
x_data = []
y_data = []

# Start reading numbers

n = 0
while True:  # This will keep looping until we break out.
    # Here we use a try/except block to try to read the data as normal
    # and to break out if unsuccessful - i.e. when we reach the end of the file.
    try:
        # Read the next line
        line = xy_data.readline()

        # Split this line into words.
        numbers = line.split()

        if len(numbers) != 2: #Each line should have exactly 2 numbers in it
            break

    except:
        # If we failed to read a line then we must have got to the end.
        break

    n += 1  # Count number of data points

    try:
        #Convert numbers to floats and add to x and y data lists
        x_data.append(float(numbers[0]))
        y_data.append(float(numbers[1]))

    except:
        continue

# Convert lists to numpy arrays
y = np.array(y_data)
x = np.array(x_data)

pylab.plot(x,y)
pylab.show()
