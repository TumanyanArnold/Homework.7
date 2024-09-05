#1
my_dict = {'Арнольд': 1999, 'Виктория': 2000, 'Иван': 1991}
print('Dictionary:', my_dict)
print('Existing value:', my_dict['Виктория'])
print('Not existing value:', my_dict.get(1991))
my_dict['Владислав'] = 1998
print('Deleted value:', my_dict['Иван'])
my_dict.update({'Антон': 1995, 'Инна': 1989})
my_dict.pop('Иван')
print('Modified dictionary:', my_dict)
#2
my_set = {1, 1, 2, 4, 3, 1, 4, True, 42.314, 'Груша', (1, 2, 3)}
print('Set:',set(my_set))
my_set.update([5, 6])
my_set.remove(1)
print('Modified set:', my_set)