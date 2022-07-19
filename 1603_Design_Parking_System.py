"""
1603. Design Parking System from Leetcode.

Design a parking system for a parking lot.
The parking lot has three kinds of parking spaces:
big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes
object of the ParkingSystem class. The number of slots for
each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space
of carType for the car that wants to get into the parking lot.
carType can be of three kinds: big, medium, or small, which are
represented by 1, 2, and 3 respectively. A car can only park in a
parking space of its carType. If there is no space available,
return false, else park the car in that size space and return true.
"""


class ParkingSystem:
    """Design Parking System Class."""

    def __init__(self, big: int, medium: int, small: int):
        """Initialise number of spaces in the parking lot.."""
        # self.__big = big
        # self.__medium = medium
        # self.__small = small
        self.parking = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        """Design Parking System Function."""
        # My initial but slow one.
        # if carType == 1 and self.__big != 0:
        #     self.__big -= 1
        #     return True
        # elif carType == 2 and self.__medium != 0:
        #     self.__medium -= 1
        #     return True
        # elif carType == 3 and self.__small != 0:
        #     self.__medium -= 1
        #     return True

        # return False

        # # Second one:
        # if self.parking[carType-1] == 0:
        #     return False
        # else:
        #     self.parking[carType-1] -= 1
        #     return True

        # Even faster:
        if self.parking[carType-1] > 0:
            self.parking[carType-1] -= 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


def main():
    """Solution."""
    nr_of_cars_in_the_lot = ParkingSystem(1, 1, 1)
    answer = nr_of_cars_in_the_lot.addCar(1)
    print(answer)
    answer = nr_of_cars_in_the_lot.addCar(1)
    print(answer)


if __name__ == "__main__":
    main()
