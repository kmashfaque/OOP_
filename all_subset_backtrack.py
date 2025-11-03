# def subset(nums):
    
#     result = []
#     subset = []

#     def backTrack(index):
#         result.append(subset.copy())    

#         for i in range(index, len(nums)):
            
#             subset.append(nums[i])
#             backTrack(i+1)
#             subset.pop()
#     backTrack(0)

#     return result

# # -------- TEST --------
# nums = [1, 2, 3]
# print(subset(nums))







