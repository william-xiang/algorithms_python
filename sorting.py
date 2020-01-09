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

# bubble sort
def bubble(nums):
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

# max heapify
def max_heapify(nums, len, i):
    left = 2 * i + 1
    right = 2 * i + 2
    max = i
    if left < len and nums[max] < nums[left]:
        max = left
    if right < len and nums[max] < nums[right]:
        max = right
    if max != i:
        nums[i], nums[max] = nums[max], nums[i]
        max_heapify(nums, len, max)

# constuct a max heap
def constuct_heap(nums):
    heapSize = len(nums)
    for i in range(heapSize / 2 - 1, -1, -1):
        max_heapify(nums, heapSize, i)

# heap sort
def heap_sort(nums):
    constuct_heap(nums)
    for i in range(len(nums) - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        max_heapify(nums, i, 0)
        