# Changelog


## 0.3.0 (DATE)

### Added
* LIST OF ADDED FEATURES

### Changed
* LIST OF CHANGES TO EXISTING FUNCTIONALITY

### Deprecated
* LIST OF SOON-TO-BE DEPRECATIONS

### Removed
* LIST OF REMOVED FEATURES

### Fixed
* LIST OF BUG FIXES

### Security
* LIST OF FIXED VULNERABILITIES

### Documentation
* LIST OF DOCUMENTATION CHANGES

<br>

## [0.2.1](https://github.com/DrSolidDevil/mlr-gd/releases/tag/v0.2.1) (2025-02-05)

### Added
* Ability to use cost function other than mean squared error (including custom ones)
* Mean absolute error added as new cost function.
* Compatability with pandas (DataFrame & Series).
* Added testing with pytest.
* Added \_\_slots\_\_ and \_\_repr\_\_ to melar.LinearRegression

### Changed
* Cost functions have been moved from melar/main.py to melar/cfuncs.py
*  Additional keyword arguments ``cost_function`` and ``cost_function_deriv`` to melar.LinearRegression.

### Documentation
* Added docstrings to melar/\_\_init\_\_.py, melar/main.py and melar/cfuncs.py
* Added module level dunders to melar/\_\_init\_\_.py

<br>

## [0.1.2](https://github.com/DrSolidDevil/mlr-gd/releases/tag/v0.1.2) (2025-01-12)

### Fixed
* \_\_init\_\_.py could not import ``LinearRegression``.

### Documentation
* Added example code to README.md
