from hardware_interface import FlashMemoryDevice


class DeviceDriver:
    """
    This class is used by the operating system to interact with the hardware 'FlashMemoryDevice'.
    """

    def __init__(self, device: FlashMemoryDevice):
        """
        :type device: hardware_interface.FlashMemoryDevice
        """
        self.__device = device

    def write(self, address: int, data: int) -> None:
        # TODO: implement this method
        if self.__device.read(address) != 0xFF:
            raise Exception("WriteFailException")
        self.__device.write(address, data)
        return None

    def read(self, address: int) -> int:
        # TODO: implement this method
        value = self.__device.read(address)
        for i in range(5):
            if value != self.__device.read(address):
                raise Exception("Read Fail Exception")
        return value
