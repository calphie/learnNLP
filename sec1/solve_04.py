input_string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_letter = {1,5,6,7,8,9,15,16,19}
atomic_number={}
for i,v in enumerate(input_string.split()):
    atomic_number[v[:1 if i+1 in one_letter else 2 ]] = i + 1
print(atomic_number)
