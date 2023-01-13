import random
import sys

people = int(sys.argv[1])
trials = int(sys.argv[2])

success = 0
for _ in range(trials):
	bdays = []
	for _ in range(people):
		bday = random.randint(1,365)
		if bday not in bdays: bdays.append(bday)
		else:
			success+=1
			break
print(f'{(100*success/trials):.2f}% of the time 2 people share the same birthday in {people} people')
