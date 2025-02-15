Cost functions
===============


    In mathematical optimization and decision theory, a loss function or cost function
    (sometimes also called an error function) is a function that maps an event or values
    of one or more variables onto a real number intuitively representing some "cost"
    associated with the event.

    \- `Wikipedia <Wikipedia: https://en.wikipedia.org/wiki/loss_function>`_

|

Cost functions for mlr-gd are regular Python functions that take target values and predicted values as parameters and return a cost.

To be used with gradient descent, these functions must also have a corresponding derivative function.
This derivative function takes an additional parameter—the input values—and returns the partial derivatives for both the bias and the weights.

Template
^^^^^^^^

.. code-block:: python

    def cost_function(y_predictions: np.ndarray, y_target: np.ndarray) -> np.float64:
        """[Name/Short description]

        [Long description]

        Args:
           y_predictions (np.ndarray): Predicted values.
            y_target (np.ndarray): Target values.

         Returns:
            np.float64: [Description of return]
        """

        # Put your cost code here

        return cost


.. code-block:: python

    def cost_function_deriv(x_training: np.ndarray, y_training: np.ndarray,
                            y_predict: np.ndarray) -> tuple:
        """[name/short description]

        [Long description (optional)]
        Args:
            x_training (np.ndarray): Input values.
            y_training (np.ndarray): Target values.
            y_predict (np.ndarray): Predicted values.

        Returns:
            tuple (np.float64, np.ndarray): [Description of return]
        """

        # Put your derivative cost code here

        return bias_derivative, weights_derivative

