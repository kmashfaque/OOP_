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
        

