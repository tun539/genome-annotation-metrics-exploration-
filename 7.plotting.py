from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def save_histogram(df: pd.DataFrame, column: str, output_dir: str | Path) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.hist(df[column].dropna(), bins=10)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(output_path / f"{column}_histogram.png")
    plt.close()


def save_boxplot_by_group(df: pd.DataFrame, metric: str, group_col: str, output_dir: str | Path) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    grouped = [group[metric].dropna().values for _, group in df.groupby(group_col)]
    labels = [name for name, _ in df.groupby(group_col)]

    plt.figure(figsize=(10, 5))
    plt.boxplot(grouped, labels=labels)
    plt.title(f"{metric} by {group_col}")
    plt.xlabel(group_col)
    plt.ylabel(metric)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(output_path / f"{metric}_by_{group_col}_boxplot.png")
    plt.close()
