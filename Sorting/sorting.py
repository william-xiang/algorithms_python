# insertion sort
def insertion(nums):
    for i in range(len(nums)):
        j = i - 1
        x = nums[i]
        while j >= 0 and x < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        
        # j + 1 is the final index
        nums[j + 1] = x
        