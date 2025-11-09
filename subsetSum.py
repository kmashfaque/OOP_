def subset_sum(nums):
  
    n = len(nums)   
    result = []

    def backtrack(index, current_sum):
       
        if index == n:
            result.append(current_sum)
            return
 
        backtrack(index + 1, current_sum)

        backtrack(index + 1, current_sum + nums[index])

    backtrack(0, 0)

    return result


nums = [1, 2, 3]
print(subset_sum(nums))
        



# def demo_recursion(level):
#     # Base case
#     if level == 3:
#         print(" " * level, f"Reached base case at level {level}")
#         return

#     # Print when we enter this call
#     print(" " * level, f"Entering level {level}")

#     # First recursive call
#     demo_recursion(level + 1)

#     # Second recursive call
#     demo_recursion(level + 1)

#     # Print when we are returning (after both calls done)
#     print(" " * level, f"Returning from level {level}")

# # Start recursion
# demo_recursion(0)


# def two_calls(level):
#     if level == 2:
#         print(" " * level, f"Base case at level {level}")
#         return

#     print(" " * level, f"Entering level {level} (first call)")
#     two_calls(level + 1)

#     print(" " * level, f"Back to level {level} after FIRST call")

#     print(" " * level, f"Entering level {level} (second call)")
#     two_calls(level + 1)

#     print(" " * level, f"Back to level {level} after SECOND call")

# two_calls(0)
