from unittest import TestCase
from unittest.mock import Mock, patch
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver


class DeviceDriverTest(TestCase):
    def test_successful_read(self):
        hardware: FlashMemoryDevice = Mock()
        hardware.read.return_value = 0x5
        driver = DeviceDriver(hardware)

        self.assertEqual(0x5, driver.read(0xFF))

    def test_successful_write(self):
        hardware: FlashMemoryDevice = Mock()
        hardware.read.return_value = 0xFF
        driver = DeviceDriver(hardware)

        self.assertIsNone(driver.write(0x1, 0x1))
