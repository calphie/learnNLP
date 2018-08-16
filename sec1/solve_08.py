input_string = "All your bases belong to us."
def cifer(sentence:str):
    def transform(s:str):
        if s.islower() :
            return chr(219-ord(s))
        else :
            return s
    return "".join(map(transform, sentence))

redecode = lambda x : cifer(cifer(x))
print(cifer(input_string), redecode(input_string))
