import pytest

from app.models.inventory import Resources

class TestResource:

    def testResource(self):
        resource = Resources('TV', 'Samsung', 25, 10)

        assert resource.name == 'TV'
        assert resource.manufacturer == 'Samsung'
        assert resource.total == 25
        assert resource.allocated == 10


    def testSTR(self):
        resource = Resources('TV', 'Samsung', 25, 10)

        assert resource.__str__() == resource.name


    def testREPR(self):
        resource = Resources('TV', 'Samsung', 25, 10)

        assert resource.__repr__() == f'The name is {resource.name},' \
                                      f' Manufactured by :{resource.manufacturer} The total is {resource.total},' \
                                      f' {resource.allocated}PCS are disponible.'

    def testAvailble(self):
        resource = Resources('TV', 'Samsung', 25, 10)

        assert resource.availble() == (resource.total - resource.allocated)


    def testClaim(self):
        resource = Resources('TV', 'Samsung', 25, 10)
        n = 5
        totalAllocated = resource.allocated
        resource.claim(n)

        assert resource.allocated == totalAllocated + n


    def testFreeup(self):
        resource = Resources('TV', 'Samsung', 25, 10)
        n = 5
        totalAllocated = resource.allocated
        resource.freeUp(n)

        assert resource.allocated == totalAllocated - n


    def testdied(self):
        resource = Resources('TV', 'Samsung', 25, 10)
        n = 5
        totalAllocated = resource.allocated
        total = resource.total
        resource.died(n)

        assert resource.allocated == totalAllocated - n
        assert resource.total == total - n


    def testPurchaised(self):
        resource = Resources('TV', 'Samsung', 25, 10)
        n = 5
        total = resource.total
        resource.purchased(n)


        assert resource.total == total + n


    def testcategory(self):
        resource = Resources('TV', 'Samsung', 25, 10)
        assert resource.category() == str(resource.__class__.__name__.lower())