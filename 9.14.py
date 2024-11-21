from random import choice

lott = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']

n1 = choice(lott)
n2 = choice(lott)
n3 = choice(lott)
n4 = choice(lott)

print(f"Any ticket matching these no or letter wins : {n1}{n2}{n3}{n4}")

