import unittest


class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        req = self.requests
        req.append(t)
        a = t - 3000
        while req[0] < a:
            req.pop(0)
        return len(req)


class TestRecentCounter(unittest.TestCase):
    """933. Number of Recent Calls."""

    def test_init(self):
        sol = RecentCounter()
        self.assertEqual(sol.requests, [])

    def test_RecentCounter(self):
        sol = RecentCounter()
        input = 1
        out = sol.ping(input)
        self.assertEqual(out, 1)

        input = 100
        out = sol.ping(input)
        self.assertEqual(out, 2)

        input = 3001
        out = sol.ping(input)
        self.assertEqual(out, 3)

        input = 3002
        out = sol.ping(input)
        self.assertEqual(out, 3)


if __name__ == '__main__':
    unittest.main()
