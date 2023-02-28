"""This class test the validator function,
    Please run The command line to run the test
    python -m pytest tests/testValidators.py
    """

import pytest
from app.utils.validators import validateInteger

class TestValidators:
    def testValid(self):
        validateInteger('argo', 10, 0, 20, 'min message', 'max message')

    def testTypeError(self):
        with pytest.raises(TypeError):
            validateInteger('argo', '10')

    def testValueError(self):
        with pytest.raises(ValueError):
            validateInteger('argo', 5, 7)

    def testMinMessage(self):
        with pytest.raises(ValueError) as ex:
            validateInteger('argo', argValue=10, minValue=50, custemMinMessage='TestoMin')
        assert str(ex.value) == 'TestoMin'

    def testMaxMessage(self):
        with pytest.raises(ValueError) as ex:
            validateInteger('argo', argValue=10, maxValue=5, custemMaxMessage='TestoMax')
        assert str(ex.value) == 'TestoMax'

    def testArgMinValuesInStdMesssage(self):
        with pytest.raises(ValueError) as ex:
            validateInteger('argo', 50, 100)
        assert str(50) in str(ex.value)
        assert str(100) in str(ex.value)


    def testArgMaxValueInStdMessage(self):
        with pytest.raises(ValueError) as ex:
            validateInteger('argo', argValue=10, minValue=5, maxValue=8)
        assert str(10) in str(ex.value)
        assert str(8) in str(ex.value)