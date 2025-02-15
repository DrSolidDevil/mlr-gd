"""cfuncs contains all standard cost functions integrated into mlr-gd and melar.

Each cost function has a name (ex. mse) that returns a cost.
Each cost function has a derivative function, indicated by _deriv
"""
import numpy as np


def mse(y_predictions: np.ndarray, y_target: np.ndarray) -> np.float64:
    """MSE Function.

    Calculates the mean square error of predictions as compared to the target values.

    Args:
        y_predictions (np.ndarray): Predicted values.
        y_target (np.ndarray): Target values.

    Returns:
        np.float64: Mean of the squared remainder array (y_predictions - y_target)
    """

    if y_predictions.size != y_target.size:
        raise ValueError("Both arrays have to be the same length.")

    cost = np.mean((y_predictions - y_target) ** 2)

    return cost


def mse_deriv(x_training: np.ndarray, y_training: np.ndarray, y_predict: np.ndarray) -> tuple:
    """Derivative of mse

    Args:
        x_training (np.ndarray): Input values.
        y_training (np.ndarray): Target values.
        y_predict (np.ndarray): Predicted values.

    Returns:
          tuple (np.float64, np.ndarray): Derivative of cost function mse (bias_derivative, weights_derivative)
    """
    y_difference = y_training - y_predict
    bias_derivative = -2 * np.mean(y_difference)

    # Basically same math as simple linear regression but with the corresponding x of that weight.
    weights_derivative = -2 * np.dot(y_difference, x_training.T) / len(y_training)

    return bias_derivative, weights_derivative


def mae(y_predictions: np.ndarray, y_target: np.ndarray) -> np.float64:
    """MAE Function.

    Calculates the mean absolute error of predictions as compared to the target values.

    Args:
        y_predictions (np.ndarray): Predicted values.
        y_target (np.ndarray): Target values.

    Returns:
        np.float64: Mean of the absolute remainder array (y_predictions - y_target)
    """

    if y_predictions.size != y_target.size:
        raise ValueError("Both arrays have to be the same length.")

    cost = np.mean(np.abs(y_predictions - y_target))

    return cost


def mae_deriv(x_training: np.ndarray, y_training: np.ndarray, y_predict: np.ndarray) -> tuple:
    """Derivative of mae

    Args:
        x_training (np.ndarray): Input values.
        y_training (np.ndarray): Target values.
        y_predict (np.ndarray): Predicted values.

    Returns:
        tuple (np.float64, np.ndarray): Derivative of cost function mae (bias_derivative, weights_derivative)
    """

    y_difference_sign = np.sign(y_training - y_predict)
    bias_derivative = -1 * np.mean(y_difference_sign)

    weights_derivative = -1 * np.dot(y_difference_sign, x_training.T) / len(y_training)

    return bias_derivative, weights_derivative


# All cost functions that cfuncs has.
C_FUNCTIONS: tuple = (mse, mae)
# All derivative cost function that cfuncs has, (They have to have the same index as its cost function)
C_FUNCTIONS_D: tuple = (mse_deriv, mae_deriv)
