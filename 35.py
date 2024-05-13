nums = list(map(int, input("Enter space-separated numbers to sort: ").split()))
n = len(nums)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Sorted array:", nums)