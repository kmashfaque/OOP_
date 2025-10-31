# from typing import List

# def subsets(nums: List[int]) -> List[List[int]]:
#     n = len(nums)
#     ans, sol = [], []

#     def backtrack(i):
#         if i == n:
#             ans.append(sol[:])
#             return

#         # Don't pick nums[i]
#         backtrack(i + 1)

#         # Pick nums[i]
#         sol.append(nums[i])
#         backtrack(i + 1)
#         sol.pop()

#     backtrack(0)
#     return ans


# # Example usage:
# nums = [1, 2]
# result = subsets(nums)
# print("All subsets:", result)

arr = "abba"
left = 0
right = len(arr) - 1

def palindrome_check(arr, left, right):
    
    if left >= right:return True

    if arr[left] != arr[right]:return False
    
    
    return palindrome_check(arr, left = left + 1, right = right - 1)

print(palindrome_check(arr, left, right))
