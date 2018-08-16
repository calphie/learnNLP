from string import ascii_lowercase, ascii_uppercase
input_string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
pi = [sum(s in ascii_uppercase or s in ascii_lowercase for s in word)  for word in input_string.split()]
print(pi)
