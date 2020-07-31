# Use this playground to experiment with list methods, using Test Run
my_list = [1,2,3, 8,4,5,'gold','blip']

#add entries
my_list.append(1)
print(my_list)

#remove first element and print removed element
print(my_list.pop())

#find position of an item
print(my_list.index('gold'))

#removing specific value
my_list.remove('blip')
print(my_list)

#sort values
another_list = [2,4,7,8,7,2,1,12]
another_list.sort()
print(another_list)