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
    insertionSort(items)
    print("%s --- %s seconds ---" % (x, time.time() - start_time))

def insertionSort(a):
  #print("UL = %s" % (a))
  for index in range(1,len(a)):
    currentvalue = a[index]
    position = index
    while position>0 and a[position-1]>currentvalue:
      a[position]=a[position-1]
      position = position-1
    a[position]=currentvalue
  #print("OL = %s" % (a))  

if __name__ == "__main__":
    main()
