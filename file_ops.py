# Standard library imports
import time

def bitcoin_csv_prices(filename):
    """Reads in a file with UNIX epoch time values and corresponding
    Bitcoin prices and outputs a file with date time format
    and prices."""

    # "r" is the flag for read-only operation, "w" is for writing
    input_file = open(filename, "r")
    output_file = open("file_ops_output.txt", "w")
    output_file.write("YYYY-MM-DD HH:MM:SS (Time)   Bitcoin Prices\n")

    for line in input_file:
        # Split each line to get separate date and format it using
        # proper directives
        line = line.split(",")
        line[0] = time.strftime('%Y-%m-%d %H:%M:%S          ',
                                time.localtime(int(line[0])))

        output_file.writelines(line)

    input_file.close()
    output_file.close()

bitcoin_csv_prices("file_ops_input.csv")
