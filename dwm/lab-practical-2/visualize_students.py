from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA_PATH = Path(__file__).parent / "student_data.csv"
OUTPUT_DIR = Path(__file__).parent / "figures"


def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    return df


def save_fig(fig: plt.Figure, name: str) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / name, dpi=140)
    plt.close(fig)


def plot_univariate(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    sns.histplot(df["G3"], bins=15, kde=True, color="#2563eb", ax=axes[0])
    axes[0].set_title("Final grade distribution (G3)")
    sns.countplot(x="studytime", data=df, palette="crest", ax=axes[1])
    axes[1].set_title("Study time (weekly hours band)")
    save_fig(fig, "univariate.png")


def plot_bivariate(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.scatterplot(
        x="G1",
        y="G3",
        hue="sex",
        data=df,
        palette="Set2",
        alpha=0.7,
        ax=axes[0],
    )
    axes[0].set_title("Initial vs final grades")
    sns.boxplot(x="studytime", y="G3", data=df, palette="Blues", ax=axes[1])
    axes[1].set_title("Final grade by study time")
    save_fig(fig, "bivariate.png")


def plot_multivariate(df: pd.DataFrame) -> None:
    pair = sns.pairplot(df, vars=["G1", "G2", "G3"], hue="sex", corner=True, height=2.4)
    pair.fig.suptitle("Score relationships", y=1.02)
    pair.savefig(OUTPUT_DIR / "pairplot_scores.png", dpi=140)
    plt.close(pair.fig)

    pivot = df.groupby(["studytime", "sex"])["G3"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x="studytime", y="G3", hue="sex", data=pivot, palette="Set2", ax=ax)
    ax.set_title("Mean final grade by study time and sex")
    save_fig(fig, "grouped_bar.png")


def plot_trend(df: pd.DataFrame) -> None:
    trend = df.groupby("age")["G3"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="age", y="G3", data=trend, marker="o", color="#10b981", ax=ax)
    ax.set_title("Average final grade by age")
    save_fig(fig, "trend_line.png")

    # Stacked share of internet access by study time
    crosstab = pd.crosstab(df["studytime"], df["internet"], normalize="index")
    fig, ax = plt.subplots(figsize=(8, 4))
    crosstab.plot(kind="bar", stacked=True, color=["#1d4ed8", "#e5e7eb"], ax=ax)
    ax.set_ylabel("Share")
    ax.set_title("Internet access within study time groups")
    save_fig(fig, "stacked_bar.png")


def main() -> None:
    df = load_data()
    plot_univariate(df)
    plot_bivariate(df)
    plot_multivariate(df)
    plot_trend(df)
    print(f"Saved figures to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
