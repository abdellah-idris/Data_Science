import math
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
s = 0
length = len(players)
mean = sum(players) / length
# calculate the variance
for i in players:
    s += (i - mean)*(i - mean)
s= s/length
# check and count the number of player in the range
count = 0
standard_deviation = math.sqrt(s)
for i in players:
    if (i >= (mean - standard_deviation) and i <= (mean+standard_deviation) ):
        count += 1
print(count)