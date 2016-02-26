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
    selectionSort(items)
    print("%s --- %s seconds ---" % (x, time.time() - start_time))

def selectionSort(a):
  for fillslot in range(len(a)-1,0,-1):
    positionOfMax=0
    for location in range(1,fillslot+1):
      if a[location]>a[positionOfMax]:
        positionOfMax = location

    temp = a[fillslot]
    a[fillslot] = a[positionOfMax]
    a[positionOfMax] = temp

if __name__ == "__main__":
  main()
