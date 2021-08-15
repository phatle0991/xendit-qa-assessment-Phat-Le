"""
Factory Util using support Browser Util:
- initialize Web Driver (we support initialize multiple Driver, separately by key)
- get Web Driver
- Web Driver actions: Close All Driver, Switch Drive
@author by phat.le on Aug 13, 2021
"""
from core.driver_util.driver_manager import DriverManager

__driver = {}


def start_driver(name, driver_key="default"):
    driver = DriverManager().start_driver(name)
    __driver[driver_key] = driver
    Key.current = driver_key


def get_driver():
    try:
        return __driver[Key.current]
    except:
        return None


def close_all_driver():
    for key in __driver:
        __driver[key].quit()
    __driver.clear()


def switch_to_driver(driver_key="default"):
    Key.current = driver_key


class Key:
    current = "default"
