import re

num = list()
doc = open('act.txt')
for line in doc:
	line = line.strip()
	output = re.findall('[0-9]+',line)
	for l in output:
		n = int(l)
		num.append(n)

print sum(num)
