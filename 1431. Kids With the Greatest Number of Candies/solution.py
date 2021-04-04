def kidsWithCandies(self, candies, extraCandies):
    return [candy + extraCandies >= max(candies) for candy in candies]