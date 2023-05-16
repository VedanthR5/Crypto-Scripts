def letterCounts(text):
    # Initialize a dictionary to store the letter counts
    counts = {}

    # Convert the text to lowercase for case-insensitive counting
    text = text.lower()

    # Iterate over each character in the text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Increment the count for the letter
            counts[char] = counts.get(char, 0) + 1

    # Return the letter counts dictionary
    return counts
