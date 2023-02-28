"""
This class is the reference to all Total invetory exsiste
"""

from app.utils.validators import validateInteger


class Resources:
    """
    The total qty for all resource
    """

    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer

        validateInteger(name, total, minValue=0)
        self._total = total

        validateInteger(name, allocated, maxValue=total)
        self._allocated = allocated

    @property
    def name(self):
        """

        :return:
            str : The name of piece
        """
        return self._name

    @property
    def manufacturer(self):
        """

        :return:
            str : The name of manufacturer
        """

        return self._manufacturer

    @property
    def total(self):
        """

        :param self:
        :return:
            int : number of pieces
        """
        return self._total

    @property
    def allocated(self):
        """

        :param self:
        :return:
            int : number of pieces alrady uses
        """
        return self._allocated

    def __str__(self):
        """

        :param self:
        :return:
            str : The name of Piece
        """
        return self.name

    def __repr__(self):
        """

        :param self:
        :return:
            str : summury about product.
        """
        return f'The name is {self.name}, Manufactured by :{self.manufacturer} The total is {self.total},' \
               f' {self.allocated}PCS are disponible.'

    def availble(self):
        """

        :return:
            int : The number of Pieces availble on pool
        """
        return (self.total - self.allocated)

    def claim(self, n):
        """
        This function take the qty from the pool
        :param n:
        :return:
            None : if qty availble on pool
        """
        validateInteger('num', argValue=n, minValue=1, maxValue=self.availble(), custemMaxMessage='The quantity  dose not availble')
        self._allocated += n



    def freeUp(self, n):
        """
        method to return n resources to the pool (e.g. disassembled some builds)
        :param n:
        :return:
            None : add n to pool
        """
        validateInteger('num', n, minValue=1, maxValue=self._allocated, custemMaxMessage='Cannot return more than allocated' )
        self._allocated -= n


    def died(self, n):
        """
        method to return and permanently remove inventory from the pool (e.g. they broke something) -
        as long as total available allows it
        :param n:
        :return:
            None :  if n removed from pool
        """
        validateInteger('num', n, 1, self.allocated, custemMaxMessage='Cannot be greater than total')
        self._total -= n
        self._allocated -= n


    def purchased(self, n):
        """
        method to add inventory to the pool (e.g. they purchased a new CPU)
        :param n:
        :return:
            None : if good values were purchsed
        """
        validateInteger(self, n, 1)
        self._total += n


    def category(self):
        """
        computed property that returns a lower case version of the class name
        :return:
            str : as a lower case
        """

        return  str(self.__class__.__name__.lower())











class CPU(Resources):
    """
    This is a child class from Resources
    """

    def __init__(self, name, manufacturer, total, allocated, cores, sockets, powerWatts):
        super().__init__(name, manufacturer, total, allocated)
        validateInteger('Cores', cores, 1)
        validateInteger('PwerWatt', powerWatts, 1)
        self._cores = cores
        self._sockets = sockets
        self._powerWatts = powerWatts

    @property
    def cores(self):
        """

        :param self:
        :return:
        """
        return self._cores

    @property
    def socket(self):
        """

        :return:
        """

        return self._sockets


    @property
    def powerWatt(self):
        """

        :return:
        """
        return self._powerWatts






class Storage(Resources):

    def __init__(self, name, manufacturer, total, allocated, capacityGB):
        """

        :param name:
        :param manufacturer:
        :param total:
        :param allocated:
        :param capacityGB:
        """
        super().__init__(name, manufacturer, total, allocated)
        validateInteger('capacityGB', capacityGB, 1)
        self._capacityGB = capacityGB


    @property
    def capacityGB(self):
        """

        :return:
        """
        return self._capacityGB

    def __repr__(self):
        """

        :return:

        """
        return f'{self.category()}: {self.capacityGB}'




class HDD(Storage):
    """
    """
    def __init__(self, capacityGB, size, rpm):
        super().__init__(capacityGB)
        self._size = size
        self._rpm = rpm


    @property
    def size(self):
        """

        :return:
        """
        return  self._size

    @property
    def rpm(self):
        """

        :return:
        """
        return  self._rpm


    def __repr__(self):
        """

        :return:
        """

        return self._size, self._rpm


class SSD(Storage):
    """
    """

    def __init__(self, capacityGB, interface):
        super().__init__(capacityGB)
        self._interface = interface

    @property
    def interface(self):
        """

        :return:
        """
        return self._interface

    def __repr__(self):
        """

        :return:
        """
        return self._interface










monitor = Resources('TV', 'Samsung', 10, 3)
print(monitor.name)
print(monitor.manufacturer)
print(monitor.total)
print(monitor.allocated)
print(monitor.__str__())
print(monitor.__repr__())
print(monitor.availble())

print(monitor.category())
print(monitor.claim(1))