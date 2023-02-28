""" This is a various validators, that validate number of int between Min and max"""


def validateInteger(argName, argValue, minValue=None,
                    maxValue=None, custemMinMessage=None, custemMaxMessage=None
                    ):
    """

    :param argName (str):
    :param argValue (obj):
    :param minValue (int):
    :param maxValue (int):
    :param custemMinMessage (str):
    :param custemMaxMessage (str):
    :return:
        None :  if no execptions

    :raises:
        TypeError : if ´argValue´ is not int
        ValueError : if ´argValue´ dose not satisfy the bounds
    """
    if not isinstance(argValue, int):
        raise TypeError(f'{argName} must be an integer!')

    if minValue is not None and argValue < minValue:
        if custemMinMessage is not None:
            raise ValueError(custemMinMessage)
        raise ValueError(f'{argValue} cannot be less than {minValue}')

    if maxValue is not None and argValue > maxValue:
        if custemMaxMessage is not None:
            raise ValueError(f'{custemMaxMessage}')
        raise ValueError(f'{argValue} cannot be greater than {maxValue}')