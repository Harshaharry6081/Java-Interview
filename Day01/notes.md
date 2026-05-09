# Core Java Basics

## Java Architecture & Fundamentals

- [ ] **Q1. What is Java?**

Java is a high-level, class-based, object-oriented programming language developed by James Gosling at Sun Microsystems in 1995. It follows the **WORA** (Write Once, Run Anywhere) principle — compiled Java code runs on any platform that supports JVM without recompilation.

**Key characteristics:**
- Platform-independent via bytecode and JVM
- Strongly typed and statically compiled
- Automatic memory management (Garbage Collection)
- Built-in multithreading support
- Rich standard library (Java API)

```java
// Your first Java program
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Accenture!");
    }
}
```

- [ ] **Q2. What are the main features of Java?**

1. **Platform Independence** — Java code compiles to bytecode that runs on any OS with a JVM.
2. **Object-Oriented** — Everything revolves around classes and objects (except primitives).
3. **Robust** — Strong type checking, exception handling, and garbage collection prevent crashes.
4. **Secure** — No pointers, bytecode verification, and a Security Manager restrict unauthorized access.
5. **Multithreaded** — Built-in support for concurrent programming via `Thread` class and `Runnable` interface.
6. **Distributed** — Libraries like RMI and EJB make building distributed applications easy.
7. **Garbage Collection** — JVM automatically reclaims unused memory, preventing memory leaks.

- [ ] **Q3. What is JVM and why is it important?**

**JVM (Java Virtual Machine)** is the runtime engine that executes Java bytecode. It is the cornerstone of Java's platform independence.

**How it works:**
1. You write `.java` source code
2. The `javac` compiler compiles it into `.class` files containing **bytecode**
3. The JVM interprets or JIT-compiles the bytecode into native machine code at runtime

**Key components of JVM:**
- **ClassLoader** — Loads `.class` files into memory
- **Runtime Data Areas** — Heap, Stack, Method Area, PC Register, Native Method Stack
- **Execution Engine** — Interpreter + JIT Compiler + Garbage Collector

```
Source Code (.java) → javac → Bytecode (.class) → JVM → Native Machine Code
```

- [ ] **Q4. What is the difference between JDK, JRE, and JVM?**

| Component | What it is | Contains |
|-----------|-----------|----------|
| **JVM** | Runtime engine that executes bytecode | Interpreter, JIT Compiler, GC |
| **JRE** | Runtime environment to run Java apps | JVM + Core Libraries (rt.jar) |
| **JDK** | Full development kit to build Java apps | JRE + javac compiler + debugger + tools |

**Relationship:** JDK ⊃ JRE ⊃ JVM

**In an interview, say:** "JVM is the engine, JRE is the car with the engine, and JDK is the full garage with tools to build and run the car."

- [ ] **Q5. Explain `public static void main(String[] args)`**

This is the **entry point** of every standalone Java application. The JVM looks for this exact signature to start execution.

| Keyword | Purpose |
|---------|---------|
| `public` | Accessible from anywhere — JVM needs to call it from outside the class |
| `static` | No object creation needed — JVM calls it before any objects exist |
| `void` | Returns nothing to the JVM |
| `main` | Special method name recognized by the JVM |
| `String[] args` | Command-line arguments passed to the program |

```java
public class Demo {
    public static void main(String[] args) {
        System.out.println("Arguments received: " + args.length);
        for (String arg : args) {
            System.out.println(arg);
        }
    }
}
// Run: java Demo hello world
// Output: Arguments received: 2, hello, world
```

**Follow-up:** If `main` is not declared `static`, the program compiles but throws `NoSuchMethodError` at runtime.

- [ ] **Q6. What are the four pillars of OOP in Java?**

1. **Encapsulation** — Bundling data and methods together, hiding internal state via access modifiers.
2. **Inheritance** — A child class acquires properties and behaviors of a parent class using `extends`.
3. **Polymorphism** — Same method name behaves differently based on context (overloading/overriding).
4. **Abstraction** — Hiding complex implementation details and exposing only essential features.

```java
// All 4 pillars in one example:
abstract class Animal {                    // ABSTRACTION
    private String name;                   // ENCAPSULATION (private field)

    public Animal(String name) { this.name = name; }
    public String getName() { return name; }  // Getter

    abstract void speak();                 // Abstract method
}

class Dog extends Animal {                 // INHERITANCE
    public Dog(String name) { super(name); }

    @Override
    void speak() {                         // POLYMORPHISM (overriding)
        System.out.println(getName() + " says Woof!");
    }
}

class Cat extends Animal {
    public Cat(String name) { super(name); }

    @Override
    void speak() {
        System.out.println(getName() + " says Meow!");
    }
}
```

- [ ] **Q7. What is inheritance in Java?**

Inheritance allows a class to **reuse** fields and methods from another class. The child class (`subclass`) inherits from the parent class (`superclass`) using the `extends` keyword.

**Types of inheritance in Java:**
- **Single** — Class B extends Class A
- **Multilevel** — Class C extends B, B extends A
- **Hierarchical** — Class B and Class C both extend Class A
- **Multiple** — NOT supported with classes (supported via interfaces)

```java
class Vehicle {
    int speed = 100;
    void start() { System.out.println("Vehicle started"); }
}

class Car extends Vehicle {
    int doors = 4;

    @Override
    void start() {
        super.start();  // Call parent method
        System.out.println("Car engine roaring!");
    }
}

// Usage:
Car car = new Car();
car.start();       // "Vehicle started" then "Car engine roaring!"
System.out.println(car.speed);  // 100 (inherited)
```

**Why Java doesn't support multiple inheritance with classes:** To avoid the **Diamond Problem** — if two parent classes have the same method, the compiler can't decide which one to use.

- [ ] **Q8. What is polymorphism in Java?**

Polymorphism means "many forms." The same method call can behave differently depending on the object type.

**Compile-time polymorphism (Method Overloading):**

```java
class Calculator {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }
}
```

**Runtime polymorphism (Method Overriding):**

```java
class Shape {
    void draw() { System.out.println("Drawing shape"); }
}

class Circle extends Shape {
    @Override
    void draw() { System.out.println("Drawing circle"); }
}

// Runtime polymorphism in action:
Shape s = new Circle();  // Parent reference, child object
s.draw();  // Output: "Drawing circle" (decided at runtime)
```

- [ ] **Q9. Explain encapsulation with an example.**

Encapsulation is the practice of making fields `private` and providing controlled access through `public` getters and setters. This protects data integrity.

```java
public class BankAccount {
    private double balance;  // Hidden from outside

    public BankAccount(double initialBalance) {
        if (initialBalance > 0) {
            this.balance = initialBalance;
        }
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;  // Validation before modifying
        }
    }

    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;  // Insufficient funds
    }
}
```

**Benefits:** Data validation, flexibility to change internal implementation without breaking external code, and security.

- [ ] **Q10. What is an interface in Java?**

An interface is a **contract** that defines what a class must do, but not how. It contains abstract method signatures that implementing classes must provide.

```java
public interface Payable {
    double calculatePay();              // abstract (implicitly)
    default String getCurrency() {      // default method (Java 8+)
        return "INR";
    }
    static boolean isValidAmount(double amt) {  // static method
        return amt > 0;
    }
}

public class Employee implements Payable {
    private double salary;

    public Employee(double salary) { this.salary = salary; }

    @Override
    public double calculatePay() {
        return salary;  // Must implement this
    }
}
```

**Key points for interview:**
- A class can implement **multiple** interfaces (solving the multiple inheritance limitation)
- Since Java 8: interfaces can have `default` and `static` methods
- Since Java 9: interfaces can have `private` methods

- [ ] **Q11. What is the difference between an abstract class and an interface?**

| Feature | Abstract Class | Interface |
|---------|---------------|-----------|
| Methods | Abstract + concrete methods | Abstract, default, static, private |
| Variables | Any type (instance vars allowed) | Only `public static final` constants |
| Constructors | Can have constructors | Cannot have constructors |
| Inheritance | `extends` (single only) | `implements` (multiple allowed) |
| Access modifiers | Any modifier | Methods are `public` by default |
| When to use | Shared behavior + partial implementation | Pure contract / capability definition |

**Interview tip:** "Use abstract class when classes share common state and behavior. Use interface when unrelated classes need to share a capability."

- [ ] **Q12. What are constructors in Java?**

A constructor is a special method that initializes an object when it is created. It has the **same name as the class** and **no return type**.

```java
public class Employee {
    private String name;
    private int id;

    // Default constructor
    public Employee() {
        this.name = "Unknown";
        this.id = 0;
    }

    // Parameterized constructor
    public Employee(String name, int id) {
        this.name = name;
        this.id = id;
    }

    // Copy constructor
    public Employee(Employee other) {
        this.name = other.name;
        this.id = other.id;
    }
}
```

**Key rules:**
- If you don't write any constructor, Java provides a default no-arg constructor
- If you write ANY constructor, Java no longer provides the default one
- Constructors can be overloaded but NOT overridden
- `this()` calls another constructor in the same class; `super()` calls the parent constructor

## Exception Handling

- [ ] **Q13. What are exceptions in Java?**

An exception is an **unwanted event** that disrupts the normal flow of a program at runtime. Java provides a robust exception handling mechanism using `try-catch-finally-throw-throws`.

**Exception hierarchy:**
```
Throwable
├── Error (OutOfMemoryError, StackOverflowError) — unrecoverable
└── Exception
    ├── Checked Exceptions (IOException, SQLException) — must handle
    └── RuntimeException (unchecked)
        ├── NullPointerException
        ├── ArrayIndexOutOfBoundsException
        ├── ArithmeticException
        └── ClassCastException
```

- [ ] **Q14. What is the difference between checked and unchecked exceptions?**

| Aspect | Checked Exception | Unchecked Exception |
|--------|------------------|-------------------|
| When checked | Compile-time | Runtime |
| Must handle? | Yes (try-catch or throws) | No (optional) |
| Extends | `Exception` directly | `RuntimeException` |
| Examples | `IOException`, `SQLException` | `NullPointerException`, `ArithmeticException` |
| Cause | External factors (file, network) | Programming bugs (null access, bad cast) |

```java
// Checked — compiler forces you to handle it
try {
    FileReader file = new FileReader("data.txt");
} catch (FileNotFoundException e) {
    System.out.println("File not found: " + e.getMessage());
}

// Unchecked — no compiler enforcement
String str = null;
str.length();  // NullPointerException at runtime
```

- [ ] **Q15. Explain try-catch-finally with examples.**

```java
public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;  // ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero: " + e.getMessage());
        } finally {
            System.out.println("This ALWAYS executes (cleanup code)");
        }
    }
}
```

**Important interview questions:**
- **Does `finally` run after `return`?** Yes! The `finally` block executes even if `try` or `catch` has a `return` statement.
- **When does `finally` NOT execute?** Only when `System.exit()` is called or JVM crashes.
- **Can we have `try` without `catch`?** Yes, `try-finally` is valid for cleanup without handling.

```java
// Multi-catch (Java 7+)
try {
    // risky code
} catch (IOException | SQLException e) {
    System.out.println("Caught: " + e.getMessage());
}
```

## Strings

- [ ] **Q16. What is String Pool in Java?**

The String Pool (also called String Intern Pool) is a special memory area inside the **Heap** where Java stores string literals for reuse. When you create a string literal, JVM checks the pool first — if it exists, the same reference is returned.

```java
String s1 = "Hello";           // Goes to String Pool
String s2 = "Hello";           // Reuses same reference from Pool
String s3 = new String("Hello"); // Creates new object in Heap (NOT pool)

System.out.println(s1 == s2);      // true (same reference)
System.out.println(s1 == s3);      // false (different objects)
System.out.println(s1.equals(s3)); // true (same content)

String s4 = s3.intern();          // Moves to pool
System.out.println(s1 == s4);      // true
```

- [ ] **Q17. Why is String immutable in Java?**

Strings are immutable (cannot be changed after creation) for these reasons:

1. **String Pool Optimization** — Multiple references can safely share the same string object
2. **Thread Safety** — Immutable objects are inherently thread-safe, no synchronization needed
3. **Security** — Database URLs, passwords, and class names are strings; immutability prevents tampering
4. **Hashing** — `hashCode()` is cached because the value never changes, making HashMap operations faster

```java
String s = "Hello";
s.concat(" World");       // Creates NEW string, original unchanged
System.out.println(s);    // Still "Hello"

s = s.concat(" World");   // Now s points to new string
System.out.println(s);    // "Hello World"
```

- [ ] **Q18. What is the difference between String, StringBuilder, and StringBuffer?**

| Feature | String | StringBuilder | StringBuffer |
|---------|--------|--------------|-------------|
| Mutability | Immutable | Mutable | Mutable |
| Thread-safe | Yes (immutable) | No | Yes (synchronized) |
| Performance | Slow for modifications | Fastest | Slower than StringBuilder |
| Use case | Fixed text, keys | Single-threaded string building | Multi-threaded string building |

```java
// BAD: Creates many temporary String objects
String result = "";
for (int i = 0; i < 1000; i++) {
    result += i;  // Creates new String each iteration!
}

// GOOD: Uses mutable buffer
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append(i);  // Modifies same object
}
String result = sb.toString();
```

## Keywords & Modifiers

- [ ] **Q19. What is the `static` keyword in Java?**

The `static` keyword means the member belongs to the **class itself**, not to any instance. Static members are shared across all objects.

```java
public class Counter {
    static int count = 0;   // Shared by ALL objects

    public Counter() {
        count++;  // Increments for every new object
    }

    static void showCount() {  // Can be called without object
        System.out.println("Total objects: " + count);
    }
}

// Usage:
new Counter();
new Counter();
Counter.showCount();  // "Total objects: 2"
```

**Static block:** Executed once when the class is loaded, used to initialize static variables.

```java
static {
    System.out.println("Class loaded!");
}
```

**Key rule:** Static methods CANNOT access non-static members directly (because no `this` context exists).

- [ ] **Q20. What is the `final` keyword in Java?**

The `final` keyword restricts modification:

| Usage | Effect |
|-------|--------|
| `final` variable | Value cannot be changed (constant) |
| `final` method | Cannot be overridden by subclasses |
| `final` class | Cannot be extended/inherited |

```java
final class Constants {                     // Cannot extend this class
    static final double PI = 3.14159;       // Constant value

    final void display() {                  // Cannot override this method
        System.out.println("PI = " + PI);
    }
}

// final with reference types:
final List<String> list = new ArrayList<>();
list.add("Hello");    // OK — modifying contents is allowed
// list = new ArrayList<>();  // ERROR — cannot reassign reference
```

- [ ] **Q21. Explain the `this` and `super` keywords.**

**`this`** refers to the current object instance:

```java
public class Employee {
    private String name;

    public Employee(String name) {
        this.name = name;       // Resolves ambiguity
    }

    public Employee() {
        this("Default");        // Calls parameterized constructor
    }
}
```

**`super`** refers to the parent class:

```java
class Animal {
    String type = "Animal";
    void display() { System.out.println("I am an animal"); }
}

class Dog extends Animal {
    String type = "Dog";

    void display() {
        super.display();                    // Calls parent method
        System.out.println("I am a dog");
        System.out.println(super.type);     // "Animal"
        System.out.println(this.type);      // "Dog"
    }
}
```

**Neither `this` nor `super` can be used in static methods** because static context has no object instance.

## Collections & Generics

- [ ] **Q22. What is the Collections Framework?**

The Collections Framework is a unified architecture for storing and manipulating groups of objects. It provides interfaces, implementations, and algorithms.

**Core interfaces hierarchy:**
```
Collection
├── List (ordered, allows duplicates)
│   ├── ArrayList (fast read, slow insert)
│   ├── LinkedList (fast insert, slow read)
│   └── Vector (synchronized, legacy)
├── Set (no duplicates)
│   ├── HashSet (unordered, O(1) operations)
│   ├── LinkedHashSet (insertion order)
│   └── TreeSet (sorted, O(log n))
└── Queue (FIFO)
    ├── PriorityQueue
    └── Deque → ArrayDeque

Map (key-value pairs, NOT part of Collection interface)
├── HashMap (unordered, allows null key)
├── LinkedHashMap (insertion order)
├── TreeMap (sorted by keys)
└── ConcurrentHashMap (thread-safe)
```

- [ ] **Q23. What is the difference between ArrayList and LinkedList?**

| Feature | ArrayList | LinkedList |
|---------|-----------|-----------|
| Internal structure | Dynamic array | Doubly linked list |
| Random access (get) | O(1) — fast | O(n) — slow |
| Insert/Delete (middle) | O(n) — slow (shifting) | O(1) — fast (pointer change) |
| Memory | Less (only data) | More (data + 2 pointers per node) |
| Best for | Frequent reads | Frequent insertions/deletions |

```java
List<String> arrayList = new ArrayList<>();
arrayList.add("A");
arrayList.get(0);  // O(1) — direct index access

List<String> linkedList = new LinkedList<>();
linkedList.add("A");
linkedList.add(0, "B");  // O(1) — just change pointers
```

- [ ] **Q24. What are Generics in Java?**

Generics provide **compile-time type safety** by letting you parameterize classes, interfaces, and methods with types.

```java
// Without generics — dangerous, runtime ClassCastException
List list = new ArrayList();
list.add("Hello");
list.add(123);           // No error at compile time!
String s = (String) list.get(1);  // ClassCastException at runtime!

// With generics — safe, compile-time checking
List<String> safeList = new ArrayList<>();
safeList.add("Hello");
// safeList.add(123);    // Compile ERROR — caught early!
String s = safeList.get(0);  // No cast needed
```

**Bounded type parameters:**

```java
// T must be a Number or its subclass
public <T extends Number> double sum(List<T> list) {
    double total = 0;
    for (T item : list) {
        total += item.doubleValue();
    }
    return total;
}
```

## Threading & Concurrency

- [ ] **Q25. What is a thread and how to create one?**

A thread is the smallest unit of execution within a process. Java supports multithreading natively.

**Two ways to create a thread:**

```java
// Way 1: Extend Thread class
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread running: " + getName());
    }
}

// Way 2: Implement Runnable interface (preferred)
class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Runnable running: " + Thread.currentThread().getName());
    }
}

// Usage:
new MyThread().start();
new Thread(new MyRunnable()).start();

// Way 3: Lambda (Java 8+)
new Thread(() -> System.out.println("Lambda thread!")).start();
```

**Why Runnable is preferred:** Java doesn't support multiple inheritance. If you extend `Thread`, you can't extend anything else.

- [ ] **Q26. What is the `synchronized` keyword?**

`synchronized` ensures that only **one thread** can access a block of code or method at a time, preventing race conditions.

```java
class BankAccount {
    private int balance = 1000;

    // Only one thread can execute this method at a time
    public synchronized void withdraw(int amount) {
        if (balance >= amount) {
            System.out.println(Thread.currentThread().getName() + " withdrawing " + amount);
            balance -= amount;
            System.out.println("Remaining balance: " + balance);
        } else {
            System.out.println("Insufficient funds!");
        }
    }
}
```

- [ ] **Q27. What is the `volatile` keyword?**

`volatile` ensures a variable's value is always read from **main memory**, not from a thread's local cache. It guarantees visibility but NOT atomicity.

```java
class SharedFlag {
    volatile boolean running = true;  // All threads see the latest value

    void stop() {
        running = false;  // Change is immediately visible to all threads
    }

    void run() {
        while (running) {
            // Without volatile, this loop might never end
            // because the thread might cache 'running = true'
        }
    }
}
```

## Wrapper Classes & Autoboxing

- [ ] **Q28. What are wrapper classes and autoboxing?**

Wrapper classes convert primitives into objects. They are needed because Java Collections only work with objects.

| Primitive | Wrapper |
|-----------|---------|
| `int` | `Integer` |
| `double` | `Double` |
| `boolean` | `Boolean` |
| `char` | `Character` |

**Autoboxing** (primitive → object) and **Unboxing** (object → primitive) happen automatically:

```java
// Autoboxing
Integer num = 42;           // int → Integer (automatic)
List<Integer> list = new ArrayList<>();
list.add(10);               // int 10 autoboxed to Integer

// Unboxing
int value = num;            // Integer → int (automatic)

// DANGER: NullPointerException with unboxing!
Integer nullNum = null;
int crash = nullNum;        // Throws NullPointerException!
```

**Integer Cache Trap (favorite interview question):**

```java
Integer a = 127;
Integer b = 127;
System.out.println(a == b);   // true (cached range: -128 to 127)

Integer c = 128;
Integer d = 128;
System.out.println(c == d);   // false! (outside cache, different objects)
System.out.println(c.equals(d)); // true (compare values, not references)
```

## == vs .equals()

- [ ] **Q29. What is the difference between == and .equals()?**

| Operator | Compares | Use for |
|----------|----------|---------|
| `==` | References (memory addresses) | Primitives, checking if same object |
| `.equals()` | Content/value | Object content comparison |

```java
String s1 = new String("Hello");
String s2 = new String("Hello");

System.out.println(s1 == s2);       // false (different objects in heap)
System.out.println(s1.equals(s2));  // true (same content)

// With String pool literals:
String s3 = "Hello";
String s4 = "Hello";
System.out.println(s3 == s4);       // true (same pool reference)
```

**Always override `.equals()` and `.hashCode()` together** when using custom objects as HashMap keys.

## Garbage Collection

- [ ] **Q30. How does Garbage Collection work in Java?**

The Garbage Collector (GC) automatically reclaims memory occupied by objects that are **no longer reachable** (no references pointing to them).

**How it works:**
1. **Mark** — GC identifies all reachable objects starting from GC Roots (static vars, local vars, thread stacks)
2. **Sweep** — Unreachable objects are removed from memory
3. **Compact** — Remaining objects are compacted to reduce fragmentation

**JVM Heap generations:**
```
Heap Memory
├── Young Generation (new objects)
│   ├── Eden Space (objects created here)
│   ├── Survivor Space S0
│   └── Survivor Space S1
└── Old Generation (long-lived objects)

Non-Heap
└── Metaspace (class metadata, since Java 8)
```

**You CANNOT force GC**, only suggest it:

```java
System.gc();               // Request (JVM may ignore)
Runtime.getRuntime().gc(); // Same — just a suggestion
```

**Common causes of memory leaks despite GC:**
- Unclosed resources (streams, connections)
- Static collections that keep growing
- Listeners/callbacks not deregistered
- `ThreadLocal` variables not cleaned up