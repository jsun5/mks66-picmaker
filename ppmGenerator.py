import random

final = ""

type = "P3\n"
x = 500
y = 500
largest = "\n255\n"

final+= type + str(x) + " " + str(y) + largest

red = random.randint(0,255)
green = random.randint(0,255)
blue = random.randint(0,255)

for i in range(x):
	for g in range(y):
		r = red
		g = 25 + (abs(green - i - g))
		#g = 255
		b = blue - abs(i-g)
		final += str(r) + ' ' + str(g) + ' ' + str(b) + ' \t'
	final += '\n'
		
f = open("best.ppm",'w')
f.write(final)
f.close()