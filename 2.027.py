# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
#
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

string = '''She sells sea shells on the sea shore The shells that she sells are sea shells 
I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''
list = string.lower().split()
print(list)

dict = {}
for word in list:
    dict[word] = dict.get(word, 0) + 1

count = 0
for _ in dict:
    count += 1
print(count)

key = dict.keys() # 2ой способ через длинну
print(len(key))

print(len(set(list))) # 3ий способ через множество