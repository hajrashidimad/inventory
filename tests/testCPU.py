import pytest

from app.models.inventory import CPU, Storage, HDD, SSD

class TestCPU:

    def testCPU(self):
        cpu = CPU('TV', 'Samsung', 25, 10, 32, 'sTR4', 250)

        assert cpu.name == 'TV'
        assert cpu.manufacturer == 'Samsung'
        assert cpu.total == 25
        assert cpu.allocated == 10
        assert cpu.cores == 32
        assert cpu.socket == 'sTR4'
        assert cpu.powerWatt == 250


