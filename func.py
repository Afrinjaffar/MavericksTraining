%%writefile test_mathfile.py

import pytest
def test_add():
    output=mathfile.add(2,3)
    assert output==5

def test_sub():
    output=mathfile.sub(4,3)
    assert output==1

def test_multiply():
    output=mathfile.multiply(2,3)
    assert output==6

    l = int(input("Length : "))
    w = int(input("Width : "))
    area = l * w
    perimeter = 2 * (l + w)
    print("Area of Rectangle : ", area)
    print("Perimeter of Rectangle : ", perimeter)

%%writefile rec.py
 def area(l,w):
     return l*w
 def perimeter(l,w)
     return 2*(l+w)

 import pytest
def test_area():
    output=pytest.area(2,3)
    assert output==6
def test_perimeter():
    output=pytest.perimeter(2,3)
    assert output==10


