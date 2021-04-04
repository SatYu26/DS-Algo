Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that they can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

Example
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]

Explanation: Kid 1 has 2 candies, and if they receive all extra candies (3) they will have 5 candies – the greatest number of candies among the kids.

Kid 2 has 3 candies, and if they receive at least 2 extra candies then they will have the greatest number of candies among the kids.

Kid 3 has 5 candies, and this is already the greatest number of candies among the kids.

Kid 4 has 1 candy, and even if they receive all extra candies they will only have 4 candies.

Kid 5 has 3 candies, and if they receive at least 2 extra candies then they will have the greatest number of candies among the kids.