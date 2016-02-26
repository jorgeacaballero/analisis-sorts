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
		mergeSort(items)
		print("%s --- %s seconds ---" % (x, time.time() - start_time))

def mergeSort(a):
	#print("UL = %s" % (a))
	if len(a)>1:
		mid = len(a)//2
		lefthalf = a[:mid]
		righthalf = a[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				a[k]=lefthalf[i]
				i=i+1
			else:
				a[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			a[k]=lefthalf[i]
			i=i+1
			k=k+1

		while j < len(righthalf):
			a[k]=righthalf[j]
			j=j+1
			k=k+1
	#print("OL = %s" % (a))

if __name__ == "__main__":
		main()
