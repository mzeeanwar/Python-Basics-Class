# Advanced String Operations

sentence = "Python is powerful"

# Splitting
words = sentence.split()
print("Words:", words)

# Joining
joined = "-".join(words)
print("Joined:", joined)

# Replace
new_sentence = sentence.replace("powerful", "awesome")
print("Replaced:", new_sentence)

# Check substring
print("Contains 'Python'? :", "Python" in sentence)
