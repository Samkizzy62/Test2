#1
def percentage(total, number):
    return(total * number / 100)
print(percentage(300, 10))

#2
list = ("aa", "bb", "cc", "dd", 'ee')
print(list[4])

#3
item = {'aa': 10, 'bb': 20, 'cc': 30, 'dd': 40, 'ee': 50}
def show_item(i):
    return item.get(i)
result = show_item('bb')
print(result)

#4
list_1 = (1, 2, 3, 4, 5)
list_2 = (10, 20, 30, 40, 50)
def added_list(list_1, list_2):
    return (list_1 + list_2)
print(added_list(list_1, list_2))