from pathlib import Path

from load_data import load_annotation_metrics
from metrics import compute_summary_statistics, group_by_taxonomy
from outliers import detect_outliers
from plotting import save_histogram, save_boxplot_by_group


def main() -> None:
    data_path = Path("data/sample_annotation_metrics.csv")
    output_dir = Path("outputs")

    df = load_annotation_metrics(data_path)

    summary = compute_summary_statistics(df)
    print("=== Summary statistics ===")
    print(summary)
    print()

    family_summary = group_by_taxonomy(df, "family")
    print("=== Mean metrics by family ===")
    print(family_summary)
    print()

    outliers = detect_outliers(df, "completeness_score")
    print("=== Candidate outliers for completeness_score ===")
    print(outliers[["genome_name", "completeness_score", "robust_z"]])
    print()

    save_histogram(df, "completeness_score", output_dir)
    save_boxplot_by_group(df, "completeness_score", "family", output_dir)


if __name__ == "__main__":
    main()
