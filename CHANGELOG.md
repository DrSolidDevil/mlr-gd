# Changelog

## [0.3.0](https://github.com/DrSolidDevil/mlr-gd/releases/tag/v0.3.0) (2025-02-15)

### Added
* Detailed documentation with hosting on readthedocs.io
* Github action for running tests before push to main branch.
* Issue template for bug reports and enhancement suggestions.
* Pull-request template.

### Documentation
* Created contribution guidelines
* Created security policy
* Created code of conduct
* Created changelog
* Created release template
* Created release checklist

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
