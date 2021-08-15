"""
Driver Manager Util using to:
- initialize Web Driver for Factory Util
@author by phat.le on Aug 13, 2021
"""
from core.driver_util.driver_util import Driver


class DriverManager:
    def start_driver(self, name="chrome"):
        return Driver().create_driver(name)
