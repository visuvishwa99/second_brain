deck:: [[pyspark_oops]]

- These Dunder methods or magic methods
- What is the purpose of `__new__` in Python?
	-
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
	-
		- Invoked after `__new__` to initialize the object
		- Example:
		 ```python
		 class A:
		 def __init__(self):
		 print("Initialized")
		 a = A()
		 ```
- When is `__str__` invoked?
	-
		- When `str(obj)` or `print(obj)` is called
		- Example:
		 ```python
		 class A:
		 def __str__(self):
		 return "Hello"
		 print(A())
		 ```
- What does the `__int__` method do?
	-
		- Invoked when `int(obj)` is called
		- Example:
		 ```python
		 class A:
		 def __int__(self):
		 return 42
		 print(int(A()))
		 ```
- What does `__len__` return?
	-
		- Invoked when `len(obj)` is used
		- Example:
		 ```python
		 class A:
		 def __len__(self):
		 return 5
		 print(len(A()))
		 ```
- What is `__call__` used for?
	-
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
	-
		- Invoked when an object is indexed: `obj[key]`
		- Example:
		 ```python
		 class A:
		 def __getitem__(self, key):
		 return key * 2
		 a = A()
		 print(a[3]) # 6
		 ```
- What is the purpose of `__setitem__`?
	-
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
	-
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
	-
		- Invoked when the `in` operator is used: `item in obj`
		- Example:
		 ```python
		 class A:
		 def __contains__(self, item):
		 return item == "yes"
		 print("yes" in A())
		 ```
- What is the use of `__bool__`?
	-
		- Invoked when the object is used in a boolean context: `if obj` or `bool(obj)`
		- Example:
		 ```python
		 class A:
		 def __bool__(self):
		 return False
		 print(bool(A())) # False
		 ```
- What does `__iter__` do?
	-
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
	-
		- Invoked when `==` is used to compare two objects: `obj1 == obj2`
		- Example:
		 ```python
		 class A:
		 def __eq__(self, other):
		 return True
		 print(A() == A())
		 ```
- When is `__ne__` invoked?
	-
		- Invoked when `!=` is used to compare two objects: `obj1 != obj2`
		- Example:
		 ```python
		 class A:
		 def __ne__(self, other):
		 return True
		 print(A() != A())
		 ```
- What is the function of `__gt__`?
	-
		- Invoked when `>` is used to compare two objects: `obj1 > obj2`
		- Example:
		 ```python
		 class A:
		 def __gt__(self, other):
		 return True
		 print(A() > A())
		 ```
- What does `__add__` define?
	-
		- Invoked when two objects are added: `obj1 + obj2`
		- Example:
		 ```python
		 class A:
		 def __add__(self, other):
		 return "Added"
		 print(A() + A())
		 ```
- When is `__mul__` triggered?
	-
		- Invoked when two objects are multiplied: `obj1 * obj2`
		- Example:
		 ```python
		 class A:
		 def __mul__(self, other):
		 return "Multiplied"
		 print(A() * A())
		 ```
- What does `__abs__` compute?
	-
		- Computes the absolute value of an object: `abs(obj)`
		- Example:
		 ```python
		 class A:
		 def __abs__(self):
		 return 10
		 print(abs(A()))
		 ```
- What does `__neg__` handle?
	-
		- Invoked when the unary minus operator is used: `-obj`
		- Example:
		 ```python
		 class A:
		 def __neg__(self):
		 return -99
		 print(-A())
		 ```
- What is the use of `__invert__`?
	-
		- Invoked when the `~` (bitwise NOT) operator is used: `~obj`
		- Example:
		 ```python
		 class A:
		 def __invert__(self):
		 return "Inverted"
		 print(~A())
		 ```
- What is the purpose of `main()` in Python?
	-
		- An optional function that contains the entry logic for the script
		- Example:
		 ```python
		 def main():
		 print("Start here")
		 ```
- What does `if __name__ == "__main__"` mean?
	-
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
		 del handler # Triggers __del__(), closes file
		 ```
		
		 <!--EndFragment-->
