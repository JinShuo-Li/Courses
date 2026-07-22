# CS1604 (Lecture 3)

## Strings

String is a sequence of characters. In C++, strings are represented as arrays of characters terminated by a null character (`'\0'`).

The ADT of a string is defined in the C++ standard library as `<string>`.

Here is an simple example of using strings in C++:

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string name;
    cout << "Enter your name: ";
    cin >> name;
    cout << "Hello, " << name << "!" << endl;
    return 0;
}
```

### Basic String Operations

String is a powerful data type that allows us to perform various operations. Some of the basic operations include:

#### Initialization

You can initialize a string in several ways:

```cpp
string str1 = "Hello";
string str3 = str1 + " " + str2; // Concatenation
```

#### Reading and Writing Strings
You can read a string from the user using `cin` and write it to the console using `cout`.

```cpp
string str;
cout << "Enter a string: ";
cin >> str; // Reads a single word
cout << "You entered: " << str << endl;
```

However, if you want to read a full line of text (including spaces), you should use `getline`:

```cpp
string str;
cout << "Enter a string: ";
getline(cin, str); // Reads a full line of text
cout << "You entered: " << str << endl;
```

#### Common Operations

- **Length**: You can get the length of a string using the `length()` method.

```cpp
string str = "Hello";
cout << "Length of the string: " << str.length() << endl;
```

- **Concatenation**: You can concatenate strings using the `+` operator.

```cpp
string str1 = "Hello";
string str2 = "World";
string str3 = str1 + " " + str2; // Concatenation
cout << str3 << endl; // Output: Hello World
```

- **Comparison**: You can compare strings using the `==`, `!=`, `<`, `>`, `<=`, and `>=` operators. Mind that string comparison follows lexicographical order.

```cpp
string str1 = "Hello";
string str2 = "World";
if (str1 == str2) {
    cout << "The strings are equal." << endl;
} else {
    cout << "The strings are not equal." << endl;
}
```

- **Getters and Setters**: You can access individual characters in a string using the `[]` operator.

```cpp
string str = "Hello";
cout << str[0] << endl; // Output: H
str[0] = 'h'; // Modifying the first character
cout << str << endl; // Output: hello
```

We can also get multiple characters using a loop:

```cpp
string str = "Hello";
for (size_t i = 0; i < str.length(); i++) {
    cout << str[i] << " ";
}
cout << endl; // Output: H e l l o
```

**Remark**: There isn't exists any operations like Python to get multiple characters at once, we can only use a loop to achieve the same result.

#### Substring

You can get a substring of a string using the `substr()` method.

```cpp
string str = "Hello World";
string sub = str.substr(0, 5); // Get the substring from index 0 with length 5
cout << sub << endl; // Output: Hello
```

Also, the default method of `substr()` is to get the substring from the specified index to the end of the string:

```cpp
string str = "Hello World";
string sub = str.substr(6); // Get the substring from index 6 to the end
cout << sub << endl; // Output: World
```

#### Find
You can find the position of a substring using the `find()` method.

```cpp
string str = "Hello World";
int pos = str.find("World");
if (pos != string::npos) {
    cout << "Substring found at position: " << pos << endl; // Output: Substring found at position: 6
} else {
    cout << "Substring not found." << endl;
}
```

#### Delete/Insert/Replace
You can delete, insert, or replace parts of a string using the `erase()`, `insert()`, and `replace()` methods.

```cpp
string str = "Hello World";
str.erase(5, 1); // Delete the space at index 5
cout << str << endl; // Output: HelloWorld
```
```cpp
string str = "Hello World";
str.insert(5, " "); // Insert a space at index 5
cout << str << endl; // Output: Hello World
```
```cpp
string str = "Hello World";
str.replace(6, 5, "C++"); // Replace "World" with "C++"
cout << str << endl; // Output: Hello C++
```

## Modules & Interfaces

The C++ standard library provides a rich set of modules and interfaces for working with strings. In this part, we will discuss some detail about libraries and interfaces in C++.

In C++ programme, the `include` directive is used to include the contents of a file or library into the program. This allows us to use the functions and classes defined in that file or library.

Any C++ program include two types of libraries: **standard libraries** and **user-defined libraries**. Standard libraries are provided by the C++ language and include a wide range of functions and classes for various purposes, such as input/output, string manipulation, mathematical operations, etc. User-defined libraries are created by programmers to encapsulate their own functions and classes for reuse in multiple programs.

Below is some widely used standard libraries in C++:

| Library | Description |
| --- | --- |
| `<iostream>` | Provides input and output stream objects. |
| `<string>` | Provides the `std::string` class for working with strings. |
| `<vector>` | Provides the `std::vector` class for working with dynamic arrays. |
| `<algorithm>` | Provides a collection of algorithms for sorting, searching, and manipulating data. |
| `<cmath>` | Provides mathematical functions. |
| `<cctype>` | Provides functions for character classification and conversion. |

Here we need to introduce the `cctype` library, which provides functions for character classification and conversion. Some commonly used functions in this library include:
| Function | Description |
| --- | --- |
| `isalpha(ch)` | Checks if the character is an alphabetic letter. |
| `isdigit(ch)` | Checks if the character is a digit. |
| `isupper(ch)` | Checks if the character is an uppercase letter. |
| `islower(ch)` | Checks if the character is a lowercase letter. |
| `toupper(ch)` | Converts the character to uppercase. |
| `tolower(ch)` | Converts the character to lowercase. |

In addition to standard libraries, programmers can create their own user-defined libraries. A user-defined library is a file that contains function and class definitions that can be reused in multiple programs. To create a user-defined library, you typically create a header file (with a `.h` extension) that contains the declarations of the functions and classes, and a source file (with a `.cpp` extension) that contains the implementations of those functions and classes.

### How to Write a Header File (.h)

Header files are used to declare the interface of a module. Here are the key steps and components:

#### 1. Header Guards
To prevent a header file from being included multiple times in the same compilation unit (which would cause redefinition errors), use header guards or `#pragma once`.

**Using Header Guards:**
```cpp
#ifndef MY_LIBRARY_H
#define MY_LIBRARY_H

// Declarations go here

#endif
```

**Using `#pragma once` (Modern approach):**
```cpp
#pragma once

// Declarations go here
```

#### 2. Declarations
Inside the header file, you only include the **declarations** (prototypes), not the full implementation.

```cpp
#pragma once
#include <string>

// Function declaration
void greet(std::string name);

// Class declaration
class Counter {
public:
    Counter();
    void increment();
    int getCount() const;
private:
    int count;
};
```

#### 3. Best Practices
- **Minimize Includes**: Only include what is absolutely necessary for the declarations. 
- **Avoid `using namespace std;`**: Never put this in a header file, as it forces that namespace on every file that includes the header. Use explicit prefixes like `std::string` instead.
- **Inline Functions**: If a function is very short, you can define it in the header using the `inline` keyword.

### How to Use a Header File

To use a user-defined header file, you need to provide the implementation in a `.cpp` file and include the header in your main program.

#### 1. Implementation File (`.cpp`)
This file contains the actual code for the functions declared in the header.

```cpp
#include "my_library.h"

// Implementation of declared functions
void greet(std::string name) {
    // ...
}
```

#### 2. Main Program
Include the header using double quotes (`""`) to tell the compiler to look in the local directory.

```cpp
#include <iostream>
#include "my_library.h"

int main() {
    greet("User");
    return 0;
}
```

#### 3. Compilation
When compiling, you must include all relevant `.cpp` files:
```bash
g++ main.cpp my_library.cpp -o my_program
```

## Aliases & References

In C++, any variable is consisted of two parts: The value itself and the name/address that points to the value. And any value can have multiple names/addresses that point to it. This is the concept of **aliases**.

For example, **name** and the **id** of a variable are aliases of the same object. They both point to the same value in memory. 

More specifically, aliases in C++ are called **references**.

```cpp
// Syntax
<type>& <name> = <variable>;
const <type>& <name> = <variable>; // For constant references
```

The keyword `const` means that the reference cannot be used to modify the value it points to.

### Call by Name

By declaring a function parameter as a reference:

```cpp
<type> <name>(<type>& parameter) {
    \\ The function body may read or write id.
}
```

```cpp
<type> <name>(const <type>& parameter) {
    \\ The function body may only read id.
}
```

**Call by name** is much more efficient than **call by value** because it avoids copying the value of the argument. Instead, it passes a reference to the original variable, allowing the function to directly access and modify the variable if needed. This is especially beneficial for large data structures or objects, as it can significantly reduce memory usage and improve performance.