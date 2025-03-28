#**********************************Optimal Solution***************
import time
import matplotlib.pyplot as plt


def layup_seq_iterative(num):
    start_time = time.time()

    memo = {
        1: 1,
        2: 2
    }
    for n in range(3, num + 1):
        if n % 2 == 0:
            memo[n] = memo[n - 1] + memo[n - 2]
        else:
            memo[n] = (2 * memo[n - 1]) + memo[n - 2]

    end_time = time.time()
    runtime = end_time - start_time
    return memo[num], runtime


def plot_runtimes(test_values):
    runtimes = []

    for n in test_values:
        # Get runtime only
        runtime = layup_seq_iterative(n)[1]
        runtimes.append(runtime)

    plt.plot(test_values, runtimes, marker='o')
    plt.xlabel('N (Input size)')
    plt.ylabel('Runtime (seconds)')
    plt.title('N vs Runtime for Layup Sequence')
    plt.grid(True)
    plt.show()


def main():
    # Testing S(n=10,000)
    result, runtime = layup_seq_iterative(10000)
    print(f"Result: {result}")
    print(f"Runtime: {runtime} seconds")

    # Plotting N vs Runtime
    test_values = [100, 500, 1000, 5000, 10000, 20000, 50000]
    plot_runtimes(test_values)


if __name__ == "__main__":
    main()

#************************Recursive/Memoization Solution**************************
# import sys
# import time
## Increase recursion depth
# sys.setrecursionlimit(15000)  # Increase recursion depth
#
#
# def layup_seq(num, memo=None):
#     if memo is None:
#         memo = {}
#
#     # Base cases:
#     if num == 1:
#         return 1
#     if num == 2:
#         return 2
#
#
#     if num in memo:
#         return memo[num]
#
#     # Store result to avoid recalculation
#     if num % 2 == 0:
#         result = layup_seq(num - 1, memo) + layup_seq(num - 2, memo)
#     else:
#         result = (2 * layup_seq(num - 1, memo)) + layup_seq(num - 2, memo)
#
#     memo[num] = result
#     return result
#
#
# def main():
#     start_time = time.time()
#     result = layup_seq(10000)
#     end_time = time.time()
#     print(f"Result: {result}")
#     print(f"Runtime: {end_time - start_time} seconds")
#
#
# if __name__ == "__main__":
#     main()
