nums = list(map(float, input("Enter space-separated numbers: ").split()))
average = sum(nums) / len(nums) if nums else 0
print("Average:", average)
