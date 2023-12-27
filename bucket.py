from collections import defaultdict
# Function to accumulate words into alphabet buckets
def accumulate_words_by_alphabet(file_path):
    try:
        # Initialize an empty dictionary to store alphabet buckets
        alphabet_buckets = defaultdict(list)
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Iterate through each line in the file
            for line in lines:
                words = line.split()
                for word in words:
                    # Convert the word to lowercase for case-insensitivity
                    word = word.lower()
                    # Check if the word starts with an alphabet character
                    if word[0].isalpha():
                        first_letter = word[0]
                        alphabet_buckets[first_letter].append(word)
            return alphabet_buckets
    except FileNotFoundError:
        return None
# Specify the path to your text file
file_path = 'note.txt'
# Call the function to accumulate words into alphabet buckets
result = accumulate_words_by_alphabet(file_path)
# Print the results
if result:
    for letter, words in result.items():
        if words:
            print(f"'{letter}': {', '.join(words)}")
        else:
            print("File not found.")
