def insertionSort(A):
  for i in range(1, len(A)):
    insert(A, A[i], i)
  return A

def insert(A, k, i):
  for j in range(i-1, -1, -1):
    if A[j] < k:
      A[j+1] = k
      return
    A[j+1] = A[j]
  A[0] = k

def selectionSort(A):
  for i in range(len(A)):
    imin = findmin(A, i)
    swap(A, i, imin)
  return A

def findmin(A, i):
  imin = i
  for j in range(i+1, len(A)):
    if A[j] < A[imin]:
      imin = j
  return imin

def swap(A, j, k):
  tmp = A[j]
  A[j] = A[k]
  A[k] = tmp

def bubbleSearch(A, k):
  hi = len(A)-1
  lo = 0
  while hi >= lo:
    mid = (hi + lo) // 2
    if A[mid] == k:
      return mid
    elif A[mid] > k:
      hi = mid - 1
    elif A[mid] < k:
      lo = mid + 1
  return -1

def searchRec(A, k):
  return searchRecAux(A, k, 0)

def searchRecAux(A, k, i):
  if i == len(A):
    return -1
  if A[i] == k:
    return i
  return searchRecAux(A, k, i+1)


def searchRec2(A, k):
  if A == []:
    return -1
  if A[0] == k:
    return 0
  recS = searchRec2(A[1:], k)
  if recS == -1:
    return -1
  return recS + 1

def subArray(A, lo, hi):
  return [A[i] for i in range(lo, hi)]

def searchLast(A, k):
  return searchLastAux(A, k, len(A)-1)

def searchLastAux(A, k, hi):
  if hi < 0:
    return -1
  if A[hi] == k:
    return hi
  return searchLastAux(A, k, hi-1)

def findMax(A):
  return findMaxAux(A, 0, 0)

def findMaxAux(A, max_v, i):
  if A == []:
    return -1
  if i == len(A):
    return max_v
  if A[i] > max_v:
    max_v = A[i]
  return findMaxAux(A, max_v, i+1)




# print(insertionSort([5, 6, 4, 7, 14, 3, 8, 2, 9, 1]))
# print(searchRec2([2, 4, 6, 8, 10], 8))
# print(fact(7, 2))
# A = [1, 2, 3, 4, 5, 6]
# print(A[:2])
# print(A[2:])
print(findMax([10, 2, 8, 6, 2, 11, 4]))

