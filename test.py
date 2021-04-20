songs = ['Flow', 'Holy', 'Case', 'Lovely', 'Kent', 'Nobody', 'Treasure', 'Sinking', 'Groove', 'Peace']
print(songs)
clothes = {'Shirt': 'White', 'Sweater': 'Blue', 'Suit': 'Black', 'Ankara': 'Yellow', 'Lace': 'Green' }
for key in clothes:
    print(f'{key} is {clothes.get(key)}')
set = {'apple', 'orange', 'black'}
print(set)
numbers = ['30','40','90','10','1','0','3']
print(numbers[6])
numbers.pop(1)
#numbers.remove(numbers[1])
new_numbers = sorted(numbers)
print(new_numbers)
#unknown
negative_numbers = ['-1','-4','-5','-2','-5']
numbers.extend(negative_numbers)
print(numbers)