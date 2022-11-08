string = input()
words = []
N = len(string)
i = 0
if "_" in string:
    words = list(string.split('_'))
elif "-" in string:
    words = list(string.split('-'))
elif string[0].islower():
    i = 0
    tmp = ""
    while i < N and string[i].islower():
        tmp += string[i]
        i += 1
    words = [tmp]
    while i < N:
        if string[i].isupper():
            word = ""
            word += string[i].lower()
            i += 1
            while i < N and string[i].islower():
                word += string[i]
                i += 1
            words.append(word)
else:
    while i < N:
        if string[i].isupper():
            word = ""
            word += string[i].lower()
            i += 1
            while i < N and string[i].islower():
                word += string[i]
                i += 1
            words.append(word)
s3 = "_".join(words)
s4 = "-".join(words)
s1 = ""
for word in words:
    s1 += word[0].upper() + word[1:]
s2 = words[0]
for word in words[1:]:
    s2 += word[0].upper() + word[1:]
print(s1 + ' ' + s2 + ' ' + s3 + ' ' + s4)
