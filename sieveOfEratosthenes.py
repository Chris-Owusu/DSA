def sieve_of_eratosthenes(limit):
  # Create a boolean list to represent whether numbers are prime or not.
  is_prime = [True] * (limit + 1)
  is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

  # Start with the first prime number, which is 2.
  current_num = 2

  while current_num * current_num <= limit:
    # If the current number is marked as prime, mark its multiples as non-prime.
    if is_prime[current_num]:
      for multiple in range(current_num * current_num, limit + 1, current_num):
        is_prime[multiple] = False
    current_num += 1

  # Collect the prime numbers into the 'true_indices' list.
  true_indices = [index for index, is_prime_number in enumerate(is_prime) if is_prime_number]
  
  return true_indices

primes = sieve_of_eratosthenes(13)
print(primes)  # should return [2, 3, 5, 7, 11, 13]