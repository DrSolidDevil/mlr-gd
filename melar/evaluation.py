import numpy as np
from melar.linear_regression import LinearRegression


def tss(y) -> np.float32:
    """Total sum of squares

    Args:
        y (np.ndarray | pd.DataFrame | pd.Series): Target values
    """
    if type(y).__name__ == "DataFrame":
        y = y.T
    return np.sum(np.square(y - np.mean(y)))

def rss(model: LinearRegression, x, y):
    """Residual Sum of Squares
        Args:
            model (LinearRegression): Model to be evaluated
            x (np.ndarray | pd.DataFrame | pd.Series): Input values
            y (np.ndarray | pd.DataFrame | pd.Series): Target values
    """
    if type(x).__name__ == "DataFrame":
        x = y.T
    if type(y).__name__ == "DataFrame":
        y = y.T
    return np.sum(np.square(y - model.predict(x)))


def r2_score(model: LinearRegression, x, y):
    """Calculate coefficient of determination for model.

    Args:
        model (LinearRegression): Model to be evaluated
        x (np.ndarray | pd.DataFrame | pd.Series): Input Values
        y (np.ndarray | pd.DataFrame | pd.Series): Target Values
    """
    return 1 - rss(model, x, y)/tss(y)













