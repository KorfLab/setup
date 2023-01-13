import os
import sys

seq = sys.argv[1]
out = os.popen(f'python3 aacomp.py {seq}').read().strip()

most = []
most_freq = None
least = []
least_freq = None
for line in out.split('\n'):
	f = line.split('\t')
	aa = f[0]
	freq = int(f[1])
	if freq == 0: continue
	if most_freq == None or freq > most_freq:
		most = [aa]
		most_freq = freq
	elif freq == most_freq:
		most.append(aa)
	if least_freq == None or freq < least_freq:
		least = [aa]
		least_freq = freq
	elif freq == least_freq:
		least.append(aa)
		
print(f'most common amino acid(s): {most}, {most_freq}')
print(f'least common amino acid(s): {least}, {least_freq}')
	
