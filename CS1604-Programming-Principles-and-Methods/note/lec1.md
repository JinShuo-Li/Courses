# CS1604 (Lecture 1)

## Introduction to C++ Programming

C++ is a powerful programming language that supports multiple programming paradigms, including procedural, object-oriented, and generic programming. It was developed by Bjarne Stroustrup in the early 1980s as an extension of the C programming language. C++ provides features such as classes, inheritance, polymorphism, and templates, which allow developers to create complex and efficient software applications.

For a standard C++ program, the entry point is the `main` function, which is where the execution of the program begins. The `main` function can return an integer value, which is typically used to indicate the success or failure of the program.

```cpp
#include <iostream>
int main() {
    std::cout << "Hello, World!" << std::endl; // Output a message to the console
    return 0; // Indicate that the program ended successfully
}
```

The `#include <iostream>` directive is used to include the input/output stream library, which allows us to use the `std::cout` object for outputting text to the console. The `std::endl` is used to insert a newline character and flush the output buffer.

To make the code more concise, we can use the `using namespace std;` directive, which allows us to omit the `std::` prefix when using standard library components.

```cpp
#include <iostream>
using namespace std;
int main() {
    cout << "Hello, World!" << endl; // Output a message to the console
    return 0; // Indicate that the program ended successfully
}
```

## Variables and Data Types

A variable is a named location in memory that can hold a value of a particular data type.

In C++, you can declare variables of various data types, such as `int`, `double`, `char`, etc. You can also declare multiple variables of the same type in a single statement.

```
<type> <variable1> = <value1>, <variable2> = <value2>, ..., <variableN> = <valueN>;
```

```cpp
// example
int age = 20;
double pi = 3.14159, psi = 1.61803, phi = 1.41421;
```

For a variable, there are three important properties: Name, Type, and Location. The name is used to identify the variable, the type determines what kind of data it can hold, and the location is where the variable is stored in memory.

Also, user-defined types can be created using `struct` or `class` in C++. This allows you to define your own data structures that can hold multiple values of different types. We will cover this in more detail in later lectures.

### Data Types

#### Integer Types

Basic integer types include `short`, `int`, `long`, and `long long`, which can be signed or unsigned. The size of these types can vary depending on the system, but typically `int` is 4 bytes, `short` is 2 bytes, and `long` is 4 or 8 bytes.

```cpp
//example
short s = 32767; // maximum value for signed short
unsigned int u = 4294967295; // maximum value for unsigned int
long l = 2147483647; // maximum value for signed long
long long ll = 9223372036854775807; // maximum value for signed long long
```

#### Floating-Point Types

Floating-point types include `float`, `double`, and `long double`. They are used to represent real numbers and can hold a wide range of values with varying precision.

In scientific notation, `double` is considered the default type for floating-point literals, while `float` is used when you want to save memory and can tolerate less precision. `long double` provides even more precision than `double`, but it is not commonly used.

```cpp
// example
float f = 3.14f; // single precision
double d = 3.141592653589793; // double precision
long double ld = 3.1415926535897932384626433832795; // extended precision
```

#### Boolean Type

The `bool` type is used to represent boolean values, which can be either `true` or `false`. It is commonly used in conditional statements and loops to control the flow of the program.

```cpp
// example
bool isSunny = true;
```

#### Character Type

The `char` type is used to represent individual characters. It can hold a single character and is typically 1 byte in size. Characters are enclosed in single quotes (`'`) in C++.

```cpp
// example
char letter = 'A';
```

#### Enumeration Type

An enumeration type (`enum`) is a user-defined type that consists of a set of named integral constants. It is used to represent a collection of related values in a more readable and maintainable way.

```cpp
// example
enum Color { RED, GREEN, BLUE };
Color myColor = RED; // Define a variable of type Color and assign it the value RED
```

#### Other Types

- Constants: A constant is a value that cannot be changed after it has been assigned. In C++, you can declare constants using the `const` keyword.

```cpp
// example
const double PI = 3.14159; // Define a constant for the value of pi
```
- Void: The `void` type is used to indicate that a function does not return a value. It is also used for pointers that do not point to any specific type.

```cpp
// example
void printMessage() {
    cout << "This function does not return a value." << endl;
}
```

- Auto: The `auto` keyword allows the compiler to automatically deduce the type of a variable from its initializer.

```cpp
// example
auto x = 42; // x is deduced to be of type int
auto y = 3.14; // y is deduced to be of type double
```

### Operators

Operators are symbols that perform operations on variables and values. C++ provides a wide range of operators, including arithmetic, relational, logical, bitwise, and assignment operators.

#### Arithmetic Operators
Arithmetic operators include `+`, `-`, `*`, `/`, and `%` for addition, subtraction, multiplication, division, and modulus operations, respectively.

```cpp
// example
int a = 10, b = 5;
int sum = a + b; // 15
int difference = a - b; // 5
int product = a * b; // 50
int quotient = a / b; // 2
int remainder = a % b; // 0
```

#### Relational Operators
Relational operators include `==`, `!=`, `<`, `>`, `<=`, and `>=` for equality, inequality, less than, greater than, less than or equal to, and greater than or equal to comparisons.

```cpp
// example
int x = 10, y = 20;
bool isEqual = (x == y); // false
bool isNotEqual = (x != y); // true
bool isLessThan = (x < y); // true
bool isGreaterThan = (x > y); // false
bool isLessThanOrEqual = (x <= y); // true
bool isGreaterThanOrEqual = (x >= y); // false
```

#### Logical Operators
Logical operators include `&&` (logical AND), `||` (logical OR), and `!` (logical NOT) for combining boolean expressions.

```cpp
// example
bool a = true, b = false;
bool andResult = a && b; // false
bool orResult = a || b; // true
bool notResult = !a; // false
```

**Mind that `1` is considered `true` and `0` is considered `false` in C++.**, this is the same as in C and Python. However, in C++, any non-zero value is considered `true` when evaluated in a boolean context, while `0` is considered `false`. This means that you can use integers in conditional statements, and they will be evaluated as boolean values.

```cpp
// example
int value = 5;
if (value) {
    cout << "Value is true" << endl; // This will be printed
} else {
    cout << "Value is false" << endl;
}
```

In this example, since `value` is `5`, which is a non-zero integer, it will be evaluated as `true`, and the output will be "Value is true". If `value` were `0`, it would be evaluated as `false`, and the output would be "Value is false".

### I/O Streams
C++ provides a powerful input/output (I/O) system through the use of streams. The `iostream` library provides the `std::cin` object for input and the `std::cout` object for output. You can use these objects to read from the console and write to the console, respectively.

#### Basic Output

To output text to the console, you can use the `std::cout` object along with the insertion operator (`<<`).

```cpp
// example
#include <iostream>
using namespace std;

int main() {
    cout << "Hello" <<"," << "World!" << endl; // Output a message to the console
    return 0; // Indicate that the program ended successfully
}
```

#### Basic Input

To read input from the console, you can use the `std::cin` object along with the extraction operator (`>>`).

```cpp
// example
#include <iostream>
using namespace std;

int main() {
    int age;
    cout << "Enter your age: "; // Prompt the user for input
    cin >> age; // Read an integer value from the console and store it in the variable 'age'
    cout << "You entered: " << age << endl; // Output the value entered by the user
    return 0; // Indicate that the program ended successfully
}
```

In this example, the program prompts the user to enter their age, reads the input from the console, and then outputs the value entered by the user. The `cin` object is used to read the input, and the `cout` object is used to display the output.

To input multiple values, you can use the `cin` object multiple times or use it in a single statement.

```cpp
// example
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Enter two integers: "; // Prompt the user for input
    cin >> a >> b; // Read two integer values from the console and store them in variables 'a' and 'b'
    cout << "You entered: " << a << " and " << b << endl; // Output the values entered by the user
    return 0; // Indicate that the program ended successfully
}
```

### Expressions and Statements

An expression is a combination of variables, literals, operators, and function calls that can be evaluated to produce a value. A statement is a complete line of code that performs an action. In C++, statements can be simple or compound.

#### Expressions

An expression can be as simple as a single variable or literal, or it can be a more complex combination of variables, literals, and operators.

- Arithmetic expressions: Arithmetic expressions involve arithmetic operators and produce a numeric result.

```cpp
// example
int x = 10, y = 5;
int sum = x + y; // 15
int product = x * y; // 50
```

- Assignment expressions: Assignment expressions involve the assignment operator (`=`) and are used to assign values to variables. Assignment expressions will overwrite the previous value of the variable with the new value. We can also use embedded assignments to redefine the precedence of operations.

```cpp
// example
int a = 10, b = 20; // Assign the value 10 to variable 'a' and 20 to variable 'b'
a = a + 5; // Update the value of 'a' to be the current value of 'a' plus 5 (15)
b = a + (a * 2); // Update the value of 'b' to be the current value of 'a' plus the result of 'a' multiplied by 2 (15 + (15 * 2) = 45)
```

- Shorthand assignment expressions: C++ provides shorthand assignment operators that combine an arithmetic operation with assignment. For example, `+=`, `-=`, `*=`, `/=`, and `%=`.

- Increment and decrement expressions: The increment operator (`++`) and decrement operator (`--`) are used to increase or decrease the value of a variable by 1, respectively.

```cpp
// example
int count = 0;
count++; // Increment count by 1 (count becomes 1)
count--; // Decrement count by 1 (count becomes 0)
```

**Avoid short-circuit evaluation combining side effects!**

Mind that `i++` and `++i` are not the same. Let's take a look at the following example:

```cpp
#include <iostream>
using namespace std;

int main() {
    int i = 3;
    int j, k;
    j = i++; // j is assigned the value of i (3), then i is incremented to 4
    i = 3; // Reset i to 3
    k = ++i; // i is incremented to 4, then k is assigned the value of i (4)
}
```

We can simply say that `i++` is a post-increment operator, which means it returns the value of `i` before incrementing it, while `++i` is a pre-increment operator, which means it increments `i` first and then returns the new value.

- Boolean expressions and Logical expressions: Boolean expressions involve relational and logical operators and produce a boolean result (`true` or `false`).

```cpp
// example
int x = 10, y = 20;
bool isGreater = (x > y); // false
bool isEqual = (x == y); // false
bool isLessOrEqual = (x <= y); // true
```

Mind that nested expressions are evaluated according to operator precedence and associativity rules. Thus, the result of some expressions in `cpp` may differ from the same expression in `python` due to differences in operator precedence and associativity.

```cpp
#include <iostream>

using namespace std;

int main() {
	bool i;
	i = -2 < -1 < 0;
	cout << i << endl; // Output: 0 (false)
    return 0;
}
```

In this example, the expression `-2 < -1 < 0` is evaluated as `(-2 < -1) < 0`. The first part `(-2 < -1)` evaluates to `true` (which is represented as `1` in C++), and then the expression becomes `1 < 0`, which evaluates to `false` (represented as `0`). Therefore, the output of the program will be `0`.

And the correct way to evaluate the expression would be:

```cpp
#include <iostream>

using namespace std;

int main() {
	bool i;
	i = (-2 < -1) && (-1 < 0);
	cout << i << endl;
}
```

#### Statements

A statement is a complete line of code that performs an action. In C++, statements can be simple or compound.

- Simple statements: A simple statement is a single line of code that performs an action, such as an assignment or a function call.

- Control flow statements: Control flow statements include `if`, `else`, `switch`, `for`, `while`, and `do-while` statements, which are used to control the flow of execution in a program.

- Compound statements: A compound statement, also known as a **block**, is a group of statements enclosed in curly braces (`{}`) that are treated as a single unit.

**If statements** are used to control the flow of execution in a program based on a condition. The basic syntax of an `if` statement is as follows:

```cpp
if (condition) {
    // code to be executed if the condition is true
} else {
    // code to be executed if the condition is false
}
```

Here is an example of an `if` statement:

```cpp
// Checking of leap years
#include <iostream>
using namespace std;

int main()
{  
   int year;
   bool result;
   cout << "Please enter the year: ";
   cin >> year;
   result = (year % 4 == 0 && year % 100 !=0) || year % 400 == 0;
   if (result) 
     cout << year << " is a leap year!"<< endl;
   else   
     cout << year << " is not a leap year." << endl;
   return 0;
}
```

In this example, the program checks if a given year is a leap year or not. The condition for a leap year is that it must be divisible by 4 but not divisible by 100, unless it is also divisible by 400. The program evaluates the condition and outputs whether the year is a leap year or not based on the result.

In addition to `if` statements, C++ also provides `else if` statements for checking multiple conditions.

```cpp
if (condition1) {
    // code to be executed if condition1 is true
} else if (condition2) {
    // code to be executed if condition2 is true
} else {
    // code to be executed if both condition1 and condition2 are false
}
```

**Switch statements** are used to perform different actions based on different conditions. The basic syntax of a `switch` statement is as follows:

```cpp
switch (expression) {
    case value1:
        // code to be executed if expression equals value1
        break;
    case value2:
        // code to be executed if expression equals value2
        break;
    // more cases...
    default:
        // code to be executed if expression does not match any case
}
```

Here is an example of a `switch` statement:

```cpp
// example
#include <iostream>
using namespace std;

int main() {
    int day;
    cout << "Enter a number (1-7) to represent a day of the week: ";
    cin >> day;

    switch (day) {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        case 4:
            cout << "Thursday" << endl;
            break;
        case 5:
            cout << "Friday" << endl;
            break;
        case 6:
            cout << "Saturday" << endl;
            break;
        case 7:
            cout << "Sunday" << endl;
            break;
        default:
            cout << "Invalid input! Please enter a number between 1 and 7." << endl;
    }

    return 0; // Indicate that the program ended successfully
}
```

**Mind that the case can be any constant expression (e.g., a literal value, a variable that is a constant, or an expression that evaluates to a constant value). To avoid fall-through, we use the `break` statement at the end of each case block. If a `break` statement is omitted, the program will continue to execute the next case block(s) until it encounters a `break` or reaches the end of the switch statement.**

**While loops** are used to repeat a block of code as long as a specified condition is true. The basic syntax of a `while` loop is as follows:

```cpp
while (condition) {
    // code to be executed as long as the condition is true
}
```

Here is an example of a `while` loop:

```cpp
// This program computes the sum of integers up to a number
int main() {
   int n;
   cin >> n;
   if (n < 0) return -1; // n must be positive

   int sum = 0, i = 1;
   while (i <= n) {
     sum += i;
     i++;
   }
   cout << “The sum is ” << sum << endl;
   return 0;
}
```

In this example, the program computes the sum of integers from 1 to `n` using a `while` loop. The loop continues to execute as long as `i` is less than or equal to `n`, and it updates the value of `sum` by adding `i` to it in each iteration. After the loop finishes, the program outputs the computed sum.

**For loops** are used to repeat a block of code a specific number of times. The basic syntax of a `for` loop is as follows:

```cpp
for (initialization; condition; increment) {
    // code to be executed for each iteration
}
```
Here is an example of a `for` loop:

```cpp
// This program computes the sum of integers up to a number
int main() {
   int n;
   cin >> n;
   if (n < 0) return -1; // n must be positive

   int sum = 0;
   for (int i = 1; i <= n; i++) {
     sum += i;
   }
   cout << “The sum is ” << sum << endl;
   return 0;
}
```

In this example, the program computes the sum of integers from 1 to `n` using a `for` loop. The loop initializes `i` to 1, checks if `i` is less than or equal to `n`, and increments `i` by 1 in each iteration. The body of the loop updates the value of `sum` by adding `i` to it. After the loop finishes, the program outputs the computed sum.

