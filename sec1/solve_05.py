input_string = "I am an NLPer"
def word_n_gram(sentence:str, n:int):
    ret = []
    words = sentence.split()
    for i in range(len(words) - n + 1 ):
        ret.append(tuple(words[i:i+n]))
    return ret
def char_n_gram(sentence:str, n:int):
    ret = []
    trim_str = "".join(sentence.split())
    for i in range(len(trim_str) - n + 1):
        ret.append(trim_str[i:i+n])
    return ret
if __name__ == "__main__":
    print(word_n_gram(input_string, 2))
    print(char_n_gram(input_string, 2))

