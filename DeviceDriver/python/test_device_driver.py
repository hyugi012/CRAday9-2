from unittest import TestCase
from unittest.mock import Mock, patch

from DeviceDriver.python.application import Application
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver


class DeviceDriverTest(TestCase):
    def test_successful_read(self):
        mk = Mock()
        mk.read.side_effect = [1, 1, 1, 1, 1]
        driver = DeviceDriver(mk)

        driver.read(0x1)

        self.assertEqual(0x5, mk.read.call_count)

    def test_raise_exception_read(self):
        mk = Mock()
        driver = DeviceDriver(mk)

        mk.read.side_effect = [1, 2, 1, 1, 1]

        with self.assertRaises(Exception):
            driver.read(0xAB)

    def test_read_for_write(self):
        mk = Mock()
        driver = DeviceDriver(mk)
        mk.read.return_value = 0xFF
        driver.write(0xA, 0x1)

        self.assertEqual(mk.read.call_count, 1)

    def test_write_exception(self):
        mk = Mock()
        driver = DeviceDriver(mk)
        mk.read.return_value = 0xF0

        with self.assertRaises(Exception):
            driver.write(0xA, 0x1)

    def test_write_success(self):
        mk = Mock()
        driver = DeviceDriver(mk)
        mk.read.return_value = 0xFF

        self.assertIsNone(driver.write(0xA, 0x1))
