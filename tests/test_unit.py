import numpy as np
import pytest
import pandas as pd

import melar


def test_cfuncs_same_len_cf_cfd():
    """Checks that C_FUNCTIONS and C_FUNCTIONS_D are the same length.
    """
    assert len(melar.cfuncs.C_FUNCTIONS) == len(melar.cfuncs.C_FUNCTIONS_D)


def test_cfuncs_same_order_cf_cfd():
    """Checks that all index of C_FUNCTIONS has the same values + _deriv as the same index of C_FUNCTIONS_D.
    """
    r = range(len(melar.cfuncs.C_FUNCTIONS))
    for i in r:
        assert melar.cfuncs.C_FUNCTIONS[i].__name__ + "_deriv" == melar.cfuncs.C_FUNCTIONS_D[i].__name__


def test_weights_amount_default():
    """Checks that if there are no set amount of model weights then there is only one model weight which is a np.float64 (if it's float then it is one weight)
    """
    model = melar.LinearRegression()
    assert isinstance(model.weights, np.float64)


def test_initial_weights_bias():
    """Checks that if inital_weights and inital_bias are set then the weight and bias is that (before training).
    """
    model = melar.LinearRegression(initial_weights=1.0, initial_bias=1.0)
    assert model.weights == 1.0
    assert model.bias == 1.0


def test_weights_amount_0():
    """Checks that if the weights_amount is set to 0 then it gets a value error.
    """
    with pytest.raises(ValueError):
        melar.LinearRegression(weights_amount=0)


def test_set_cost_function():
    """Checks if you can set the cost_function and the cost_function_deriv
    """
    # Uses string for simplicity because the specific function is not actually used in this test.
    model = melar.LinearRegression(cost_function='test', cost_function_deriv='test_deriv')
    assert model.cost_function == 'test'
    assert model.cost_function_deriv == 'test_deriv'
    
@pytest.mark.pandastest
def test_predict_return_dataframe():
    """Checks if you get a dataframe as a return when inputing a dataframe into LinearRegression.predict
    """
    model = melar.LinearRegression()
    df = pd.DataFrame([0])
    prediction = model.predict(df)
    assert type(prediction).__name__ == "DataFrame"

@pytest.mark.pandastest
def test_predict_return_series():
    """Checks if you get a series as a return when inputing a series into LinearRegression.predict
    """
    model = melar.LinearRegression()
    ser = pd.Series([0])
    prediction = model.predict(ser)
    assert type(prediction).__name__ == "Series"
