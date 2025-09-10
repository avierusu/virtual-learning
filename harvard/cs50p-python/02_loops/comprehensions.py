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

# Implementation of get_words() and save_counts() not provided
def get_words():
    ...

def save_counts():
    ...


main()