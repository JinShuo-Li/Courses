# CS1604 (Lecture 4)

## Abstract Data Types (ADTs)

Compared with concrete data structures, abstract data types (ADTs) are more general and focus on the behavior of the data rather than its implementation.

An ADT includes **Domains** and **Operations**. Domains is a set of values that the ADT can take on, while Operations are the functions that can be performed on the ADT.

Simply saying, an ADT omits the details of how the data is stored and manipulated, and instead focuses on what operations can be performed on the data. This is called **Abstraction**.

## Constructors and Destructors

### Constructors

Constructors are a setter for initializing the store of an object upon creation.

- No return type, not even `void`.
- Automatically called when an object is created.
- Can be overloaded.

### Destructors

Destructors are a setter for cleaning up an object at the end of its lifetime.

- No return type, no parameters.
- Automatically called when an object is destroyed.
- Cannot be overloaded (only one destructor per class).

### Important Notes

- Constructors **do not** allocate memory — they only initialize already‑allocated storage.
- Destructors **do not** deallocate memory — they only perform cleanup.
- Memory allocation and deallocation can be:
  - **Automatic** (global objects, local objects)
  - **Manual** (dynamic memory, e.g., `new` / `delete`)

### Syntax Example

```cpp
class MyClass {
public:
    // Constructors (overloaded)
    MyClass();                // default constructor
    MyClass(int value);       // parameterized constructor

    // Destructor
    ~MyClass();

private:
    int data;
};
```

### Calling Constructors

Constructors are automatically called when an object variable is defined:

```cpp
MyClass obj1;            // default constructor
MyClass obj2(10);        // constructor with int
MyClass obj3 = 20;       // equivalent to MyClass obj3(20);
```

You can also create **temporary objects** using a constructor:

```cpp
cout << string("Hello") << endl;   // temporary string object
```

### Example: String Class Constructors

```cpp
string s1("Hello");        // from C-style string
string s2(10, 'x');        // 10 copies of 'x'
string s3(s1, 7);          // substring from index 7 to end
string s4(s1, 7, 5);       // substring of length 5 starting at index 7
```

## Streams

### Output stream

In different programming languages, the syntax for outputting to the console varies:

```python
print("Hello, World!")
```

```cpp
cout << "Hello, World!" << endl;
```

```java
System.out.println("Hello, World!");
```

C++ output streams are represented as an ADT/class `ostream` in the standard library `<ostream>`.

- `cout` is an instance of `ostream` that represents the standard output stream.
- Method for pushing a value for ostream `os`:

```cpp
os.put(ch);
```

#### Insertions

The `<<` operator is overloaded for `ostream` to allow for easy insertion of various types of data:

```cpp
cout << "Hello, World!" << endl;  // string literal
cout << 42 << endl;               // integer
cout << 3.14 << endl;             // floating-point number
```

#### Manipulators

Manipulators are special functions that can be used with `ostream` to modify the output format. For example:

```cpp
cout << std::hex << 255 << std::endl;  // outputs "ff" in hexadecimal
cout << std::dec << 255 << std::endl;  // outputs "255"
cout << std::setw(10) << 42 << std::endl; // outputs "        42" (width of 10)
```

#### Set Precision

- fixed: forces the output to be in fixed-point notation.
- scientific: forces the output to be in scientific notation.

```cpp
cout << std::fixed << std::setprecision(2) << 3.14159 << std::endl; // outputs "3.14"
cout << std::scientific << std::setprecision(2) << 3.14159 << std::endl; // outputs "3.14e+00"
```

### Input stream

In C++, the `cin` object is an instance of the `istream` class, which represents the standard input stream. It is used to read input from the user.

#### Extractions

The `>>` operator is overloaded for `istream` to allow for easy extraction of various types of data:

```cpp
int age;
std::cout << "Enter your age: ";
std::cin >> age;  // reads an integer from the user
std::cout << "You entered: " << age << std::endl;
```

#### Getline

The `getline` function is used to read an entire line of input, including spaces:

```cpp
std::string name;
std::cout << "Enter your name: ";
std::getline(std::cin, name);  // reads a line of input into the string 'name'
std::cout << "Hello, " << name << "!" << std::endl;
```

Read from the input stream one character at a time:

```cpp
// read all characters until EOF
void read_input(istream& is) {
    char ch;
    while (is.get(ch)) {
        // process character ch
    }
}
```

Or we can read the input and check `EOF`:

```cpp
void read_input(istream& is) {
    char ch;
    while (true) {
        ch = is.get();
        if (is.eof()) break; // check for EOF
        // process character ch
    }
}
```

If you want to read line by line, you can use `getline`:

```cpp
void read_input(istream& is) {
    std::string line;
    while (std::getline(is, line)) {
        // process line
    }
}
```

### Data File I/O

We can also read from and write to files using file streams in C++. The `<fstream>` header provides the `ifstream` class for reading from files and the `ofstream` class for writing to files.

```cpp
#include <fstream>

using namespace std;

// Declare file stream variables
ifstream infile;
ofstream outfile;

// Open a file for reading
infile.open("input.txt");

//Alternatively, if the file name is a string variable:
string filename = "input.txt";
infile.open(filename.c_str()); // convert string to C-style string, but since C++11, you can directly use string itself.

// Check if the file was opened successfully
if (!infile) {
    cout << "Error opening file!" << endl;
    return -1;
}

// Read from the file
string line;
while (getline(infile, line)) {
    // Process the line
    cout << line << endl; // For example, print the line to the console
}

// Close the file
infile.close();
```

To write to a file:

```cpp
// Open a file for writing
outfile.open("output.txt");
if (!outfile) {
    cout << "Error opening file!" << endl;
    return -1;
}

// Write to the file
outfile << "Hello, World!" << endl;
// outfile here is an ofstream object, so we can use the same insertion operator as with cout
```