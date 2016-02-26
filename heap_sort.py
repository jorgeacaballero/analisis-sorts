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
    HeapSort(items)
    print("%s --- %s seconds ---" % (x, time.time() - start_time))

def HeapSort(a):
  #print("UL = %s" % (a))
  length = len( a ) - 1
  leastParent = length / 2
  for i in range ( leastParent, -1, -1 ):
    moveDown( a, i, length )
 
  for i in range ( length, 0, -1 ):
    if a[0] > a[i]:
      swap( a, 0, i )
      moveDown( a, 0, i - 1 )
  #print("UL = %s" % (a))
 
def moveDown( a, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    if ( largest < last ) and ( a[largest] < a[largest + 1] ):
      largest += 1
    if a[largest] > a[first]:
      swap( a, largest, first )
      first = largest;
      largest = 2 * first + 1
    else:
      return
 
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

if __name__ == "__main__":
    main()
