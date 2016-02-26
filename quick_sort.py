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
    quickSort(items)
    print("%s --- %s seconds ---" % (x, time.time() - start_time))

def quickSort(a):
  quickSortHelper(a,0,len(a)-1)

def quickSortHelper(a,first,last):
  if first<last:
    splitpoint = partition(a,first,last)
    quickSortHelper(a,first,splitpoint-1)
    quickSortHelper(a,splitpoint+1,last)


def partition(a,first,last):
  pivotvalue = a[first]

  leftmark = first+1
  rightmark = last

  done = False
  while not done:

    while leftmark <= rightmark and a[leftmark] <= pivotvalue:
      leftmark = leftmark + 1

    while a[rightmark] >= pivotvalue and rightmark >= leftmark:
      rightmark = rightmark -1

    if rightmark < leftmark:
      done = True
    else:
      temp = a[leftmark]
      a[leftmark] = a[rightmark]
      a[rightmark] = temp

  temp = a[first]
  a[first] = a[rightmark]
  a[rightmark] = temp


  return rightmark

if __name__ == "__main__":
    main()
