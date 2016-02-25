import time
import random

def main():
  for x in xrange(1,10):
    items = []
    start_time = time.time()
    for y in xrange(1,10):
      items.append(random.randint(1, 10))
    BubbleSort(items)
    print("%s --- %s seconds ---" % (x, time.time() - start_time))

def BubbleSort(a):
  length = len(bad_list) - 1
  sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

if __name__ == "__main__":
    main()
