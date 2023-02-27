vowel = ['a', 'e', 'i', 'o', 'u']
Sentence = input("Enter a string: ")
count = 0
for i in Sentence:
    if i in vowel:
        count += 1
print(count)