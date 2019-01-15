ans = 0

with open(transaction.log) as f:
    lines = f.readlines()

while lines:
	line = raw_input("> ").split()
	if not line:
		break;
		
	val = int(line[1])
	if line[0] == 'D':
		net += val
	elif line[0] == 'W':
		net -= val

print ans
