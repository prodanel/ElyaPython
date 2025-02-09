def replace_substring(S, S1, S2):
    result = S.replace(S1, S2)
    return result
S = "Привет, мир! Привет, мир!"
S1 = "Привет"
S2 = "Здравствуйте"
new_string = replace_substring(S, S1, S2)
print(new_string)
