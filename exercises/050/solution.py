pairs = 0

for a in range(0, 1001):
    if a % 3 == 0 or a % 5 == 0:
        pairs = pairs + a
 
print(pairs)
