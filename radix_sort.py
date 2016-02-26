# -*- coding: utf-8 -*-
import time
import random

def main():
  r = 1000000
  print("Running with a r of %s" % (r))
  for x in xrange(1,11):
    items = []
    for y in xrange(1,r + 1):
      items.append(random.randint(1, r + 1))
    start_time = time.time()
    radixsort(items)
    print("%s --- %s seconds ---" % (x, time.time() - start_time))

def radixsort( aList ):
	RADIX = 10
	maxLength = False
	tmp , placement = -1, 1
	while not maxLength:
		maxLength = True
		# declare and initialize buckets
		buckets = [list() for _ in range( RADIX )]
		# split aList between lists
		for i in aList:
			tmp = i / placement
			buckets[tmp % RADIX].append( i )
			if maxLength and tmp > 0:
				maxLength = False
		# empty lists into aList array
		a = 0
		for b in range( RADIX ):
			buck = buckets[b]
			for i in buck:
				aList[a] = i
				a += 1
		# move to next digit
		placement *= RADIX

if __name__ == "__main__":
  main()
