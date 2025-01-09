import numpy as np


class LinearRegression:
    """Linear regression using gradient descent.

    LinearRegression trains a linear model with weights and a bias using gradient descent to minimize the cost function (MSE).
    """

    def __init__(self, initial_weights: np.ndarray = None,
                 initial_bias: float = np.random.uniform(-1, 1), weights_amount: int = 1) -> None:
        """
        Args:
            initial_weights: Initial weights of model, defaults to np.random.uniform(low=-1, high=1, size=weight_amount).
            initial_bias: Initial bias of model, defaults to np.random.uniform(-1, 1).
            weights_amount: How many weights the model has, defaults to 1.
        """  # noqa: D205, D212, D415

        self.bias = initial_bias
        if initial_weights is None:
            self.weights = np.random.uniform(low=-1, high=1, size=weights_amount)
        else:
            self.weights = initial_weights

    def predict(self, x: np.ndarray) -> np.ndarray:
        """Predict using the linear model.

        Args:
            x: Input value(s) to be predicted.

        Returns:
            Predicted values.
        """

        predictions = self.bias + np.dot(self.weights, x)
        return predictions

    @staticmethod
    def cost(y_predictions: np.ndarray, y_target: np.ndarray) -> float:

        """MSE Function.

        Calculates the mean square error of predictions as compared to the target values.
        Args:
            y_predictions: Predicted values.
            y_target: Target values.

        Returns:
            Mean of the squared remainder array (y_predictions - y_target)
        """

        if y_predictions.size != y_target.size:
            raise ValueError("Both arrays have to be the same length.")

        return np.mean((y_predictions - y_target) ** 2)

    def adjust(self, x_training: np.ndarray, y_training: np.ndarray, y_predict: np.ndarray,
               learning_rate: float) -> None:
        """Adjusts the weights and bias of the model using gradient descent.

        Args:
            x_training: Training data.
            y_training: Target values.
            y_predict: Model-predicted values.
            learning_rate: Size of adjustment.
        """

        y_difference = y_training - y_predict
        bias_derivative = -2 * np.mean(y_difference)

        # Basically same math as simple linear regression but with the corresponding x of that weight.
        weights_derivative = -2 * np.dot(y_difference, x_training.T) / len(y_training)

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

        if do_print is True:
            for current_generation in range(generations):
                predictions = self.predict(x)
                self.adjust(x, y, predictions, learning_rate)
                print(f"Gen: {current_generation}, Cost: {self.cost(predictions, y)}")

            print("Training Complete")

        else:
            for current_generation in range(generations):
                predictions = self.predict(x)
                self.adjust(x, y, predictions, learning_rate)


# test
