my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
# This doesn't work:
# friend_foods = my_foods
print(friend_foods)
print(my_foods)