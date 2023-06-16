array = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
word = input("введите текст стихотворения:" )
word = word.split()
print(word)
array_new = []
count = 0
for i in word: 
    for k in i:
        if k in array:
            count+=1
    array_new.append(count)        
print(array_new)
if len(set(array_new)) > 1:
    print("Пам парам")
else:
    print("Парам пам-пам")