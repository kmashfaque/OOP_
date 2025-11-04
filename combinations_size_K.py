def combination_size(nums, k):
    
    result = []
    new_arr = []
    def combination(index):
        
        if len(new_arr) == k:
            return result.append(new_arr.copy())

        for i in range (index,len(nums)):

            new_arr.append(nums[i])
            combination(i+1)
            new_arr.pop()

    combination(0)
    return result

nums = [1,2,3]
k = 2

print(combination_size(nums, k))