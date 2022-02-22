shopping_list = ['bread', 'coffee', 'croissants', 'milk', 'sugar']
# don't use keywords like 'list' otherwise could cause issues later on

if ('bread' in shopping_list) and ('butter' not in shopping_list):
    shopping_list.append('butter')

print(shopping_list)