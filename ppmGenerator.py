import random

final = ""

type = "P3\n"
x = 500
y = 500
largest = "\n255\n"

final+= type + str(x) + " " + str(y) + largest

red = random.randint(255)
green = random.randint(255)
blue = random.randint(255)

for i in range(x):
	for g in range(y):
		r = red
		g = green
		b = blue
		final += str(r) + ' ' + str(g) + ' ' + str(b) + ' \t'
	final += '\n'
		
f = open("best.ppm",'w')
f.write(final)
f.close()