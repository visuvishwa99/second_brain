---
tags:
  - languages
---

# Java Concepts for Data Engineering

## Object-Oriented Programming (OOP) Core Concepts

### 1. Class and Objects
A **Class** is a blueprint/template. An **Object** is an instance of that class.

```java
// Define a class
class Car {
 String make;
 String model;
 int year;

 void drive() {
 System.out.println("Driving the car...");
 }
}

// Create objects
Car car1 = new Car();
car1.make = "Toyota";
```

### 2. Encapsulation
Bundling data and methods within a single unit (class) and restricting direct access to some of an object's components (using `private`).

```java
class BankAccount {
 private double balance; // Private data

 public void deposit(double amount) { // Public interface
 balance += amount;
 }

 public double getBalance() {
 return balance;
 }
}
```

### 3. Inheritance
Mechanism where one class acquires the properties and behaviors of another class.
**Keyword**: `extends`

```java
class Vehicle {
 void startEngine() {
 System.out.println("Starting engine...");
 }
}

class Car extends Vehicle { // Car inherits from Vehicle
 void drive() {
 startEngine(); // Can call inherited method
 System.out.println("Driving...");
 }
}
```

### 4. Polymorphism
The ability to take multiple forms. Achieved via:
* **Method Overloading**: Same method name, different parameters.
* **Method Overriding**: Subclass provides a specific implementation of a method already defined in its parent class.

```java
// Method Overriding Example
class Animal {
 void makeSound() { System.out.println("Animal sound"); }
}

class Dog extends Animal {
 @Override
 void makeSound() { System.out.println("Bark"); }
}
```

### 5. Abstraction
Hiding implementation details and showing only functionality.
* **Abstract Class**: Can have both abstract (empty) and concrete methods.
* **Interface**: Blueprint of a class, static constants and abstract methods (mostly).

```java
interface Drawable {
 void draw();
}

class Rectangle implements Drawable {
 public void draw() {
 System.out.println("Drawing rectangle...");
 }
}
```

---

## Generics
Generics allow you to define classes, interfaces, and methods with placeholders for types (e.g., `<T>`). This ensures type safety at compile time.

**Benefits**:
* **Type Safety**: Catch invalid types at compile time.
* **No Casting**: Eliminates need for explicit casting.
* **Code Reusability**: Single logic for multiple data types.

### Generic Class
```java
class Box<T> {
 private T item;
 public void set(T item) { this.item = item; }
 public T get() { return item; }
}

// Usage
Box<Integer> intBox = new Box<>();
intBox.set(10);
```

### Generic Collections (Common in Data Engineering)
```java
List<String> names = new ArrayList<>();
names.add("Alice");
// names.add(123); // Compile-time error!

Map<Integer, String> idMap = new HashMap<>();
idMap.put(1, "Data");
```

### Generic Method
```java
public static <T> void printArray(T[] array) {
 for (T item : array) {
 System.out.print(item + " ");
 }
}
```
