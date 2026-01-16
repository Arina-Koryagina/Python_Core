import string

# st = "hello python"
# for s in st:
#     print(s)
#
# print(st[2])

# l = [1, 2, 3]

# print(st.upper())
# print(st.lower())
# print(st.find("o"))
# print(st.rfind("o"))
# print(st.index("o"))
# print(" + ".join([str(i) for i in l]))
# print(st.zfill(20))
# print(st.ljust(20, '+'))
# print(st.rjust(20, '+'))
# print(st.center(20, '+'))
# print(st.title())
# print(st.capitalize())
# print("5".islower())
# print("30000".endswith("01"))
# print("30000".startswith("30"))
# print("30000".count("0"))
# print("30000".replace("0", "A"))
# print("mama myla ramu".split('a'))
# print("mama myla ramu".strip())

# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
# print(string.printable)

# print(chr(97))
# print(ord('b'))

# print(st[2:6])

# st = "Koryagina Arina"
# name = st.split()
# print(name[1] + " " + name[0])

# print(" ".join(reversed(st.split())))

st = "Bingle bongle dingle dangle, yickedy doo, yickedy da, lippy-tappy-too-ta!"  # (C) 10th Doctor
# words = st.split()
# lenth = []
# for i in range(len(words)):
#     lenth.append((len(words[i])))
# print(words[lenth.index(max(lenth))])

# maxLen = 0
# w = ''
# words = st.split()
# for s in words:
#     if len(s) > maxLen:
#         maxLen = len(s)
#         w = s
# print(w)

# words = st.split()
# n = len(words)
# for j in range(n-1):
#     for i in range(n-1-j):
#         if len(words[i]) > len(words[i+1]):
#             words[i], words[i+1] = words[i+1], words[i]
# print(words)

# text = ('It was a nice day. \nAll the days had been nice. there had been rather '
#         'more than 7 of them so far, and rain had not been invented yet.'
#         'but clouds massing east of Eden suggested that the first thunderstorm '
#         'was on its way, and it was going to be a big one! \nThe angel of the Eastern Gate '
#         'put his wings over his head to shield himself from the first drops.\n'
#         '"I am sorry," he said politely. "What was it you were saying?"\n'
#         '"I said, that one went down like a lead balloon," said the serpent.\n'
#         '"Oh. Yes," said the angel, whose name was Aziraphale.\n'
#         '"I think it was a bit of an overreaction, to be honest," said the serpent.'
#         '"I mean, first offense and everything. I can not see what is so bad about '
#         'knowing the difference between good and evil, anyway."\n'
#         '"It must be bad," reasoned Aziraphale, in the slightly concerned tones '
#         'of one who can not see it either, and is worrying about it, '
#         '"otherwise you would not have been involved."\n')
# print(text)
# rech = text.split(".")
# rech = [r.strip().capitalize()+"." for r in rech]
# text1 = " ".join(rech)
# print(text1)
# digit = 0
# for i in text:
#     digit += i.isdigit()
# print(digit)
# punct = 0
# punct_list = [",", ".", "!", "?", ":", ";"]
# for i in text:
#     if i in punct_list:
#         punct += 1
# print(punct)
# print(text.count("!"))
