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

print(count_words())