import time

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

def main():
    i = 1
    while i <= 50:
        start_time = time.perf_counter()
        
        result = fibo(i)
        
        end_time = time.perf_counter()
        elapsed = end_time - start_time

        print(f"The {i}th number of the series is {result} (Time: {elapsed:.6f}s)")
        i += 1

if __name__ == "__main__":
    main()