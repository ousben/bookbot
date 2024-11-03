# This is the main function that reads the file and prints the contents
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

# This function counts the words in the file
def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)

# This function counts the letters in the file
def count_letters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letters = {}
        for char in file_contents:
            if char.isalpha():
                letters[char] = letters.get(char, 0) + 1
        return letters

# This function prints the report
def print_report():
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words()} words found in the document")
    for letter in count_letters().keys():
        print(f"The '{letter}' character was found {count_letters()[letter]} times")
    print(f"--- End report ---")

print_report()