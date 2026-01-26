deck:: [[pyspark_oops]]

- These Dunder methods or magic methods
- What is the purpose of `__new__` in Python?
	- #card ^6841f211-2c15-446d-aa13-8246446e16b6
		- Invoked before `__init__` to allocate memory to the object
		- Example:
		  ```python
		  class A:
		     def __new__(cls):
		         print("Creating instance")
		         return super().__new__(cls)
		  a = A()
		  ```
- What is the role of `__init__` in Python?
	- #card ^6841f211-8521-432d-beb5-d90cac9155b5
		- Invoked after `__new__` to initialize the object
		- Example:
		  ```python
		  class A:
		     def __init__(self):
		         print("Initialized")
		  a = A()
		  ```
- When is `__str__` invoked?
	- #card ^6841f211-dc5c-48f1-acbe-61503622d852
		- When `str(obj)` or `print(obj)` is called
		- Example:
		  ```python
		  class A:
		     def __str__(self):
		         return "Hello"
		  print(A())
		  ```
- What does the `__int__` method do?
	- #card ^6841f211-4cee-431e-b454-87be200be5c5
		- Invoked when `int(obj)` is called
		- Example:
		  ```python
		  class A:
		     def __int__(self):
		         return 42
		  print(int(A()))
		  ```
- What does `__len__` return?
	- #card ^6841f211-5d63-458d-8bf0-16769dff0c4b
		- Invoked when `len(obj)` is used
		- Example:
		  ```python
		  class A:
		     def __len__(self):
		         return 5
		  print(len(A()))
		  ```
- What is `__call__` used for?
	- #card ^6841f211-1802-446b-b6a2-730ee3d8737d
		- Invoked when a class object is called as a function: `obj()`
		- Example:
		  ```python
		  class A:
		     def __call__(self):
		         print("Called")
		  a = A()
		  a()
		  ```
- When is `__getitem__` triggered?
	- #card ^6841f211-eee0-4525-b6ab-2571f85155d0
		- Invoked when an object is indexed: `obj[key]`
		- Example:
		  ```python
		  class A:
		     def __getitem__(self, key):
		         return key * 2
		  a = A()
		  print(a[3])  # 6
		  ```
- What is the purpose of `__setitem__`?
	- #card ^6841f211-4fc2-46be-ba05-3cf0ea80f4a7
		- Invoked when an object is indexed and value is set: `obj[key] = value`
		- Example:
		  ```python
		  class A:
		     def __setitem__(self, key, value):
		         print(f"Set {key} = {value}")
		  a = A()
		  a[1] = 100
		  ```
- What does `__delitem__` do?
	- #card ^6841f211-9cfd-4817-a786-00d7766b092e
		- Invoked when an object's index is deleted: `del obj[key]`
		- Example:
		  ```python
		  class A:
		     def __delitem__(self, key):
		         print(f"Deleted key {key}")
		  a = A()
		  del a[0]
		  ```
- When does `__contains__` get called?
	- #card ^6841f211-da2f-471e-a212-548078370d9d
		- Invoked when the `in` operator is used: `item in obj`
		- Example:
		  ```python
		  class A:
		     def __contains__(self, item):
		         return item == "yes"
		  print("yes" in A())
		  ```
- What is the use of `__bool__`?
	- #card ^6841f211-f1e8-4ad4-bcb4-d8b189b84969
		- Invoked when the object is used in a boolean context: `if obj` or `bool(obj)`
		- Example:
		  ```python
		  class A:
		     def __bool__(self):
		         return False
		  print(bool(A()))  # False
		  ```
- What does `__iter__` do?
	- #card ^6841f211-64c8-4ca8-ba29-29b9fb988819
		- Invoked when the object is iterated: `for x in obj`
		- Example:
		  ```python
		  class A:
		     def __iter__(self):
		         return iter([1, 2, 3])
		  for i in A():
		     print(i)
		  ```
- What is `__eq__` used for?
	- #card ^6841f211-5a96-49b3-809f-c7c606330a9e
		- Invoked when `==` is used to compare two objects: `obj1 == obj2`
		- Example:
		  ```python
		  class A:
		     def __eq__(self, other):
		         return True
		  print(A() == A())
		  ```
- When is `__ne__` invoked?
	- #card ^6841f211-dbfd-4c9c-b2be-458565687b79
		- Invoked when `!=` is used to compare two objects: `obj1 != obj2`
		- Example:
		  ```python
		  class A:
		     def __ne__(self, other):
		         return True
		  print(A() != A())
		  ```
- What is the function of `__gt__`?
	- #card ^6841f211-38df-4718-a588-44eb314891c0
		- Invoked when `>` is used to compare two objects: `obj1 > obj2`
		- Example:
		  ```python
		  class A:
		     def __gt__(self, other):
		         return True
		  print(A() > A())
		  ```
- What does `__add__` define?
	- #card ^6841f211-3078-407d-8c88-912b14d7e64f
		- Invoked when two objects are added: `obj1 + obj2`
		- Example:
		  ```python
		  class A:
		     def __add__(self, other):
		         return "Added"
		  print(A() + A())
		  ```
- When is `__mul__` triggered?
	- #card ^6841f211-4baf-41c0-a3f0-191f819a7e78
		- Invoked when two objects are multiplied: `obj1 * obj2`
		- Example:
		  ```python
		  class A:
		     def __mul__(self, other):
		         return "Multiplied"
		  print(A() * A())
		  ```
- What does `__abs__` compute?
	- #card ^6841f211-b60c-4c10-9ecf-5bb03ffc80e4
		- Computes the absolute value of an object: `abs(obj)`
		- Example:
		  ```python
		  class A:
		     def __abs__(self):
		         return 10
		  print(abs(A()))
		  ```
- What does `__neg__` handle?
	- #card ^6841f211-8ea7-4fbe-8e2a-40c8b7ff01bb
		- Invoked when the unary minus operator is used: `-obj`
		- Example:
		  ```python
		  class A:
		     def __neg__(self):
		         return -99
		  print(-A())
		  ```
- What is the use of `__invert__`?
	- #card ^6841f211-9e70-4272-bc86-58ff7a7184e6
		- Invoked when the `~` (bitwise NOT) operator is used: `~obj`
		- Example:
		  ```python
		  class A:
		     def __invert__(self):
		         return "Inverted"
		  print(~A())
		  ```
- What is the purpose of `main()` in Python?
	- #card ^6841f211-f6d9-40b2-893c-eb613ee0c7b1
		- An optional function that contains the entry logic for the script
		- Example:
		  ```python
		  def main():
		     print("Start here")
		  ```
- What does `if __name__ == "__main__"` mean?
	- #card ^6841f211-4b86-4ccf-936f-60da68a7ab79
		- A guard to prevent code from running on import. Used to conditionally call `main()` or other script logic
		- Example:
		  ```python
		  def main():
		     print("Run as script")
		  
		  if __name__ == "__main__":
		     main()
		  ```
- What is a destructor in Python?
	- id:: 6841f23c-a528-499b-a471-857f50e6d66a
	  
	  #card
		- A **destructor** is a special method `__del__()` called when an object is about to be destroyed.
		- In Python, destructors are rarely needed due to the built-in **garbage collector**, unlike in C++ where manual memory management is common.
		- Example:
		  
		  ```
		  class FileHandler:
		  def __init__(self, filename):
		      self.file = open(filename, 'w')
		      print("File opened")
		  
		  def __del__(self):
		      self.file.close()
		      print("File closed")
		  
		  handler = FileHandler("example.txt")
		  del handler  # Triggers __del__(), closes file
		  ```
		  
		  <!--EndFragment-->
