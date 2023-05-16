def number_to_words(n):
  
    ones_words = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]

    tens_words = [ "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

   
    hundreds_word = "hundred"
    thousands_word = "thousand"

    if n == 1000:
        return "one thousand"

    words = ""
    if n // 100 > 0:
        words += ones_words[n // 100] + " " + hundreds_word
        if n % 100 > 0:
            words += " and "

    n %= 100
    if n < 20:
        words += ones_words[n]
    else:
        words += tens_words[n // 10]
        if n % 10 > 0:
            words += " " + ones_words[n % 10]

    return words


def count_letters_in_numbers():
    total_letters = 0

    for i in range(1, 1001):
        words = number_to_words(i)
        letters = len(words.replace(" ", "").replace("-", ""))
        total_letters += letters

    return total_letters


# Calculate the total number of letters used from 1 to 1000
total_letters = count_letters_in_numbers()
print("Total number of letters used from 1 to 1000:", total_letters)
