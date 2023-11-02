#### Fibonacci with Memoization

memo = {}

def fibonacci(num):
  # Check if the result is already in the memo dictionary
  if num in memo:
    return memo[num]
  
  # Base cases
  if num <= 1:
    return num

  # Recursive case
  memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
  return memo[num]

# Test your code with calls here:
print(fibonacci(20))
print(fibonacci(200))