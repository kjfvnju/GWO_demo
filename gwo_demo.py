# gwo_demo.py
# Simple Grey Wolf Optimizer demo solving f(x,y) = x^2 + y^2 + 5*sin(x)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def objective_function(position):
    x, y = position
    return x**2 + y**2 + 5 * np.sin(x)

def gwo(obj_func, dim, lb, ub, num_wolves=30, max_iter=200, seed=None):
    rng = np.random.default_rng(seed)
    wolves = rng.uniform(lb, ub, (num_wolves, dim))

    alpha_pos = np.zeros(dim); alpha_score = float('inf')
    beta_pos  = np.zeros(dim); beta_score  = float('inf')
    delta_pos = np.zeros(dim); delta_score = float('inf')

    history = []

    for t in range(max_iter):
        # Evaluate
        scores = np.array([obj_func(w) for w in wolves])

        # Update alpha/beta/delta
        for i, score in enumerate(scores):
            if score < alpha_score:
                alpha_score, alpha_pos = score, wolves[i].copy()
            elif score < beta_score:
                beta_score, beta_pos = score, wolves[i].copy()
            elif score < delta_score:
                delta_score, delta_pos = score, wolves[i].copy()

        history.append(alpha_score)

        # parameter a decreases linearly from 2 -> 0
        a = 2 * (1 - t / (max_iter - 1))

        # Update positions
        for i in range(num_wolves):
            X = wolves[i].copy()
            A1 = 2 * a * rng.random(dim) - a
            C1 = 2 * rng.random(dim)
            D_alpha = np.abs(C1 * alpha_pos - X)
            X1 = alpha_pos - A1 * D_alpha

            A2 = 2 * a * rng.random(dim) - a
            C2 = 2 * rng.random(dim)
            D_beta = np.abs(C2 * beta_pos - X)
            X2 = beta_pos - A2 * D_beta

            A3 = 2 * a * rng.random(dim) - a
            C3 = 2 * rng.random(dim)
            D_delta = np.abs(C3 * delta_pos - X)
            X3 = delta_pos - A3 * D_delta

            new_pos = (X1 + X2 + X3) / 3.0
            new_pos = np.clip(new_pos, lb, ub)
            wolves[i] = new_pos

    return {'alpha_pos': alpha_pos, 'alpha_score': alpha_score, 'history': np.array(history)}

def main():
    dim = 2
    lb = np.array([-5.0, -5.0])
    ub = np.array([ 5.0,  5.0])

    res = gwo(objective_function, dim, lb, ub,
              num_wolves=40, max_iter=200, seed=42)

    alpha_pos = res['alpha_pos']
    alpha_score = res['alpha_score']
    history = res['history']

    print("Best position (alpha):", alpha_pos)
    print("Best objective value:", alpha_score)

    # Save convergence plot
    plt.figure(figsize=(7,4))
    plt.plot(history)
    plt.title("GWO convergence (best fitness over iterations)")
    plt.xlabel("Iteration")
    plt.ylabel("Best fitness")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("gwo_convergence.png")
    plt.close()
    print("Saved plot: gwo_convergence.png")

    # Save history CSV
    df = pd.DataFrame({'iteration': np.arange(1, len(history)+1), 'best_fitness': history})
    df.to_csv("gwo_history.csv", index=False)
    print("Saved history: gwo_history.csv")

if __name__ == "__main__":
    main()
