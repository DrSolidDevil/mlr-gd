mlr-gd Quickstart
=================

Importing the Package
^^^^^^^^^^^^^^^^^^^^^

To import the package into your Python script:

.. code-block:: python

    import melar


About
^^^^^

The main component of mlr-gd is the :ref:`LinearRegression<linregmodule>` class. This class is a complete model with methods for training and predicting.
To use the class you initialize a new object assigned to a variable, optionally with arguments for configuring initial weights and biases, cost function and the amount of weights.


Example
^^^^^^^

Here is a quick example to demonstrate how to use mlr-gd:

.. code-block:: python

    import numpy as np
    import melar

    # Example data: y = x1 + 0.5*x2
    x = np.array([[1, 3, 5, 8], [1, 2, 3, 6]])
    y = np.array([1.5, 4, 6.5, 11])

    learning_rate = 0.01
    generations = 100

    model = melar.LinearRegression(weights_amount=2)
    model.train(x, y, learning_rate, generations, do_print=True)
    print(f"Weights: {model.weights}, Bias: {model.bias}")
