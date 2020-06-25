"""
Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two
 different items in the array that, when added together, give the target value. The indices of these items should then be returned in an array like so: [index1, index2].

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/
Available here: https://www.codewars.com/kata/52c31f8e6605bcc646000082
"""


# solution

def two_sum(numbers, target):
    result = []
    for n in numbers:
        if n < target:
            diff = target - n
            if diff in numbers:
                result.append(numbers.index(n))
                if numbers.index(diff) in result:
                    result.append(len(numbers) - numbers[::-1].index(diff) - 1)
                else:
                    result.append(numbers.index(diff))
                return result
            else:
                continue
        return result


# Examples
print(two_sum([1,2,3], 4))
print(two_sum([1234,5678,9012], 14690))
print(two_sum([2,2,3], 4))