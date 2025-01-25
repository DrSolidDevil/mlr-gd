import numpy as np

import melar.cfuncs as cfuncs


class LinearRegression:
    """Linear regression using gradient descent.

    LinearRegression trains a linear model with weights and a bias using gradient descent to minimize the cost function (MSE).
    """

    def __init__(self, initial_weights: np.ndarray | np.float64 | float = None,
                 initial_bias: np.float64 | float = np.random.uniform(-1, 1), weights_amount: int = 1,
                 cost_function=cfuncs.mse,
                 cost_function_deriv=cfuncs.mse_deriv) -> None:
        """
        Args:
            initial_weights: Initial weights of model, defaults to np.random.uniform(low=-1, high=1, size=weight_amount).
            initial_bias: Initial bias of model, defaults to np.random.uniform(-1, 1).
            weights_amount: How many weights the model has, defaults to 1.
            cost_function: cost function derivative (UPDATE THIS TO BETTER DESCRIPTION)
            cost_function_deriv: cost function derivative (UPDATE THIS TO BETTER DESCRIPTION)
        """  # noqa: D205, D212, D415

        self.bias = initial_bias
        self.cost_function = cost_function
        self.cost_function_deriv = cost_function_deriv
        if initial_weights is None:
            self.weights = np.random.uniform(low=-1, high=1, size=weights_amount)
            # Prevents error from happening when you have one weight because
            # np.dot will not accept arrays of different shapes, but it does accept scalars.
            if weights_amount == 1:
                self.weights = self.weights[0]
        else:
            #   if type(initial_weights).__name__ == "Series":
            self.weights = initial_weights

    def np_predict(self, x: np.ndarray) -> np.int64 | np.float64:
        """Predict using the linear model.

        This is a version of predict that only accepts numpy arrays.
        This is ever so slightly faster for regular use.
        Regular predict is also compatible with numpy.

        Args:
            x: Input value(s) to be predicted.

        Returns:
            Predicted values.
        """
        predictions = self.bias + np.dot(self.weights, x)  # dot product is the sum of w * x
        return predictions  # this returns an int or a float

    def predict(self, x) -> np.int64 | np.float64:
        """Predict using the linear model.

        Args:
            x: Input value(s) to be predicted. (np.ndarray/pd.DataFrame/pd.Series)

        Returns:
            Predicted values.
        """
        # If input is dataframe then it will return a dataframe
        if type(x).__name__ == "DataFrame":
            x = x.T
            predictions = self.bias + np.dot(self.weights, x)  # dot product is the sum of w * x
            return x.__class__(predictions.T)

        predictions = self.bias + np.dot(self.weights, x)  # dot product is the sum of w * x
        return predictions  # this returns an int or a float

    def adjust(self, x_training: np.ndarray, y_training: np.ndarray, y_predict: np.ndarray,
               learning_rate: float) -> None:
        """Adjusts the weights and bias of the model using gradient descent.

        Args:
            x_training: Training data.
            y_training: Target values.
            y_predict: Model-predicted values.
            learning_rate: Size of adjustment.
        """

        bias_derivative, weights_derivative = self.cost_function_deriv(x_training, y_training, y_predict)

        self.bias = self.bias - learning_rate * bias_derivative
        self.weights = self.weights - learning_rate * weights_derivative

    def train(self, x: np.ndarray, y: np.ndarray, learning_rate: float, generations: int,
              do_print: bool = False) -> None:
        """Trains the model.

        Args:
            x: Training data.
            y: Target values.
            learning_rate: Size of adjustment per generation.
            generations: Amount of times to adjust.
            do_print: Print loss for every generation.
        """

        # Checks if x and y are dataframes.
        # If so, it transposes them to be compatible with the adjust method.

        if type(x).__name__ == "DataFrame":
            x = np.array(x).T
        print("a", np.shape(x))
        if type(y).__name__ == "DataFrame":
            y = np.array(y).T

        if do_print:
            for current_generation in range(generations):
                predictions = self.np_predict(x)
                self.adjust(x, y, predictions, learning_rate)
                print(f"Gen: {current_generation}, Cost: {self.cost_function(predictions, y)}")

            print("Training Complete")
        else:
            for current_generation in range(generations):
                predictions = self.np_predict(x)
                self.adjust(x, y, predictions, learning_rate)
