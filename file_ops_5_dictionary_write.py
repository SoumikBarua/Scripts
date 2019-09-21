# Local imports
from file_ops_4_shakespeare_words import word_occurrences

def most_ten_common_words():
    """Writes to a file the ten most common words found in a
    text file using helper function. In the output file, words
    and their occurrences will be separated by comma."""

    # Call helper function to get dictionary
    result_dictionary = word_occurrences("file_ops_4_input.txt")
    sorted_result = sorted(result_dictionary.items(),
                           key = lambda kv:(kv[1], kv[0]), reverse=True)

    # Set up output file for writing
    output_file = open("file_ops_5_output.csv", "w")
    output_file.write("Words, Occurrences\n")
    
    for index in range(0, 10):
        output_file.writelines(sorted_result[index][0]
                               + ", " + str(sorted_result[index][1]) + "\n")

    output_file.close()

most_ten_common_words()
