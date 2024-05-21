"""
@Author  : Geekmister
@Date    : 2024/05/21 11:13
@MyHome  : https://github.com/geekmister
@Desc    : 
    Test case case of login.py
"""


# test_sample.py

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


if __name__ == '__main__':
    test_add()
    # Another way to run the test is to use pytest command in terminal, for example: pytest .\login.py