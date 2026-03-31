import pandas as pd

from src.outliers import robust_z_scores, detect_outliers


def test_robust_z_scores_returns_same_length() -> None:
    series = pd.Series([10, 11, 10, 12, 50])
    scores = robust_z_scores(series)
    assert len(scores) == len(series)


def test_detect_outliers_finds_extreme_value() -> None:
    df = pd.DataFrame(
        {
            "genome_name": ["A", "B", "C", "D", "E"],
            "completeness_score": [90, 91, 89, 92, 50],
        }
    )
    outliers = detect_outliers(df, "completeness_score", threshold=3.0)
    assert "E" in outliers["genome_name"].values
