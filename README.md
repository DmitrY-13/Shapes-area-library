# Shapes area library for Mindbox's questionnaire

## What does the package contain?
* `Shape` abstract class 
* `Circle` class
* `Triangle` class
* `PyTest` tests

## How to use?
* `Circle`:

    You can create instance of `Circle` class by passing `radius` parameter to its constructor.
    By accessing `area` property you will get area of created instance.
    ```python
    from shapes_area import Circle
    
    circle = Circle(10)

    print(circle.area) # Result: 314.1592653589793
    ```

* `Triangle`:

    You can create instance of `Triangle` class by passing `a`, `b`, `c` parameters to its constructor.
    By accessing `area` property you will get area of created instance.
    You also can call `is_right` method to find out if triangle is right-angled.
    ```python
    from shapes_area import Triangle
    
    triangle = Triangle(3, 4, 5)

    print(triangle.area) # Result: 6.0
    print(triangle.is_right()) # Result: True
    ```
    Method `is_right` also contains `acceptable_error` parameter,
    which is needed if sides of triangle have large fractional part,
    in it, you can specify acceptable error.

## How to create shape?
* Import `Shape` class from `shape_area`
* Inherit your class from `Shape` class
* Override `area` property

Example:
```python
from typing import override

from shapes_area import Shape


class YourShape(Shape):
    def __init__(self):
        # your realisation
        pass
    
    @property
    @override
    def area(self) -> int | float:
        # your realisation
        pass

```

## How to run tests?
* Install `requirements`:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
* Run `PyTest`:
    ```bash
    pytest
    ```