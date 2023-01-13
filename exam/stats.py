import sys
import math

def check(data):
	checked = []
	for elem in data:
		try:
			elem = float(elem)
			checked.append(elem)
		except ValueError:
			sys.stderr.write(f'Illegal entry found, \'{elem}\', will be removed from calculation\n')
	return checked

def mean(data):
	return sum(data)/len(data)
	
def stdv(data):
	ssd = 0
	m = mean(data)
	for num in data:
		ssd += math.pow((num-m),2)
	return math.sqrt(ssd/len(data))
	
def median(data):
	data.sort()
	l = len(data)
	lhalf = int(l/2)
	if l % 2 == 0:
		return (data[lhalf-1] + data[lhalf])/2
	else:
		return data[lhalf]

data = sys.argv[1:]
data = check(data)
print('Valid data: ', end='')
for elem in data: print(elem, end=' ')
print(f'\nmean:', mean(data))
print('stddev:', stdv(data))
print('median:', median(data))

