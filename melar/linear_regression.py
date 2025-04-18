import json

import numpy as np

import melar.cfuncs as cfuncs


class LinearRegression:
    """Linear regression using gradient descent.

    This class functions as an all-in-one object for linear regression using gradient descent.
    Each instance of this class is a fully functioning linear regression model.
    This class is designed to be used with numpy arrays, pandas DataFrames, and pandas Series.


    Args:
        initial_weights: Initial weights of the model. If None, random weights are generated.
        initial_bias: Initial bias of the model. Default is a random float between -1 and 1.
        weights_amount: Amount of weights to generate. Default is 1.
        cost_function: Cost function to be used. Default is Mean Squared Error.
        cost_function_deriv: Derivative of the cost function. Default is the derivative of Mean Squared Error.
    """

    __slots__ = ['weights', 'bias', '_cost_function', '_cost_function_deriv']

    def __init__(self, initial_weights: np.ndarray | np.float64 | float = None,
                 initial_bias: np.float64 | float = np.random.uniform(-1, 1), weights_amount: int = 1,
                 cost_function=cfuncs.mse,
                 cost_function_deriv=cfuncs.mse_deriv) -> None:
        """Initializes the LinearRegression model with the given parameters.

        Args:
            initial_weights (np.ndarray | np.float64 | float, optional): Initial weights for the model. Defaults to None.
            initial_bias (np.float64 | float, optional): Initial bias for the model. Defaults to a random value between -1 and 1.
            weights_amount (int, optional): Number of weights. Defaults to 1.
            cost_function (callable, optional): Cost function to be minimized. Defaults to cfuncs.mse.
            cost_function_deriv (callable, optional): Derivative of the cost function. Defaults to cfuncs.mse_deriv.
        """

        if weights_amount < 1:
            raise ValueError("weights_amount has to be 1 or more")

        self.bias = initial_bias
        """np.float64: Bias of the model instance. Default is a random float between -1 and 1.
        """

        self._cost_function = cost_function
        self._cost_function_deriv = cost_function_deriv
        if initial_weights is None:
            self.weights = np.random.uniform(low=-1, high=1, size=weights_amount)
            """np.float64 or np.ndarray: Weights of the model instance. If there is only one weight, it is a float; otherwise, it is an array.
            """
            # Prevents error from happening when you have one weight because
            # np.dot will not accept arrays of different shapes, but it does accept scalars.
            if weights_amount == 1:
                self.weights = self.weights[0]

        else:
            self.weights = initial_weights

    def __repr__(self):
        """Returns a string representation of the LinearRegression model.

        The representation includes the bias and weights of the model.

        Returns:
            str: String representation of the model.
        """
        return f"{self.__class__.__name__}(bias={self.bias}, weights={self.weights})"

    def save(self, filename: str):
        save_data = {
            "weights": self.weights.tolist(),
            "bias": float(self.bias)
        }
        with open(filename, "w") as file:
            json.dump(save_data, file)

    def load(self, filename: str):
        """Loads model

        Args:
            filename (str): Filename
        """
        with open(filename, "r") as file:
            loaded_data = json.load(file)
        loaded_data = json.loads(loaded_data)
        self.weights = np.array(loaded_data["weights"])
        self.bias = np.float32(loaded_data["bias"])

    def np_predict(self, x: np.ndarray) -> np.float64 | np.ndarray:
        """Predict using the linear model.

        This is a version of predict that only accepts numpy arrays.
        This is ever so slightly faster for regular use.
        Regular predict is also compatible with numpy.

        Args:
            x (np.ndarray): Input value(s) to be predicted.

        Returns:
            (np.float64 | np.ndarray): Predicted values.
        """

        predictions = self.bias + np.dot(self.weights, x)
        return predictions  # this returns an int or a float

    def predict(self, x):
        """Predict using the linear model.

        Args:
            x (np.ndarray | pd.DataFrame | pd.Series): Input value(s) to be predicted.

        Returns:
            (np.float64 | np.ndarray | pd.DataFrame | pd.Series): Predicted values.
        """

        # If input is dataframe then it will return a dataframe
        if type(x).__name__ == "DataFrame":
            x = x.T
            predictions = self.bias + np.dot(self.weights, x)
            return x.__class__(predictions.T)
        # If input is series then it will return a series
        if type(x).__name__ == "Series":
            predictions = self.bias + np.dot(self.weights, x)
            return x.__class__(predictions)

        predictions = self.bias + np.dot(self.weights, x)
        return predictions

    def __call__(self, x):
        """Predict using the linear model.

        Args:
            x (np.ndarray | pd.DataFrame | pd.Series): Input value(s) to be predicted.

        Returns:
            (np.float64 | np.ndarray | pd.DataFrame | pd.Series): Predicted values.

        Notes:
            This is a shorthand for self.predict(x)
        """
        return self.predict(x)

    def adjust(self, x_training: np.ndarray, y_training: np.ndarray, y_predict: np.ndarray,
               learning_rate: float) -> None:
        """Adjusts the weights and bias of the model using gradient descent.

        This method updates the model's weights and bias based on the training data,
        the predicted values, and the learning rate. It uses the derivative of the
        cost function to calculate the necessary adjustments.

        Args:
            x_training (np.ndarray): Training data.
            y_training (np.ndarray): Target values.
            y_predict (np.ndarray): Model-predicted values.
            learning_rate (float): Size of adjustment.
        """

        bias_derivative, weights_derivative = self._cost_function_deriv(x_training, y_training, y_predict)
        self.bias = self.bias - learning_rate * bias_derivative
        self.weights = self.weights - learning_rate * weights_derivative

    def train(self, x, y, learning_rate: float, generations: int,
              do_print: bool = False) -> None:
        """Trains the model.

        This method iteratively adjusts the model's weights and bias over a specified
        number of generations. It uses the training data and target values to minimize
        the cost function. Optionally, it can print the cost at each generation for easy tracking of progress.

        Args:
            x (np.ndarray | pd.DataFrame | pd.Series): Training data.
            y (np.ndarray | pd.DataFrame | pd.Series): Target values.
            learning_rate (float): Size of adjustment per generation.
            generations (int): Amount of times to adjust.
            do_print (bool): Whether to print the loss for every generation during training.
        """

        if type(x).__name__ == "DataFrame":
            x = np.array(x).T
        if type(y).__name__ == "DataFrame":
            y = np.array(y).T[0]

        if do_print:
            for current_generation in range(generations):
                predictions = self.np_predict(x)
                self.adjust(x, y, predictions, learning_rate)
                print(f"Gen: {current_generation}, Cost: {self._cost_function(predictions, y)}")

            print("Training Complete")
        else:
            for current_generation in range(generations):
                predictions = self.np_predict(x)
                self.adjust(x, y, predictions, learning_rate)
