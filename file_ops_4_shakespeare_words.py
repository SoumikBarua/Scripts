
def word_occurrences(file_name):
    """Parses a text file to return a dictionary with words in the file
    as keys and the word occurrences as values."""

    # Open file with 'utf-8' encoding to address ascii codec failing to
    # decode 0xe2
    file = open(file_name, "r", encoding="utf-8")

    dictionary = {}
    unique_words_counter = 0

    # Sentence endings . ? !
    # Sentence pauses , ; :
    # Compound words -
    # Containers () [] {}
    # Possessive or contraction '
    # Quotes and others ' " #
    
    punctuations = '.?!,;:()[]{}#"'

    for line in file:
        # Ignore empty lines
        if len(line)==1:
            continue
        else:
            # Strip newline, split by space
            # Remove '-' only at the end to preserve compound words
            # Inspect each word for other punctuation marks
            # Add to dictionary if alphabetic
            # Consider special cases for poetic contraction, compound
            
            line = line.strip("\n").split(" ")

            for word in line:
                word = word.lower().strip("-")

                for punc in punctuations:
                    if punc in word:
                        word = word.replace(punc, "")

                if word.isalpha() or '-' in word or "'" in word:
                    if word in dictionary:
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1
                        unique_words_counter += 1

            # TODO: Consider merging contractions with normal spelling
            # e.g. "'t" would be counted as "it"


    file.close()
    
    print("There are " + str(unique_words_counter) + " unique words!")
    return (dictionary)
            
#word_occurrences("file_ops_4_input.txt")
