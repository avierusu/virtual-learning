import csv
import re

def main():
    counts = {}
    words = get_words("address.txt")

    # Convert all words to lowercase using List Comprehensions
    # so count is case insensitive
    # We also only include words longer than 4 letters
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    # Count each time every word appears
    # We can use Dictionary Comprehensions instead of a loop
    counts = {word: words.count(word) for word in lowercase_words}
    # for word in lowercase_words:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1
    
    save_counts(counts)

# Implementations of get_words and save_counts provided
def get_words(file_name):
    with open(file_name, "r") as f:
        contents = f.read()
    
    contents = " ".join(contents.split())
    contents = re.sub(r"[^\w\- ]", "", contents)
    contents = re.sub(r"\-\-", " ", contents)
    return contents.split()

def save_counts(counts):
    with open("counts.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Word", "Count"])
        for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([word, count])


main()

'''
import csv
import re


def get_words(filename):
with open(filename, "r") as f:
contents = f.read()

contents = " ".join(contents.split())
contents = re.sub(r"[^\w\- ]", "", contents)
contents = re.sub(r"\-\-", " ", contents)
return contents.split()


def save_counts(counts):
with open("counts.csv", "w") as f:
writer = csv.writer(f)
writer.writerow(["Word", "Count"])
for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
writer.writerow([word, count])
'''