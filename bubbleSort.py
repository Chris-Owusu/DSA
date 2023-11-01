####  Bubble Sort: Swap
nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp
  
# define bubble_sort():
def bubble_sort(arr):
  for elem in arr:
    for num in range(len(nums) - 1):
      if arr[num] > arr[num + 1]:
        swap(arr, num, num + 1)

##### test statements

print("Pre-Sort: {0}".format(nums))      
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))