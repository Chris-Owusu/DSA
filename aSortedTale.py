## Utils

import csv

# This code loads the current book
# shelf data from the csv file
def load_books(filename):
  bookshelf = []
  with open(filename) as file:
      shelf = csv.DictReader(file)
      for book in shelf:
          # add your code here
          
          bookshelf.append(book)
  return bookshelf


### Sort

import random

def bubble_sort(arr, comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      if comparison_function(arr[idx], arr[idx + 1]):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr

def quick_sort(arr, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = arr[pivot_idx]
  arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]
  less_than_pointer = start
  for i in range(start, end):
    if comparison_function(pivot_element, arr[i]):  # Fixed the comparison function
      arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
      less_than_pointer += 1
  arr[end], arr[less_than_pointer] = arr[less_than_pointer], arr[end]
  quick_sort(arr, start, less_than_pointer - 1, comparison_function)
  quick_sort(arr, less_than_pointer + 1, end, comparison_function)


### Script

import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')

# Corrected indentation for the next three lines
for book in bookshelf:
    print(book['title'])

    # Moved the following lines inside the loop to process each book
    book['author_lower'] = book['author'].lower()
    book['title_lower'] = book['title'].lower()

def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

# Fixed the function name in the following line
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for book in sort_1:
    print(book['title'])

def by_author_ascending(book_a, book_b):
    # Simplified the function
    return book_a['author_lower'] > book_b['author_lower']

# Fixed the function name in the following line and sorted bookshelf_v1
bookshelf_v1 = bookshelf.copy()
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
print(sort_2)

bookshelf_v2 = bookshelf.copy()

# Fixed the function name in the following line and sorted bookshelf_v2
sorts.quick_sort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
print(bookshelf_v2)

def by_total_length(book_a, book_b):
    return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])
