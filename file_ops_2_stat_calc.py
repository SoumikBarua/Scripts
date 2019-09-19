# Standard library imports
import time, math, statistics

def math_and_std_dev(file_name):
    """Reads in a csv file with UNIX epoch time values and corresponding
    Bitcoin prices to calculate the max, min, mean and the standard
    deviation."""
    
    file = open(file_name, "r")

    # Extract the first listed price & set up variables for calculation
    total_number_of_values = 1
    sum_of_all_values = float(file.readline().strip("\n").split(",")[1])
    
    maximum_value = sum_of_all_values + 0.00
    maximum_date = ""
    minimum_value = sum_of_all_values + 0.00
    minimum_date = ""

    # Iterate through the values to update max, min, and sum
    for line in file:
        line = line.strip("\n").split(",")
        current_value = float(line[1])
        current_date = int(line[0])
        
        if (maximum_value < current_value):
            maximum_value = current_value
            maximum_date = time.strftime('%Y-%m-%d %H:%M:%S',
                                         time.localtime(current_date))

        if (minimum_value > current_value):
            minimum_value = current_value
            minimum_date = time.strftime('%Y-%m-%d %H:%M:%S',
                                         time.localtime(current_date))

        total_number_of_values += 1
        sum_of_all_values += current_value

    mean = sum_of_all_values/total_number_of_values

    file.close()

    # Open file again for standard deviation calculation, EOF reached
    standard_dev_total = 0.00
    median_list = []
    file = open(file_name, "r")

    for line in file:
        value = float(line.strip("\n").split(",")[1])
        standard_dev_total += math.pow((value-mean), 2)
        median_list.append(value)

    standard_dev = math.sqrt(standard_dev_total/total_number_of_values)
    median = statistics.median(median_list)

    print("Max Bitcoin price is ${p:.2f}".format(p=maximum_value)
          + " with a timestamp " + maximum_date)
    print("Min Bitcoin price is ${p:.2f}".format(p=minimum_value)
          + " with a timestamp " + minimum_date)
    print("Mean price is ${p:.2f}".format(p=mean))
    print("Standard deviation of prices is {p:.2f}".format(p=standard_dev))
    print("Median price is ${p:.2f}".format(p=median))

math_and_std_dev("file_ops_input.csv")
