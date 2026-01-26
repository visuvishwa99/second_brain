deck:: [[python]]

- First element of list
	- #card ^6812ecc8-fe06-4738-aba2-23263b280000
		- ```python
		  lst[0]
		  ```
- Last element of list
	- #card
	  id:: 6812ecc8-ca34-485d-a0c7-a4f98b1ad0f8
		- ```python
		  lst[-1]
		  ```
- Count items in a list
	- #card ^6812ecc8-a5c8-4660-8f39-6a88e466695a
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-01-23T07:00:00.000Z
	  card-last-reviewed:: 2026-01-22T19:43:17.051Z
	  card-last-score:: 1
		- ```python
		  len(lst)
		  ```
- Make a shallow copy of a list
	- #card
	  id:: 6812ecc8-e393-43df-857f-ee2a0e477761
		- ```python
		  """
		  A shallow copy creates a new, independent list object, but the elements within it are still references to the 
		  same objects as the original list.
		  
		  This is different from a deep copy, which creates a new list and also recursively creates new copies of 
		  all the objects within the list.
		  """
		  lst[:]
		  ```
		  or
		- ```python
		  list(lst)
		  ```
		  or
		- ```python
		  lst.copy()
		  ```
- Make a deep copy of a list
	- #card ^6812ecc8-8d63-44c0-81bf-3b5dd27254fc
		- ```python
		  import copy
		  copy.deepcopy(lst)
		  
		  
		  
		  MN=>>
		  SALT for Shallow:
		  Shallow Assigns Links To inner objects (shared references)
		  
		  DEED for Deep:
		  Deep Entirely Everything Duplicated (totally new copies)
		  ```
- Convert string to list of characters ex: Geeks for -> [g,e,e,......]
	- #card
	  id:: 6812ecc8-709f-445d-bc44-9f5916f1720f
		- ```python
		  list("Geeks for")
		  ```
- Access character at index 3 for a given list
	- #card ^6812ecc8-78a7-4532-9af0-c60327071c4b
		- ```python
		  string[3]
		  ```
- Remove character at index 3 for a given string not list
	- #card
	  id:: 6812ecc8-fbc7-4d3a-8f54-59476349bbe2
		- ```python
		  string[:3] + string[4:]
		  
		  for list you can use pop(index)
		  ```
- Add character 'c' at index 3 for a given list
	- #card ^6812ecc8-ada0-4f6a-b44f-e7abe9be6d70
		- ```python
		  string[:3] + 'c' + string[3:]
		  ```
- Check if string is palindrome
	- #card
	  id:: 6812ecc8-cdd9-42c9-a29e-db1f0ce6bbf4
		- ```python
		  s == s[::-1]
		  ```
- Check if two strings are anagrams
	- #card ^6812ecc8-1eab-4cff-ae94-27ef163bef1a
		- ```python
		  from collections import Counter
		  Counter(s) == Counter(t)
		  ```
- Add element to end of list
	- #card
	  id:: 6812ecc8-5582-4ffc-b581-7cb8d1dfaabb
		- ```python
		  lst.append(value)
		  ```
- Add multiple elements to end of list
	- #card ^6812ecc8-833c-4b55-8054-ba3ebdbcbf3e
		- ```python
		  lst.extend(iterable)
		  ```
- Insert element at specific position of a list
	- #card
	  id:: 6812ecc8-8d4e-46ba-b3b5-1543c540b826
		- ```python
		  lst.insert(index, value)
		  ```
- Remove first occurrence of value of a list not string
	- #card ^6812ecc8-3de0-4313-bcc3-67230ec8e333
		- id:: 6812edc6-4f12-4db6-86d1-0422c6f64f9b
		  ```python
		  
		  | Method        | Removes                   | Returns         | Notes                                |
		  | ------------- | ------------------------- | --------------- | ------------------------------------ |
		  | `remove(val)` | First occurrence of value | None            | Raises error if value not found      |
		  | `pop(idx)`    | Element at index          | Element removed | Default `pop()` removes last element |
		  
		  
		  lst.remove(value)
		  fruits = ["apple", "banana", "cherry", "apple", "banana"]
		  
		  # Remove the first occurrence of "banana"
		  fruits.remove("banana")
		  
		  print(fruits)  # Output: ['apple', 'cherry', 'apple', 'banana']
		  
		  fruits = ["apple", "banana", "cherry", "apple", "banana"]
		  ---------------------------------------------------------------------------
		  # Remove element at index 1 (second element)
		  removed_fruit = fruits.pop(1)
		  
		  print(fruits)        # Output: ['apple', 'cherry', 'apple', 'banana']
		  print(removed_fruit) # Output: banana
		  
		  Note : Default: pop() removes the last element.
		  ```
- Remove and return element at index
	- #card ^6812ecc8-b82d-4459-8cf1-813186e520a6
		- ```python
		  lst.pop(index)
		  ```
- Sort list in-place
	- #card
	  id:: 6812ecc8-f44f-4f0c-ac52-72a777e7d5b2
		- ```python
		  lst.sort()
		  
		  Note :
		  lst.sort(reverse=True)          # descending
		  lst.sort(key=lambda x: -x )      # custom
		  “In-place” means that the original object is modified directly, rather than creating a new object.
		  ```
- Reverse list in-place
	- #card ^6812ecc8-f62f-41db-a58e-7a02c773a168
		- ```python
		  lst.reverse()
		  &lst[::-1]
		  ```
- Get a new sorted list
	- #card
	  id:: 6812ecc8-47cb-455a-bbdc-9d1687ea8122
		- ```python
		  sorted(lst)
		  
		  """
		  `sorted()` and `list.sort()` are both used to sort iterables in Python, but they differ in how they operate on data, their return values, and their space complexity.
		  
		  Here is a summary of the key differences:
		  
		  | Feature | `sorted()` | `list.sort()` |
		  | :--- | :--- | :--- |
		  | **Modification** | Returns a **new, sorted list** | Sorts the list **in-place** |
		  | **Return Value** | The new sorted list | `None` |
		  | **Applicability** | Works on any iterable (list, tuple, string, etc.) | Works only on lists |
		  | **Time Complexity** | **$O(n log n)$** | **$O(n log n)$** |
		  | **Space Complexity** | **$O(n)$** | **$O(1)$** |
		  
		  """
		  
		  ```
- Difference between sort() and sorted()
	- #card ^6812ecc8-ab0f-443f-9f9c-498c06418fcb
		- sort() is a list method that modifies the list in-place and returns None
		- sorted() is a built-in function that returns a new sorted list
		- sort() works only on lists, sorted() works on any iterable
- Create a dictionary
	- #card ^6812ecc8-b1c9-4c72-932d-7b27a41dbc30
		- ```python
		  d = {'key1': 'value1', 'key2': 'value2'} # Regular Dictionary
		  
		  
		  d = dict(key1='value1', key2='value2') # using dict() constructor
		  
		  📌 Why use OrderedDict in Python
		  
		  Even though regular dictionaries preserve insertion order (Python 3.7+), OrderedDict provides extra methods that regular dicts don’t have:
		  
		  Method	Description
		  move_to_end(key, last=True/False)	Move a key to the end (last=True) or beginning (last=False) of the dictionary
		  popitem(last=True/False)	Remove and return the last (last=True) or first (last=False) item
		  
		  from collections import OrderedDict
		  
		  od = OrderedDict() # but OrderedDict adds useful ordering methods for advanced use cases
		  od['a'] = 1
		  od['b'] = 2
		  od['c'] = 3
		  
		  od.move_to_end('a')           # 'a' moved to the end
		  print(od)                     # OrderedDict([('b', 2), ('c', 3), ('a', 1)])
		  
		  od.popitem(last=False)        # removes first item ('b', 2)
		  print(od)                     # OrderedDict([('c', 3), ('a', 1)])
		  
		  
		  ```
- Access dictionary value
	- #card
	  id:: 6812ecc8-9c13-4df2-a966-a641aaab8caf
		- ```python
		  d['key']
		  ```
		  or
		- ```python
		  d.get('key', default_value)  # Often preferred in production code
		  ```
- Get all keys of dict
	- #card
	  id:: 6812ecc8-845d-419f-b3fd-b6ad44d0606d
		- ```python
		  d.keys()
		  ```
- Get all values of dict
	- #card ^6812ecc8-5ddf-451c-9037-6aaaffaae5a2
		- ```python
		  d.values()
		  ```
- Get all key-value pairs
	- #card
	  id:: 6812ecc8-2b16-4e37-8798-5319efa7c9f8
		- ```python
		  d.items()
		  ```
- Create a set
	- #card ^6812ecc8-f03e-4766-a4ca-057c5695bacf
		- ```python
		  s = {1, 2, 3}
		  ```
		  or
		- ```python
		  s = set([1, 2, 3])
		  ```
- Add to a set
	- #card ^6812ecc8-d5a7-425d-9acc-4a4469e0ae45
		- ```python
		  add() → adds a single element & update() → adds multiple elements
		  
		  Note : set.add() → only adds to the set, no position control.If you want position control you need list not set 
		  
		  my_set = {1, 2, 3}
		  my_set.add(4)
		  my_set.add(0)
		  print(my_set)
		  {0, 1, 2, 3, 4}  # Notice how 0 may appear at the “start”!
		  #set.add() does not guarantee the position; sets are fundamentally unordered.
		  
		  
		  my_set = {1, 2, 3}
		  my_set.update([4, 5, 6])
		  print(my_set)  # {1, 2, 3, 4, 5, 6}
		  ```
- Remove from a set
	- #card
	  id:: 6812ecc8-66d5-46cd-8868-df4b7f4ef701
		- ```python
		  s.remove(4)
		  active_user_ids = {1001, 1002, 1003, 1004}
		  # When a user is deactivated
		  active_user_ids.remove(1003)
		  ```
		  or
		- ```python
		  s.discard(4)
		  # Safe removal of potential bad values without disrupting the pipeline
		  valid_product_ids = {"A123", "B456", "C789"}
		  for product_id in ["B456", "D012", "E345"]:
		  valid_product_ids.discard(product_id)  # Removes only if exists
		  Key Difference
		  
		  Error safety: discard() is the safer option as it never raises an exception
		  Verification: remove() can be used when you want to confirm an element was present
		  
		  ```
- Join list of strings with separator
	- #card
	  id:: 6812ecc8-8e3a-4fe6-bf94-ab531fb7dc21
		- ```python
		  '-'.join(list_of_strings)
		  list_of_strings = ["data", "engineering", "concepts"]
		  result = '-'.join(list_of_strings)
		  # result would be "data-engineering-concepts"
		  ```
- Split string on whitespace
	- #card ^6812ecc8-87d1-46bb-ba55-a3f67aa3497a
		- ```python
		  s.split()
		  ```
- Split string on specific character
	- #card
	  id:: 6812ecc8-bc94-4984-b36a-a46722a88286
		- ```python
		  s.split(',')
		  ```
- Convert to uppercase
	- #card ^6812ecc8-1fe8-475c-bff9-02d32e88641b
		- ```python
		  s.upper()
		  ```
- Convert to lowercase
	- #card
	  id:: 6812ecc8-1aad-45e4-8f97-2f7646ebce02
		- ```python
		  s.lower()
		  ```
- Remove whitespace from ends
	- #card ^6812ecc8-dac3-43c5-9bbf-203d46b27beb
		- ```python
		  s.strip()
		  ```
- Check if string contains only alphanumeric characters
	- #card
	  id:: 6812ecc8-277d-4284-b9fd-ef048397c29a
		- ```python
		  s.isalnum()
		  ```
- Get ASCII value of character
	- #card ^6812ecc8-9dac-453a-a49b-f929b6536622
		- ```python
		  ord('a')
		  ```
- Convert ASCII value to character
	- #card
	  id:: 6812ecc8-0930-41b1-905f-95fc3ab9267f
		- ```python
		  chr(97)
		  ```
- Iterate with index and value
	- #card ^6812ecc8-9af9-4500-826e-9bbda6562efd
		- ```python
		  for idx, val in enumerate(lst):
		   # Your code here
		  ```
- Create a range of numbers
	- #card
	  id:: 6812ecc8-d9ed-4244-a0ff-0807273f96ce
		- ```python
		  range(start, stop, step)
		  ```
- Loop over dictionary keys
	- #card ^6812ecc8-cf98-4ee0-a8d5-ebbfc6028827
		- ```python
		  for key in d:
		   # Your code here
		  ```
- Loop over dictionary values
	- #card
	  id:: 6812ecc8-95c5-44fe-91be-cea30ca9d752
		- ```python
		  for value in d.values():
		   # Your code here
		  ```
- Loop over key-value pairs
	- #card ^6812ecc8-00e7-4b15-8aa1-79443ac24b64
		- ```python
		  for key, value in d.items():
		   # Your code here
		  ```
- Create an anonymous function
	- #card
	  id:: 6812ecc8-a1cc-4dbe-a049-8cfeb28d6ff3
		- ```python
		  lambda arguments: expression
		  ```
- Name a function to each item in iterable
	- #card ^6812ecc8-42be-46d3-95cf-d34c8311c4af
		- ```python
		  map(function, iterable)
		  # map() function takes two arguments: a function and an iterable. It returns a map object 
		  
		  example:
		    numbers = [1, 2, 3, 4]
		    doubled_numbers = map(lambda x: x * 2, numbers)
		  
		    # Convert the map object to a list to see the result
		    print(list(doubled_numbers))
		  ```
- Filter items based on function
	- #card
	  id:: 6812ecc8-5f6f-4b60-9c21-8bfce7cb65f1
		- ```python
		  filter(function, sequence)
		  ```
- Name a function cumulatively to items
	- #card ^6812ecc8-6eba-48df-95ea-51fbc682618a
		- ```python
		  from functools import reduce
		  reduce(function, sequence)
		  
		  from functools import reduce
		  
		  # Example with a list of card values
		  card_values = [10, 5, 2, 8, 3]  
		  
		  # Sum all values
		  total_value = reduce(lambda x, y: x + y, card_values)
		  # Equivalent to: ((((10 + 5) + 2) + 8) + 3)
		  
		  print(total_value)  # Output: 28
		  
		  Note : 
		    x = accumulated value so far
		    y = current element from the sequence
		    reduce() continues until only one value remains and it automatically traverses the list from left to right.
		  ```
- Comprehension to create a new list (syntax)
	- #card
	  id:: 6812ecc8-8336-4bfc-bf3c-a7083dc0d2d8
		- ```python
		  [expression for item in iterable if condition]
		  expression → what each element in the new list will be
		  item → variable for each element in the original iterable
		  iterable → any iterable (list, range, etc.)
		  if condition → optional filter
		  
		  
		  numbers = [1, 2, 3, 4, 5]
		  squares = [x**2 for x in numbers]
		  print(squares)  # [1, 4, 9, 16, 25]
		  
		  ```
- Rotate list right / left  by n
	- #card ^6812ecc8-702f-48e6-84ed-ed7eac2a5a0c
		- ```python
		  
		  Visual memory aid:
		  
		  RIGHT: -n comes first → lst[-n:] + lst[:-n]
		  LEFT: n comes first → lst[n:] + lst[:n]
		  ```
- Define positive infinity
	- #card
	  id:: 6812ecc8-9fad-4e4e-8ad0-5beec5977843
		- ```python
		  float('inf')
		  ```
- Define negative infinity
	- #card ^6812ecc8-c5b1-41ae-b25e-608f62d840bf
		- ```python
		  float('-inf')
		  ```
- Round a number (just roundup)
	- #card
	  id:: 6812ecc8-a3d0-4d35-ae17-9e19424d1635
		- ```python
		  import math
		  # Floor examples (round down)
		  math.floor(3.2)  # Returns 3
		  math.floor(3.9)  # Returns 3
		  math.floor(3.0)  # Returns 3
		  math.floor(-3.2)  # Returns -4 (rounds down to more negative)
		  ```
- Round a number up
	- #card ^6812ecc8-7dae-4233-96b5-65f6a097885e
		- ```python
		  # Ceil examples (round up)
		  math.ceil(3.2)  # Returns 4
		  math.ceil(3.9)  # Returns 4
		  math.ceil(3.0)  # Returns 3
		  math.ceil(-3.2)  # Returns -3 (rounds up to less negative)
		  ```
- Create a default dictionary
	- #card
	  id:: 6812ecc8-7155-42d6-a576-855066414494
		- ```python
		  from collections import defaultdict
		  counts = defaultdict(int)
		  
		  Example => 
		  from collections import defaultdict
		  counts = defaultdict(int)
		  words = ["apple", "banana", "apple", "orange", "banana", "apple"]
		  
		  for word in words:
		      counts[word] += 1
		  
		  print(dict(counts))
		  
		  ```
- Check if substring exists
	- #card ^6812ecc8-b93b-4622-9647-dc7655384834
		- ```python
		  if substring in string:
		   # Your code here
		  
		  text = "Hello, world!"
		  if "world" in text:
		      print("Substring found!") #Substring found!
		  
		  
		  ```
- Fix indentation in code editor
	- #card
	  id:: 6812ecc8-88bb-4ea6-a2cb-5ed3681eaf18
		- ```
		  python
		  
		  CTRL+[  # Outdent
		  CTRL+]  # Indent
		  ```
- Handle an exception
	- #card ^6812ecc8-af81-4b08-9713-1b0926ebf0a2
		- ```python
		  try:
		   # code that might raise exception
		  except ExceptionType as e:
		   # handle exception
		  ```
- Handle multiple exceptions
	- #card
	  id:: 6812ecc8-23db-41b1-a57b-7a7e1025c7c9
		- ```python
		  try:
		   # code
		  except (TypeError, ValueError) as e:
		   # handle multiple types
		  ```
- Raise an exception
	- #card ^6812ecc8-cdb8-42a3-83e5-1f37cdc05c73
		- ```python
		  raise ExceptionClass("message")
		  ```
- Filter vs Map vs FlatMap vs Reduce
	- #card
	  id:: 681680d9-9da9-4bee-8c7e-6730f628a7f0
		- ```python
		  # Keep only even numbers
		  numbers = [1, 2, 3, 4, 5]
		  even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
		  
		  # Square each number
		  numbers = [1, 2, 3, 4, 5]
		  squared = list(map(lambda x: x * x, numbers))  # [1, 4, 9, 16, 25]
		  
		  # Python doesn't have built-in flatMap, but we can implement it
		  def flat_map(func, collection):
		  return [item for sublist in map(func, collection) for item in sublist]
		  
		  # Generate pairs for each number
		  numbers = [1, 2, 3]
		  pairs = flat_map(lambda x: [x, x], numbers)  # [1, 1, 2, 2, 3, 3]
		  
		  from functools import reduce
		  
		  # Sum all numbers
		  numbers = [1, 2, 3, 4, 5]
		  total = reduce(lambda acc, x: acc + x, numbers, 0)  # 15
		  
		  I'd be happy to present the key differences between Filter, Map, FlatMap, and Reduce in table format:
		  
		  | Operation | Purpose | Input/Output Size | Function Type | Result Type | Common Use Cases |
		  |-----------|---------|-------------------|---------------|-------------|------------------|
		  | **Filter** | Selectively include elements | Same or smaller | Predicate function (returns boolean) | Collection | Remove unwanted data, validation |
		  | **Map** | Transform each element | Same size (1:1) | Transformation function | Collection | Data conversion, formatting |
		  | **FlatMap** | Transform and flatten | Can be larger or smaller | 1-to-many transformation | Collection | Handle nested structures, expand data |
		  | **Reduce** | Combine all elements | Many to one | Binary operation with accumulator | Single value | Aggregation, summarization |
		  
		  This table highlights the fundamental differences in how these operations process data collections and their typical applications in data engineering pipelines.
		  ```
-
