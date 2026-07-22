# CS1604 (Lecture 2)

## Functions

Why we need to use functions?

- **Code Reusability**: Functions allow us to reuse code without having to rewrite it. This promotes efficiency and reduces the chances of errors. We don't need to make the wheel again; we can just call the function whenever we need it.

- **Modularity**: Functions help break down complex problems into smaller, manageable pieces. This makes it easier to understand and maintain the code. Each function can be designed to perform a specific task, which enhances readability and organization.

- **Abstraction**: Functions allow us to abstract away the details of how a task is performed. We can focus on what the function does rather than how it does it. This makes it easier to use and understand the code.

### Basic Syntax of Functions

```cpp
<type> <name>(<parameters>) {
    <body>
}
```

- `<type>`: The return type of the function (e.g., `int`, `void`, etc.). If the function does not return a value, we use `void`.
- `<name>`: The name of the function, which should be descriptive of its purpose.
- `<parameters>`: The input parameters for the function, enclosed in parentheses. If the function does not take any parameters, we use empty parentheses `()`.
- `<body>`: The block of code that defines what the function does. This is enclosed in curly braces `{}`.

### Return statement

The `return` statement is used to exit a function and optionally return a value to the caller. The syntax is as follows:

```cpp
return <value>;
```
- `<value>`: The value that the function returns. This must match the return type specified in the function declaration. If the function is declared with a return type of `void`, it should not return any value.

**Note on `break` vs `return`**: 
- `break` is used to exit a **loop** (like `for` or `while`) or a `switch` statement. It does not exit the function.
- `return` is used to exit the **entire function** immediately, regardless of where it is called (even inside multiple nested loops).

Here is an Example:

```cpp
#include <iostream>
using namespace std;

// Function to calculate the sum of two integers
int sum(int a, int b) {
    return a + b; // Return the sum of a and b
}

int main() {
    int num1 = 5, num2 = 10;
    int result = sum(num1, num2); // Call the sum function
    cout << "The sum of " << num1 << " and " << num2 << " is: " << result << endl; // Output the result
    return 0; // Exit the program
}
```

If you choose `void` as the return type, it means that the function does not return any value.

```cpp
#include <iostream>
using namespace std;
// Function to print a message
void printMessage() {
    cout << "Hello, this is a message from the printMessage function!" << endl;
    return;
}
```

*Mind that every function can only return one value. If you need to return multiple values, you can use structures, classes, or pointers to achieve that.*

### Main Function

Every C++ program must have a `main` function, which is the entry point of the program. The `main` function is where the execution of the program begins. It can return an integer value to indicate the success or failure of the program. The standard convention is to return `0` for successful execution.

```cpp
int main() {
    // Your code here
    return 0; // Indicate successful execution
}
```

### Function Calls

When you call a function, you provide the necessary arguments (if any) that the function requires. The function then executes its body and returns a value (if applicable). The syntax for calling a function is as follows:

```cpp
<function_name>(<arguments>);
```
- `<function_name>`: The name of the function you want to call.
- `<arguments>`: The values you pass to the function, which must match the parameters defined in the function declaration.

In the example above, we called the `sum` function with two integer arguments, `num1` and `num2`, and stored the result in the variable `result`.

```cpp
int result = sum(num1, num2); // Call the sum function
```

Also, function calls can be embedded within other function calls or expressions.

```cpp
#include <iostream>
using namespace std;

int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int incr(int a) {
    return a + 1;
}

int main() {
    cout << incr(max(5, 10)) << endl;
    return 0;
}
```

In this example, we first call the `max` function to find the maximum of `5` and `10`, which returns `10`. Then we pass that result to the `incr` function, which increments it by `1`, resulting in `11`. Finally, we print the result.

### Function Classification

Functions can be classified based on their return type and parameters. While we declare a function, we can specify the return type and the parameters it takes. Based on these characteristics, we can categorize functions into different types:

#### Boolean Functions

Boolean functions return a value of type `bool`, which can be either `true` or `false`. These functions are often used for decision-making and conditional statements.

```cpp
#include <iostream>
using namespace std;
// Function to check if a number is even
bool isEven(int num) {
    return (num % 2 == 0); // Return true if num is even, false otherwise
}

int main() {
    int number = 4;
    if (isEven(number)) {
        cout << number << " is even." << endl; // Output if the number is even
    } else {
        cout << number << " is odd." << endl; // Output if the number is odd
    }
    return 0;
}
```

#### Void Functions

Void functions do not return any value. They are typically used to perform actions or side effects, such as printing output or modifying variables.

```cpp
#include <iostream>
using namespace std;

// Function to print a message
void printMessage() {
    cout << "Hello, world!" << endl; // Print a message
}

int main() {
    printMessage(); // Call the void function to print the message
    return 0;
}
```

#### Value-Returning Functions
Value-returning functions return a value of a specified type. They are used when we need to perform a calculation or retrieve information that can be used elsewhere in the program.

```cpp
#include <iostream>
using namespace std;

// Function to calculate the area of a rectangle
double area(double width, double height) {
    return width * height; // Return the area of the rectangle
}

int main() {
    double w = 5.0, h = 3.0;
    double rectArea = area(w, h); // Call the value-returning function to calculate area
    cout << "The area of the rectangle is: " << rectArea << endl; // Output the area
    return 0;
}
```

In this example, the `area` function takes two `double` parameters (width and height) and returns the calculated area of a rectangle. The returned value is then stored in the variable `rectArea` and printed to the console.

Here we can deduce the structure of a C++ program, which typically consists of the `main` function and any additional functions that are defined to perform specific tasks. The `main` function serves as the starting point, while other functions can be called from within `main` or from other functions to perform various operations.

```cpp
#include <iostream>
using namespace std;

int f1() {
    // Function body for f1
    return 0; // Return a value of type int
}
void f2() {
    // Function body for f2
    // No return value since it's a void function
}
int main() {
    // Function body for main
    f1(); // Call function f1
    f2(); // Call function f2
    return 0; // Indicate successful execution
}
```

### Scope of Variables

The scope of a variable refers to the region of the program where the variable is defined and can be accessed. In C++, there are different types of variable scopes:

- **Local Scope**: Variables declared within a function or block are local to that function or block. They can only be accessed within that function or block and are not visible outside of it. The functions' parameters also have local scope. Any block will be covered by curly braces `{}`. For example:

```cpp
#include <iostream>
using namespace std;

void exampleFunction() {
    int localVar = 10; // localVar is only accessible within exampleFunction
    cout << "Local variable: " << localVar << endl; // Output the local variable
}

int main() {
    exampleFunction(); // Call the function to demonstrate local variable scope
    // cout << localVar; // This would cause an error since localVar is not accessible here
    return 0;
}
```
- **Global Scope**: Variables declared outside of all functions have global scope. They can be accessed from any function within the program. However, it's generally recommended to minimize the use of global variables to avoid unintended side effects and improve code maintainability.

```cpp
#include <iostream>
using namespace std;

int globalVar = 20; // globalVar is accessible from any function

void exampleFunction() {
    cout << "Global variable: " << globalVar << endl; // Output the global variable
}

int main() {
    exampleFunction(); // Call the function to demonstrate global variable scope
    cout << "Global variable in main: " << globalVar << endl; // Output the global variable in main
    return 0;
}
```

#### Stack Frames

Every function call creates a collection of memory block. And any operations whether it's reading and assigning variables, or calling other functions, will be performed on that memory block. The collection of memory blocks is called a **stack frame**. Each stack frame contains the function's parameters, local variables, and return address. When a function is **called**, a new stack frame is created for that function, and when the function **returns**, its stack frame is destroyed.

Here is a flowchart illustrating the lifecycle of a stack frame and the process of returning a value:

```text

+--------+    call f1()    +--------+
|  main  |  -------------> |  f1()  | 
+--------+                 +--------+
    |                           |
    |                           |
+------------+             +--------+
| return val | <-----------|  Stack |
+------------+             +--------+
```

**Difference with Python**: Take a look at the following Python code:

```python
def swap(a, b):
    a, b = b, a

if __name__ == "__main__":
    x = 5
    y = 10
    swap(x, y)
    print(x, y)  # Output: 10 5
```

However, in C++, if we just copy the same grammar like code, it will be like this:

```cpp
#include <iostream>
using namespace std;

void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int x = 5;
    int y = 10;
    swap(x, y);
    cout << x << " " << y << endl; // Output: 5 10
    return 0;
}
```

In the C++ version, the `swap` function does not actually swap the values of `x` and `y` in the `main` function because it is passing the parameters by value. This means that the function receives copies of `x` and `y`, and any changes made to `a` and `b` inside the `swap` function do not affect the original variables in `main`.

In contrast, in Python, the `swap` function successfully swaps the values of `x` and `y` because Python's variables are references to objects, and the swap operation modifies the references rather than creating new copies.

**Variables in C++ is not a REFERENCE**: In C++, variables are not references by default. When you pass a variable to a function, you are passing a **copy** of that variable (pass by value). If you want to modify the original variable, you need to use pointers or references.

#### Life Cycle of a Variable

The life cycle of a variable refers to the period during which the variable exists in memory and can be accessed. The life cycle of a variable is determined by its scope and storage duration.

| Time | Global Variables | Local Variables |
|------|------------------|-----------------|
|Begin to live| When the program **starts** | When the function is **called** |
|End to live| When the program **ends** | When the function **returns** |

Now we can give the execution flow of a C++ program:

1. Global memory for global variables are allocated.
2. Execution starts from the `main` function.
3. The execution continues:
   - Sequential execution of statements in `main`.
   - Loops and conditionals are executed based on their logic.
   - Function calls grow stack frames.
   - Function returns destroy stack frames.
4. The execution ends when the `main` function returns.
5. The global memory is deallocated when the program ends.

#### Detailed Scope of Variables

1. Scope of function parameters:

```cpp
#include <iostream>
using namespace std;

void exampleFunction(int param) {
    cout << "Parameter value: " << param << endl; // Accessing the parameter within the function
}

int main() {
    exampleFunction(42); // Calling the function with an argument
    // cout << param; // This would cause an error since param is not accessible here
    return 0;
}
```

2. Scope of loop variables:

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 5; i++) {
        cout << "Loop variable i: " << i << endl; // Accessing the loop variable within the loop
    }
    // cout << i; // This would cause an error since i is not accessible here
    return 0;
}
```

3. Scope of global variables:
   
```cpp
#include <iostream>
using namespace std;

int globalVar = 100; // Global variable accessible throughout the program

void exampleFunction() {
    cout << "Global variable in function: " << globalVar << endl; // Accessing the global variable within a function
}

int main() {
    cout << "Global variable in main: " << globalVar << endl; // Accessing the global variable in main
    exampleFunction(); // Calling the function to demonstrate access to global variable
    return 0;
}
```

**Remark**: Mind that the variables in `main` function are local to `main` and cannot be accessed by other functions, while global variables can be accessed by any function in the program. Loop variables and function parameters are also local to their respective scopes and cannot be accessed outside of those scopes. All global variables must be "naked" (i.e., not declared within any function) to be accessible globally.

4. Scope of functions:

```cpp
#include <iostream>
using namespace std;

void exampleFunction() {
    cout << "This is an example function." << endl; // Function body
}

int main() {
    exampleFunction(); // Calling the function to demonstrate its scope
    return 0;
}
```

In this example, the `exampleFunction` is defined outside of the `main` function and can be called from `main` or any other function in the program. The scope of the function is global, meaning it can be accessed from anywhere in the program.

**Function Prototypes**: In C++, if you want to call a function before its definition, you need to declare a function prototype. A function prototype is a declaration of a function that specifies its name, return type, and parameters, but does not include the function body. This allows the compiler to recognize the function when it is called before its definition.

```cpp
#include <iostream>
using namespace std;

// Function prototype
void exampleFunction();

int main() {
    exampleFunction(); // Calling the function before its definition
    return 0;
}

// Function definition
void exampleFunction() {
    cout << "This is an example function." << endl; // Function body
}
```

### Visibility of Definition across Modules

In multiple source files, while compiling, the compiler needs to know the declaration of a function or variable to ensure that it is used correctly. Which means that any function or variable can be defined **once** in the whole program. For example:

```cpp
// a.cpp
int counter;
```

```cpp
// b.cpp
int counter; // This will cause a multiple definition error
```

How can we solve this issue if we just want to use the variable in their own source files? We can use the `static` keyword to limit the visibility of the variable to the file it is defined in.

```cpp
// a.cpp
static int counter; // This variable is only visible in a.cpp
```

```cpp
// b.cpp
static int counter; // This variable is only visible in b.cpp
```

Mind that the `static` keyword guarantees that the variable is only visible within the file it is defined in. Each files can have its own `counter` variable without causing a multiple definition error.

So how can we share a variable across multiple files? We can use the `extern` keyword to declare a variable that is defined in another file.

```cpp
// a.cpp
int counter; // Define the variable in a.cpp
```

```cpp
// b.cpp
extern int counter; // Declare the variable defined in a.cpp
```

The `extern` keyword confirms that this is just a declaration of the variable, and the actual definition is in another file. We can also use it for functions:

```cpp
// a.cpp
void exampleFunction() {
    // Function body
}
```

```cpp
// b.cpp
extern void exampleFunction(); // Declare the function defined in a.cpp
```

### Recursion

Recursion is a programming technique where a function calls itself in order to solve a problem. A recursive function typically has two main components: a base case that stops the recursion, and a recursive case that breaks the problem into smaller subproblems.

Recursion has its own pros and cons:

- **Pros**:
  - It can simplify code and make it more elegant, especially for problems that have a natural recursive structure (e.g., tree traversal, factorial calculation).
  - It can reduce the amount of code needed to solve a problem, as it eliminates the need for explicit loops and temporary variables.
- **Cons**:
  - Recursive functions can be less efficient than their iterative counterparts, as each recursive call adds a new frame to the call stack.
  - Deep recursion can lead to stack overflow errors if the recursion depth exceeds the maximum stack size.

Here is a simple example of a recursive function to calculate the factorial of a number:

```cpp
#include <iostream>
using namespace std;

int sum(int n) {
    int result;
    if (n == 0) result = 0;
    else result = n + sum(n - 1);
    return result;
}

int main() {
    int n = 5;
    cout << "The sum of integers from 0 to " << n << " is: " << sum(n) << endl; // Output the result of the recursive function
    return 0;
}
```

In this example, the `sum` function calculates the sum of all integers from `0` to `n`. The base case is when `n` is `0`, where it returns `0`. For any other positive integer `n`, it returns `n` plus the result of calling `sum` with `n - 1`, which breaks the problem into smaller subproblems until it reaches the base case.

Another example is the Fibonacci sequence:

```cpp
#include <iostream>
using namespace std;

int fibo(int n) {
    if (n <= 1) return n;
    else return fibo(n-1) + fibo(n-2);
}

int main() {
    int result = fibo(5);
    cout << result << endl;
    return 0;
}
```

#### Stack Frames in Recursion

In recursion computations, stack frames are allocated as recursive calls happen. Each time a function calls itself, a new stack frame is created to hold the parameters and local variables for that call. When the base case is reached and the function starts returning, the stack frames are destroyed in reverse order as the function unwinds back to the original call.

#### Tail Recursion 
Tail recursion is a special case of recursion where the recursive call is the last operation performed in the function. Tail recursion can be optimized by the compiler into iterative loops, which can improve performance and reduce the risk of stack overflow.

We use factorial as an example to illustrate tail recursion:

```cpp
#include <iostream>
using namespace std;

int factorial(int n, int acc = 1) {
    if (n == 0) return acc; // Base case: return the accumulated result
    else return factorial(n - 1, n * acc); // Recursive case: multiply n with the accumulated result and call factorial with n-1
}

int main() {
    int n = 5;
    cout << "Factorial of " << n << " is: " << factorial(n) << endl; // Output the result of the tail recursive function
    return 0;
}
```

Here is another example of tail recursion using the Fibonacci sequence:

```cpp
#include <iostream>
using namespace std;

int fibo(int n, int a = 0, int b = 1) {
    if (n == 0) return a; // Base case: return the nth Fibonacci number
    else return fibo(n - 1, b, a + b); // Recursive case: update a and b for the next call
}

int main() {
    int n = 5;
    cout << "Fibonacci of " << n << " is: " << fibo(n) << endl; // Output the result of the tail recursive function
    return 0;
}
```

#### Mutual Recursion
Mutual recursion occurs when two or more functions call each other in a recursive manner. This can be useful for solving problems that have a natural mutual recursive structure.

```cpp
#include <iostream>
using namespace std;

bool isEven(int n); // Forward declaration of isEven
bool isOdd(int n); // Forward declaration of isOdd

bool isEven(int n) {
    if (n == 0) return true; // Base case: 0 is even
    else return isOdd(n - 1); // Recursive case: check if n-1 is odd
}

bool isOdd(int n) {
    if (n == 0) return false; // Base case: 0 is not odd
    else return isEven(n - 1); // Recursive case: check if n-1 is even
}
```

