# Standard library imports
import math

def pearson_correlation(file_name):
    """Reads in a csv file with UNIX epoch time values and corresponding
    Bitcoin prices to calculate the Pearson correlation between the
    prices and the timestamps.
    Note: Pearson correlation indicates how two variables are linearly
    related and ranges from -1 to 1."""

    file = open(file_name, "r")

    # Set up the variables for Pearson correlation equation
    sigma_xy = 0
    sigma_x = 0
    sigma_y = 0
    n = 0
    sigma_x_squared = 0
    sigma_y_squared = 0
    pearson_numerator = 0.0
    perason_denominator = 0.0

    for line in file:
        line = line.strip("\n").split(",")
        sigma_xy += float(line[0]) * float(line[1])
        sigma_x += float(line[0])
        sigma_y += float(line[1])
        n += 1
        sigma_x_squared += math.pow(float(line[0]), 2)
        sigma_y_squared += math.pow(float(line[1]), 2)

    # Set up the division
    pearson_numerator = sigma_xy - ((sigma_x*sigma_y)/n)
    pearson_denominator = math.sqrt((sigma_x_squared - (math.pow(sigma_x, 2)/n))
                                    *(sigma_y_squared - (math.pow(sigma_y,2)/n)))
    coefficient = pearson_numerator/pearson_denominator
    
    print ("The Pearson correlation between Unix timestamps and Bitcoin prices"
           + " is " + str(coefficient))
    
pearson_correlation("file_ops_1&2&3_input.csv")
