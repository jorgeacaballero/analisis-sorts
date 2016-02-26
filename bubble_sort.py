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
		BubbleSort(items)
		print("%s --- %s seconds ---" % (x, time.time() - start_time))

def BubbleSort(a):
	#print("UL = %s" % (a))
	length = len(a) - 1
	sorted = False

	while not sorted:
		sorted = True
		for i in range(length):
			if a[i] > a[i+1]:
				sorted = False
				a[i], a[i+1] = a[i+1], a[i]
	#print("OL = %s" % (a))

if __name__ == "__main__":
		main()
