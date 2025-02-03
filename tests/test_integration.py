import numpy as np
import pytest

import melar

# This file runs integration tests of the model with cost functions


COST_FUNCTIONS = melar.cfuncs.C_FUNCTIONS
COST_FUNCTIONS_DERIVATIVE = melar.cfuncs.C_FUNCTIONS_D

# Standard amount of iterations to run each test function
STD_ITER = 5


# Standard learning rate, the more weights the lower this should be.
# For STD_ITER = 5 the learning rate should be around 0.01
# For STD_ITER = 10 the learning rate should be around 0.001
@pytest.fixture
def std_lrate():
    return 0.01


# Standard amount of generations
@pytest.fixture
def std_gens():
    return 10


# Standard array length
@pytest.fixture
def std_arrlen():
    return 5


def std_t_params_func(start):
    """Creates the standard parameters for testing the model

    Args:
        start: How many weights to start with.

    Returns:
        A list of tuples for pytest.mark.parametrize to use when running standard tests.
        The tuples are made up of an integer for how many weights the iteration should have
        and the index (of C_FUNCTIONS and C_FUNCTIONS_D) of the cost function to be used.

    """

    params = []
    f_len = len(COST_FUNCTIONS)
    ids = COST_FUNCTIONS
    ids = [i.__name__ for i in ids]
    ids = np.repeat(ids, STD_ITER - start + 1)

    for i in range(f_len):
        for j in range(start, STD_ITER + 1):
            params.append((j, i))
    print(params)
    return params, ids


# starts with 1 weight
std_t_params_1, std_t_cf_ids_1 = std_t_params_func(1)
# starts with 2 weights
std_t_params_2, std_t_cf_ids_2 = std_t_params_func(2)


@pytest.mark.parametrize("weights_amount, cost_funcs_index", std_t_params_1, ids=std_t_cf_ids_1)
def test_0weights_0bias(std_lrate, std_gens, std_arrlen, weights_amount, cost_funcs_index):
    """Tests "null model" (y = 0*x1 + 0*x2 +0), this should give weights and bias close to 0.
    """

    # creates array of input values
    x = []

    for i in range(weights_amount):
        x.append([j + i for j in list(range(std_arrlen))])

    x = np.array(x)
    y = np.zeros(std_arrlen, dtype=int)
    model = melar.LinearRegression(weights_amount=weights_amount, cost_function=COST_FUNCTIONS[cost_funcs_index],
                                   cost_function_deriv=COST_FUNCTIONS_DERIVATIVE[cost_funcs_index])
    model.train(x, y, std_lrate, std_gens)
    # Check if all weights are less than +/- 2  if it's bigger then there is probably a problem with the code.
    assert np.all(np.abs(model.weights) < 2)
    assert abs(model.bias) < 2


@pytest.mark.parametrize("weights_amount, cost_funcs_index", std_t_params_1, ids=std_t_cf_ids_1)
def test_1weights_0bias(std_lrate, std_gens, std_arrlen, weights_amount, cost_funcs_index):
    """Tests model with weights that are 1 (y = 0*x1 + 0*x2 +0), this should give weights to 1.
    """

    # creates array of input values
    x = []

    for i in range(weights_amount):
        x.append([j + i for j in list(range(std_arrlen))])

    x = np.array(x)
    y = np.sum(x, axis=0)
    print(y)
    model = melar.LinearRegression(weights_amount=weights_amount, cost_function=COST_FUNCTIONS[cost_funcs_index],
                                   cost_function_deriv=COST_FUNCTIONS_DERIVATIVE[cost_funcs_index])
    model.train(x, y, std_lrate, std_gens)
    # The target weights are 1 and the target bias is 0
    # Check if all weights are less than 2.5  
    # If it's bigger than that there is probably a problem with the code.
    assert np.all(model.weights < 2.5)
    assert np.all(model.weights > -1)
    assert abs(model.bias) < 2
