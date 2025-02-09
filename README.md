<h1 align="center"> <br>
  <img src="https://raw.githubusercontent.com/DrSolidDevil/mlr-gd/main/logo.png" width="300">
  <br><br>This is the branch for the development of 0.3.0
  
</h1>
<h2>The main goal of this version is to improve documentation and reach community standards</h2>
<div id="badges" align="center">
<a href="https://pypi.org/project/mlr-gd/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/mlr-gd?label=PyPi%20downloads"></a>
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/DrSolidDevil/mlr-gd">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/mlr-gd">
<a href="https://github.com/DrSolidDevil/mlr-gd/blob/main/LICENSE"><img alt="PyPI - License" src="https://img.shields.io/pypi/l/mlr-gd"></a>
<img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/mlr-gd">
</div>





<br>
Multiple linear regression by gradient descent.
<br><br>
<h2>Installation</h2>

To install mlr-gd you can use [pip](https://pip.pypa.io):

```bash
$ python -m pip install mlr-gd
```

Alternatively, you can install it by cloning the [GitHub repository](https://github.com/DrSolidDevil/mlr-gd):
```bash
$ git clone https://github.com/DrSolidDevil/mlr-gd.git
$ cd mlr-gd
$ pip install .
```

<br>

To import the package into your script:  
```python
import melar
```

<br>
<br>
<h2>Example</h2>


```python
import numpy as np
import melar

# y = x1 + 0.5*x2
x = np.array([[1, 3, 5, 8], [1, 2, 3, 6]])
y = np.array([1.5, 4, 6.5, 11])

learning_rate = 0.01
generations = 100


model = melar.LinearRegression(weights_amount=2)
model.train(x, y, learning_rate, generations, do_print=True)
print(f"Weights: {model.weights}, Bias: {model.bias}")
```


```
Gen: 0, Cost: 95.4852602406095
Gen: 1, Cost: 5.593624864417041
Gen: 2, Cost: 0.3286224504551768
Gen: 3, Cost: 0.020244781001893267
...
Gen: 99, Cost: 0.0007438760098695897
Training Complete
Weights: [0.94643617 0.57630021], Bias: -0.003265101149422934
```
