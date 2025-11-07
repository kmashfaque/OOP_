# def permutation(arr):
#     result = []
    

#     def backtack(index):
#           if index == len(arr):
#                result.append(arr.copy())
#                return 
          
#           for i in range(index, len(arr)):
#                 arr[index], arr[i] = arr[i], arr[index]
#                 backtack(index + 1)
#                 arr[index], arr[i] = arr[i], arr[index]
                
#     backtack(0)
    
#     return result

# arr = [1,2,3] 
# print(permutation(arr))


def permutation(arr):
    result = []

    def backtrack(index):
        # print(f"ENTER index={index}, arr={arr}")

        if index == len(arr):
            # print(">>> BASE CASE, append", arr)
            result.append(arr.copy())
            return

        for i in range(index, len(arr)):
            # print(f"SWAP index={index} and i={i} -> {arr[index]} <-> {arr[i]}")
            arr[index], arr[i] = arr[i], arr[index]

            backtrack(index + 1)

            # print(f"UNDO SWAP index={index} and i={i} -> {arr[index]} <-> {arr[i]}")
            arr[index], arr[i] = arr[i], arr[index]

        # print(f"EXIT index={index}, arr={arr}")

    backtrack(0)
    return result

arr = [1,2,3] 
print(permutation(arr))