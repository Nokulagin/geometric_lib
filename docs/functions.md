# Functions overview
## Circle (**`circle.py`**)

- **`area(r)`**

Calculates area of a circle using given radius r  
The formula used for calculations:  
S = πR²

**Arguments:**
- r (number type) : radius of a circle

**Return value:**
- area (number type) : area of a circle of radius r

**Example:**
```python
area(5) # returns 78.54
```

- **`perimeter(r)`**

Calculates perimeter of a circle using given radius r  
The formula used for calculations:  
P = 2πR

**Arguments:**
- r (number type) : radius of a circle

**Return value:**
- perimeter (number type) : perimeter of a circle of radius r

**Example:**
```python
perimeter(5) # returns 15.71
```

## Rectangle (**`rectangle.py`**)

- **`area(a, b)`**

Calculates area of a rectangle using given side lengths a and b  
The formula used for calculations:  
S = ab

**Arguments:**
- a (number type) : side length of a rectangle
- b (number type) : side length of a rectangle

**Return value:**
- area (number type) : area of the rectangle with side lengths a and b

**Example:**
```python
area(5, 2) # returns 10
```

- **`perimeter(a, b)`**

Calculates perimeter of a rectangle using given side lengths a and b  
The formula used for calculations:  
P = 2(a + b)

**Arguments:**
- a (number type) : side length of a rectangle
- b (number type) : side length of a rectangle

**Return value:**
- perimeter (number type) : perimeter of the rectangle with side lengths a and b

**Example:**
```python
perimeter(5, 2) # returns 14
```

## Square (**`square.py`**)

- **`area(a)`**

Calculates area of a square using given side length a  
The formula used for calculations:  
S = a²

**Arguments:**
- a (number type) : side length of a square

**Return value:**
- area (number type) : area of the square with side length a

**Example:**
```python
area(5) # returns 25
```

- **`perimeter(a)`**

Calculates perimeter of a square using given side length a  
The formula used for calculations:  
P = 4a

**Arguments:**
- a (number type) : side length of a square

**Return value:**
- perimeter (number type) : perimeter of the square with side length a

**Example:**
```python
perimeter(5) # returns 20
```

## Triangle (**`triangle.py`**)

- **`area(a, h)`**

Calculates area of a triangle using given base length a and height length h  
The formula used for calculations:  
S = ah/2

**Arguments:**
- a (number type) : base length of a triangle
- h (number type) : height length of a triangle

**Return value:**
- area (number type) : area of the triangle with base length a and height length h

**Example:**
```python
area(5, 2) # returns 5
```

- **`perimeter(a, b, c)`**

Calculates perimeter of a triangle using given side lengths a, b, c  
The formula used for calculations:  
P = a + b + c

**Arguments:**
- a (number type) : side length of a triangle
- b (number type) : side length of a triangle
- c (number type) : side length of a triangle

**Return value:**
- perimeter (number type) : perimeter of the triangle with side lengths a, b, c

**Example:**
```python
perimeter(5, 2, 4) # returns 11
```