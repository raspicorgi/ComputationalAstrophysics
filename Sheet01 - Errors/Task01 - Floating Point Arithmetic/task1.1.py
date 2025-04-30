import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

analytical_result = np.pi**2 / 6  # Analytical result for the sum of 1/i^2 from i=1 to infinity

def sum(k, dtype=np.float32):
    """
    Calculate the sum of 1/i^2 for i from 1 to k using the specified dtype.
    """
    i = np.arange(1, k + 1, dtype=dtype)
    res = np.sum(dtype(1.0) / i**2, dtype=dtype)
    return res

def plot_func(s_k):
    return np.abs(s_k - analytical_result) / analytical_result


if __name__ == "__main__":
    ks = [10**6, 10**7, 10**8] 
    # Prepare a DataFrame to store results
    results = []

    for k in ks:
        print(f"calculating for k={k}")
        result_float32 = sum(k, np.float32)
        result_float64 = sum(k, np.float64)
        results.append({"k": k, "dtype": "float32", "sum": result_float32})
        results.append({"k": k, "dtype": "float64", "sum": result_float64})

    df = pd.DataFrame(results)


    plt.figure(figsize=(10, 6))
    for dtype in df["dtype"].unique():
        subset = df[df["dtype"] == dtype]
        plt.plot(subset["k"], plot_func(subset["sum"]), marker="o", label=f"{dtype}")

    # plt.axhline(analytical_result, color="red", linestyle="--", label="Analytical Result")
    plt.xscale("log")
    plt.xlabel("k")
    plt.ylabel("Sum")
    plt.title("Sum of 1/i^2 for different k and dtypes")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig("task1.1.png")