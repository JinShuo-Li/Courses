import math
import copy

class Functions:
    """
    A class for wrapping mathematical functions with bounds, error handling, 
    and numerical analysis capabilities.
    """
    def __init__(self, func, value=0, a=-10, b=10, tolerance=1e-5):
        if not callable(func):
            raise TypeError("1-1: The variable 'func' must be a callable function (e.g., lambda or def)")
        
        if not (isinstance(value, (int, float))):
            raise TypeError("1-2: The target 'value' must be an integer or float")
            
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("1-3: The bounds 'a' and 'b' must be integers or floats")
            
        if a >= b:
            raise ValueError("1-4: Left bound 'a' must be strictly less than right bound 'b'")
            
        if not isinstance(tolerance, (int, float)):
            raise TypeError("1-5: The 'tolerance' must be an integer or float")
            
        if tolerance <= 0:
            raise ValueError("1-6: Tolerance must be positive")

        self.func = func
        self.value = value
        self.left = float(a)
        self.right = float(b)
        self.toler = float(tolerance)

    def set_bounds(self, a, b):
        """
        Update the domain [a, b] of the function.
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("2-1: The bounds 'a' and 'b' must be integers or floats")
        if a >= b:
            raise ValueError("2-2: Left bound 'a' must be strictly less than right bound 'b'")
        
        self.left = float(a)
        self.right = float(b)

    def __call__(self, x):
        """
        Evaluate f(x). Raises error if out of bounds.
        Allows usage like: y = my_obj(x)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("3-1: Input 'x' must be a number")
            
        if not (self.left <= x <= self.right):
            return None 
            
        try:
            return self.func(x)
        except Exception as e:
            raise RuntimeError(f"3-2: Error evaluating function at x={x}: {str(e)}")

    def solve_bisec(self):
        """
        Finds root such that f(x) = self.value using Bisection Method.
        """
        def target_func(x):
            return self.func(x) - self.value
        
        a, b = self.left, self.right
        
        try:
            fa = target_func(a)
            fb = target_func(b)
        except Exception:
            raise RuntimeError("4-1: Failed to evaluate function at bounds")

        if abs(fa) < self.toler: return a
        if abs(fb) < self.toler: return b
        
        if fa * fb > 0:
            return None 
            
        iteration = 0
        max_iter = 1000
        
        while abs(b - a) > self.toler and iteration < max_iter:
            mid = (a + b) / 2.0
            fmid = target_func(mid)
            
            if abs(fmid) < 1e-15:
                return mid
            
            if fa * fmid < 0:
                b = mid
                fb = fmid
            else:
                a = mid
                fa = fmid
            iteration += 1
            
        return (a + b) / 2.0

    def solve_newton(self, x0=None, max_iter=1000):
        """
        Finds root using Newton-Raphson Method.
        """
        if x0 is None:
            x0 = (self.left + self.right) / 2.0
        
        if not isinstance(x0, (int, float)):
            raise TypeError("5-1: Initial guess x0 must be numeric")
            
        f = lambda x: self.func(x) - self.value
        df = lambda x: (f(x + 1e-5) - f(x - 1e-5)) / 2e-5
        
        x = x0
        for _ in range(max_iter):
            if not (self.left <= x <= self.right):
                return None
            try:
                fx = f(x)
                if abs(fx) < self.toler:
                    return x
                    
                dfx = df(x)
                if abs(dfx) < 1e-12: 
                    return None
                
                x_new = x - fx / dfx
                
                if abs(x_new - x) < self.toler:
                    if self.left <= x_new <= self.right:
                        return x_new
                    return None
                x = x_new
            except:
                return None
        return None

    def solve_secant(self, max_iter=1000):
        """
        Finds root using the Secant Method.
        """
        x0 = self.left
        x1 = self.right
        
        f = lambda x: self.func(x) - self.value
        
        for _ in range(max_iter):
            fx0 = f(x0)
            fx1 = f(x1)
            
            if abs(fx1) < self.toler:
                return x1
                
            if abs(fx1 - fx0) < 1e-12:
                return None
                
            x_temp = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            
            x0 = x1
            x1 = x_temp
            
            if not (self.left <= x1 <= self.right):
                return None
                
            if abs(x1 - x0) < self.toler:
                return x1
                
        return None

    def find_minimum(self):
        """
        Finds a local minimum within bounds using Golden Section Search.
        """
        gr = (math.sqrt(5) + 1) / 2
        a = self.left
        b = self.right
        
        c = b - (b - a) / gr
        d = a + (b - a) / gr
        
        while abs(b - a) > self.toler:
            if self.func(c) < self.func(d):
                b = d
            else:
                a = c

            c = b - (b - a) / gr
            d = a + (b - a) / gr
            
        return (b + a) / 2

    def find_maximum(self):
        """
        Finds a local maximum within bounds.
        """
        neg_func = Functions(lambda x: -self.func(x), a=self.left, b=self.right, tolerance=self.toler)
        return neg_func.find_minimum()

    def derivative(self):
        """
        Returns a new Functions object representing f'(x).
        """
        def d_func(x):
            h = max(self.toler, 1e-5)
            val = (-self.func(x + 2*h) + 8*self.func(x + h) - 8*self.func(x - h) + self.func(x - 2*h)) / (12*h)
            return val
            
        return Functions(d_func, value=0, a=self.left, b=self.right, tolerance=self.toler)

    def integrate_riemann(self, steps=1000):
        """
        Calculates definite integral using Riemann Sum (Left).
        """
        if not isinstance(steps, int) or steps <= 0:
            raise ValueError("6-1: Steps must be a positive integer")
            
        h = (self.right - self.left) / steps
        total = 0
        current_x = self.left
        
        for _ in range(steps):
            total += self.func(current_x)
            current_x += h
            
        return total * h

    def integrate_simpson(self, steps=1000):
        """
        Calculates definite integral using Simpson's 1/3 Rule.
        More accurate than Riemann sum.
        """
        if not isinstance(steps, int) or steps <= 0:
            raise ValueError("6-2: Steps must be a positive integer")

        if steps % 2 != 0:
            steps += 1
            
        h = (self.right - self.left) / steps
        x = [self.left + i * h for i in range(steps + 1)]
        y = [self.func(xi) for xi in x]
        
        total = y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-1:2])
        return total * h / 3.0

    def integrate_trapezoidal(self, steps=1000):
        """
        Calculates definite integral using Trapezoidal Rule.
        """
        if not isinstance(steps, int) or steps <= 0:
            raise ValueError("6-3: Steps must be a positive integer")
            
        h = (self.right - self.left) / steps
        total = 0.5 * (self.func(self.left) + self.func(self.right))
        
        for i in range(1, steps):
            total += self.func(self.left + i * h)
            
        return total * h

    def arc_length(self, steps=1000):
        """
        Calculates the arc length of the function curve over the interval.
        L = integral of sqrt(1 + [f'(x)]^2) dx
        """
        deriv = self.derivative()
        def arc_integrand(x):
            dy = deriv(x)
            return math.sqrt(1 + dy**2)
            
        integrator = Functions(arc_integrand, a=self.left, b=self.right, tolerance=self.toler)
        return integrator.integrate_simpson(steps)

    def mean_value(self):
        """
        Calculates the average value of the function over [a, b].
        """
        area = self.integrate_simpson()
        length = self.right - self.left
        if length == 0:
            return 0
        return area / length

    def taylor_coeffs(self, x0, order=3):
        """
        Returns a list of Taylor Series coefficients [c0, c1, c2...] at point x0.
        where f(x) approx sum(ci * (x-x0)^i)
        """
        if not isinstance(order, int) or order < 0:
            raise ValueError("7-1: Order must be a non-negative integer")
        
        if not (self.left <= x0 <= self.right):
            raise ValueError("7-2: Expansion point x0 is out of bounds")

        coeffs = []
        current_func = self
        factorial = 1
        
        for i in range(order + 1):
            if i > 0: factorial *= i
            
            try:
                val = current_func(x0)
                coeffs.append(val / factorial)
            except:
                coeffs.append(0)

            current_func = current_func.derivative()
            
        return coeffs

    def __add__(self, other):
        """
        Overloads the + operator. 
        Supports: Function + Function, Function + Scalar.
        """
        if isinstance(other, (int, float)):
            def new_func(x): return self.func(x) + other
            return Functions(new_func, a=self.left, b=self.right, tolerance=self.toler)
            
        elif isinstance(other, Functions):
            def new_func(x): return self.func(x) + other.func(x)
            new_a = max(self.left, other.left)
            new_b = min(self.right, other.right)
            if new_a >= new_b:
                raise ValueError("8-1: Domains do not overlap for addition")
            return Functions(new_func, a=new_a, b=new_b, tolerance=min(self.toler, other.toler))
            
        else:
            raise TypeError("8-2: Operand must be Functions object or number")

    def __radd__(self, other):
        """
        Supports Scalar + Function.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """
        Overloads the - operator.
        Supports: Function - Function, Function - Scalar.
        """
        if isinstance(other, (int, float)):
            def new_func(x): return self.func(x) - other
            return Functions(new_func, a=self.left, b=self.right, tolerance=self.toler)
            
        elif isinstance(other, Functions):
            def new_func(x): return self.func(x) - other.func(x)
            new_a = max(self.left, other.left)
            new_b = min(self.right, other.right)
            if new_a >= new_b:
                raise ValueError("9-1: Domains do not overlap for subtraction")
            return Functions(new_func, a=new_a, b=new_b, tolerance=min(self.toler, other.toler))
            
        else:
            raise TypeError("9-2: Operand must be Functions object or number")

    def __rsub__(self, other):
        """
        Supports Scalar - Function.
        """
        if isinstance(other, (int, float)):
            def new_func(x): return other - self.func(x)
            return Functions(new_func, a=self.left, b=self.right, tolerance=self.toler)
        else:
            raise TypeError("9-3: Operand must be number")

    def __mul__(self, other):
        """
        Overloads the * operator.
        Supports: Function * Function, Function * Scalar.
        """
        if isinstance(other, (int, float)):
            def new_func(x): return self.func(x) * other
            return Functions(new_func, a=self.left, b=self.right, tolerance=self.toler)
            
        elif isinstance(other, Functions):
            def new_func(x): return self.func(x) * other.func(x)
            new_a = max(self.left, other.left)
            new_b = min(self.right, other.right)
            if new_a >= new_b:
                raise ValueError("10-1: Domains do not overlap for multiplication")
            return Functions(new_func, a=new_a, b=new_b, tolerance=min(self.toler, other.toler))
            
        else:
            raise TypeError("10-2: Operand must be Functions object or number")

    def __rmul__(self, other):
        """
        Supports Scalar * Function.
        """
        return self.__mul__(other)

    def __truediv__(self, other):
        """
        Overloads the / operator.
        """
        if isinstance(other, (int, float)):
            if abs(other) < 1e-9:
                raise ZeroDivisionError("11-1: Division by zero scalar")
            def new_func(x): return self.func(x) / other
            return Functions(new_func, a=self.left, b=self.right, tolerance=self.toler)
            
        elif isinstance(other, Functions):
            def new_func(x): 
                denom = other.func(x)
                if abs(denom) < 1e-9: raise ZeroDivisionError("11-2: Division by zero in function domain")
                return self.func(x) / denom
            new_a = max(self.left, other.left)
            new_b = min(self.right, other.right)
            if new_a >= new_b:
                raise ValueError("11-3: Domains do not overlap for division")
            return Functions(new_func, a=new_a, b=new_b, tolerance=min(self.toler, other.toler))
            
        else:
            raise TypeError("11-4: Operand must be Functions object or number")

    def __pow__(self, exponent):
        """
        Overloads the ** operator. (f(x)) ^ n
        """
        if not isinstance(exponent, (int, float)):
            raise TypeError("12-1: Exponent must be a number")
            
        def new_func(x): return self.func(x) ** exponent
        return Functions(new_func, a=self.left, b=self.right, tolerance=self.toler)

    def __neg__(self):
        """
        Overloads the unary - operator.
        """
        def new_func(x): return -self.func(x)
        return Functions(new_func, a=self.left, b=self.right, tolerance=self.toler)

    def composite(self, inner_func):
        """
        Returns f(g(x)) where self is f and inner_func is g.
        """
        if not isinstance(inner_func, Functions):
            raise TypeError("13-1: Inner function must be a Functions object")
        def new_func(x):
            gx = inner_func(x)
            if gx is None: return None
            if not (self.left <= gx <= self.right):
                raise ValueError(f"13-2: Inner function value {gx} out of outer function bounds")
            return self.func(gx)
            
        return Functions(new_func, a=inner_func.left, b=inner_func.right, tolerance=self.toler)

    def copy(self):
        """
        Returns a deep copy of the function object.
        """
        return Functions(self.func, self.value, self.left, self.right, self.toler)

    def __str__(self):
        """
        String representation of the object.
        """
        return f"Functions Object: domain=[{self.left}, {self.right}], tolerance={self.toler}"

    def plot_ascii(self, width=60, height=15):
        """
        Generates a simple ASCII plot of the function.
        """
        xs = []
        ys = []
        step = (self.right - self.left) / width

        for i in range(width + 1):
            x = self.left + i * step
            try:
                y = self.func(x)
                xs.append(x)
                ys.append(y)
            except:
                ys.append(None)

        valid_ys = [y for y in ys if y is not None]
        if not valid_ys:
            return "14-1: Cannot plot (no valid values)"
            
        min_y = min(valid_ys)
        max_y = max(valid_ys)
        y_range = max_y - min_y
        if y_range == 0: y_range = 1
        
        output = []
        output.append(f"Plotting function from {self.left} to {self.right}")
        output.append("-" * (width + 2))
        
        grid = [[' ' for _ in range(width + 1)] for _ in range(height + 1)]
        
        for i, y in enumerate(ys):
            if y is None: continue
            normalized_y = (y - min_y) / y_range
            row = int((height) * (1 - normalized_y))
            row = max(0, min(height, row))
            grid[row][i] = '*'
            
        for row in grid:
            output.append("|" + "".join(row) + "|")
            
        output.append("-" * (width + 2))
        output.append(f"Min Y: {min_y:.4f}, Max Y: {max_y:.4f}")
        
        return "\n".join(output)

def linear(m, c, a=-10, b=10):
    """
    Creates a linear function f(x) = mx + c
    """
    if not (isinstance(m, (int, float)) and isinstance(c, (int, float))):
        raise TypeError("20-1: Slope m and intercept c must be numbers")
    return Functions(lambda x: m*x + c, a=a, b=b)

def polynomial(coeffs, a=-10, b=10):
    """
    Creates a polynomial function from coefficients.
    coeffs=[c0, c1, c2] -> c0 + c1*x + c2*x^2
    """
    if not isinstance(coeffs, list):
        raise TypeError("21-1: Coeffs must be a list")
    
    def poly_func(x):
        res = 0
        for i, c in enumerate(coeffs):
            res += c * (x**i)
        return res
    return Functions(poly_func, a=a, b=b)

def sine(freq=1, amp=1, phase=0, a=-math.pi, b=math.pi):
    """
    Creates f(x) = amp * sin(freq * x + phase)
    """
    def s_func(x):
        return amp * math.sin(freq * x + phase)
    return Functions(s_func, a=a, b=b)

def compose(outer, inner):
    """
    Functional syntax for composition.
    """
    if not (isinstance(outer, Functions) and isinstance(inner, Functions)):
        raise TypeError("22-1: Arguments must be Functions objects")
    return outer.composite(inner)

if __name__ == "__main__":
    f = Functions(lambda x: x**2 - 4, a=-5, b=5)
    root = f.solve_bisec()
    print(f"Root found at: {root}")
    print(f"Function value at root: {f(root)}")
    print(f"Derivative at root: {f.derivative()(root)}")
    print(f"Integral from -5 to 5: {f.integrate_simpson()}")