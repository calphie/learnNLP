input_string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(" ".join(map(lambda s : s if len(s) <= 4 else s[0] + s[1:-1][::-1] + s[-1], input_string.split())))
