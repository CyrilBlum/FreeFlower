import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")


def main():
    # Start at n=1 to avoid log(0).
    n = np.linspace(1, 100, 400)

    curves = {
        "$O(1)$": np.ones_like(n),
        "$O(\log(n))$": np.log2(n),
        "$O(n)$": n,
        "$O(n\cdot\log(n))$": n * np.log2(n),
        "$O(n^2)$": n ** 2,
        "$O(2^n)$": 2 ** (n / 10)
    }

    fig, ax = plt.subplots(figsize=(8, 5))
    for label, values in curves.items():
        ax.plot(n, values, linewidth=2, label=label)

    ax.set_title("Wachstum typischer Laufzeiten", fontsize=14)
    ax.set_xlabel("Eingabegrösse $n$", fontsize=12)
    ax.set_ylabel("Relative Laufzeit\n(logarithmisch)", fontsize=12)
    ax.set_yscale("log")
    ax.set_ylim(0.1, max([max(values) for values in curves.values()]) * 5) # Set y-axis limit to 5 times the maximum value of the curves
    ax.grid(True, which="both", linestyle="--", alpha=0.35)
    ax.legend(loc="upper left", frameon=True)

    fig.tight_layout()
    fig.savefig(
        "Grundlagen_Info/00_Programmieren/Skript/Figures/big_o_complexities_plot.pdf",
        format="pdf",
        bbox_inches="tight",
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
