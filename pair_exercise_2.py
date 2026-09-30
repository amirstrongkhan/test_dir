import string

# Questions 2 and 3
mystring = '"Hello, World!"'
print(mystring)

mystring = "'Hello, World!\""
print(mystring)

# Question 4
poem = """First I saw the white bear, then I saw the black;
Then I saw the camel with a hump upon his back;
Then I saw the grey wolf, with mutton in his maw;
Then I saw the wombat waddle in the straw;
Then I saw the elephant a waving of his trunk;
Then I saw the monkeys - mercy, how unpleasantly they smelt!"""

# Questions 5 and 6
print(len(poem))
print(len(set(poem)))

# Question 7
poem_nopunc = poem.translate(str.maketrans('', '', string.punctuation))

# Question 8
poem_words = poem_nopunc.split()

# Questions 9, 10, 11
print(len(poem_words))
print(len(set(poem_words)))
print(poem_words[-16])

# Question 12
print(poem_words[::-1])

for word in reversed(poem_words):
    print(word)

# Question 13
print(poem_words[::2])

for i in range(0, len(poem_words), 2):
    print(poem_words[i])

# Question 14
for word in poem_words:
    if word == "mutton":
        break
    print(word)

# Question 15
poem_tuple = tuple(poem_words)

# Question 16
slice = poem_words[38:42]

# Question 17
slice[0] = "drink"

# Question 18
poem_words.sort()

# Question 19
h_words = [word for word in poem_words if word.startswith("h")]

# Question 20
m_words = [word.upper() if "m" in word else word for word in poem_words]

# Question 21
multi_table = [[i * j for j in range(1, 13)] for i in range(1, 13)]

# Question 22
poem_lower = poem_nopunc.lower()

# Question 23
char_counts = {char: poem_lower.count(char) for char in sorted(set(poem_lower))}

# Question 24
for key, value in char_counts.items():
    if key in "aeiouy":
        print(key, value)

# Extra credit for Question 24
print({key: value for key, value in char_counts.items() if key in "aeiouy"})

# Question 25
missing_letters = [letter for letter in string.ascii_lowercase if letter not in poem_lower]
print(missing_letters)

# Extra credit for Question 25
print(set(string.ascii_lowercase) - set(poem_lower))
