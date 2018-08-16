def char_n_gram(sentence: str, n: int):
    ret = []
    trim_str = "".join(sentence.split())
    for i in range(len(trim_str) - n + 1):
        ret.append(trim_str[i:i + n])
    return ret


p1 = "paraparaparadise"
p2 = "paragraph"
p1_2_gram = set(char_n_gram(p1, 2))
p2_2_gram = set(char_n_gram(p2, 2))
print("union", p1_2_gram | p2_2_gram)
print("intersection", p1_2_gram & p2_2_gram)
print("difference1", p1_2_gram.difference(p2_2_gram))
print("difference2", p2_2_gram.difference(p1_2_gram))
print("se in \"%s\"" % p1, "se" in p1_2_gram)
print("se in \"%s\"" % p2, "se" in p2_2_gram)
