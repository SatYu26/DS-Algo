# Consider an array of numbers. Our task is to add 1 to the numbers at odd indices and to add 2 to the number at even indices.

# Now we'll solve the above problem using both a for-loop and list comprehension.


# using fro loop
def addOneAndTwo(nums, n):
    for i in range(n):
        if i % 2 == 1:
            nums[i] += 1
        else:
            nums[i] += 2
    return nums


# using List Comprehension
def addOneAndTwoL(nums, n):
    return [nums[i] + 1 if i % 2 == 1 else nums[i] + 2 for i in range(n)]
