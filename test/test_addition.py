from app.main import addition
import pytest

class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x
    
    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'find')

# content of test_class_demo.py
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 5

    def test_two(self):
        assert self.value == 11