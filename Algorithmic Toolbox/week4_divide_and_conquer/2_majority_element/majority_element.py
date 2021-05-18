# Uses python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_elem = get_majority_element(a, left, (left + right - 1) // 2 + 1)
    right_elem = get_majority_element(a, (left + right - 1) // 2 + 1, right)

    lcount = 0
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1


# def findCandidate(A):
#     maj_index = 0
#     count = 1
#     for i in range(len(A)):
#         if A[maj_index] == A[i]:
#             count += 1
#         else:
#             count -= 1
#         if count == 0:
#             maj_index = i
#             count = 1
#     return A[maj_index]

# # Function to check if the candidate occurs more than n/2 times


# def isMajority(A, cand):
#     count = 0
#     for i in range(len(A)):
#         if A[i] == cand:
#             count += 1
#     if count > len(A)/2:
#         return True
#     else:
#         return False


def get_majority_naive(a):
    n = len(a)
    for i in range(n):
        currentElement = a[i]
        count = 0

        for j in range(n):
            if a[j] == currentElement:
                count += 1
        if count > n/2:
            return a[i]
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
