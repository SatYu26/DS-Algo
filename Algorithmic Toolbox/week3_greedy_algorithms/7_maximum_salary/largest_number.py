# Python program to find largest
# number from the given values
# function that return largest
# possible number

# https://www.geeksforgeeks.org/arrange-given-numbers-form-biggest-number-set-2/

import sys


def largestNumber(array):

    # extval is a empty list for extended
    # values and ans for calculating answer
    extval, ans = [], ""

    # calculating the length of largest number
    # from given and add 1 for further operation
    l = len(str(max(array))) + 1

    # iterate given values and
    # calculating extended values
    for i in array:
        temp = str(i) * l

        # make tuple of extended value and
        # equivalant original value then
        # append to list
        extval.append((temp[:l:], i))

    # sort extval in descending order
    extval.sort(reverse=True)

    # iterate extended values
    for i in extval:

        # concatinate original value equivalant
        # to extended value into ans variable
        ans += str(i[1])

    if int(ans) == 0:
        return "0"
    return ans


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largestNumber(a))
