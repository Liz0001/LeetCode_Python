"""
2469. Convert the Temperature.

You are given a non-negative floating point number rounded to two decimal
places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it
as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the
actual answer will be accepted.
"""
from typing import List


class Solution:
    """Convert the Temperature."""

    def convertTemperature(self, celsius: float) -> List[float]:
        """Convert the Temperature."""
        return [(celsius + 273.15), (celsius * 1.80 + 32.00)]


def main():
    """Solution."""
    solution = Solution()
    nums = 36.5
    answer = solution.convertTemperature(nums)
    print(answer)


if __name__ == "__main__":
    main()
