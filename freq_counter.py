import re, sys
from math import log10, floor

def round_within_sig(x, sig=2):
    return round(x, sig-int(floor(log10(x)))-1)

stats_file = open(sys.argv[1], 'r')
out_file   = open(sys.argv[4], 'w')

word = sys.argv[2]
num_sigs = int(sys.argv[3])

name = ""
while (name != word):
    s    = stats_file.readline()
    name = s[:len(word)]

the_stats_list =  re.split('\s+', s)

freq = {}

for i in range(1, len(the_stats_list)):
    try:
        n = round_within_sig(float(the_stats_list[i]), num_sigs)
    
        if not n in freq:
            freq[n] = 0
            
        freq[n] += 1
    except ValueError:
        pass
    
keys = freq.keys()
keys = sorted(keys)

for i in keys:
    out_file.write(str(i) + '\t' + str(freq[i]) + '\n')
