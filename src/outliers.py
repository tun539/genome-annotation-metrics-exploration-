import numpy as np
import pandas as pd


def robust_z_scores(series: pd.Series) -> pd.Series:
    """Compute robust z-scores using median and MAD."""
    median = series.median()
    mad = np.median(np.abs(series - median))

    if mad == 0:
        return pd.Series([0.0] * len(series), index=series.index)

    return 0.6745 * (series - median) / mad


def detect_outliers(df: pd.DataFrame, column: str, threshold: float = 3.5) -> pd.DataFrame:
    """Return rows whose robust z-score exceeds threshold."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataframe.")

    result = df.copy()
    result["robust_z"] = robust_z_scores(result[column])
    return result[result["robust_z"].abs() > threshold]
