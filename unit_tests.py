import unittest
from poisson_distro import attackerSuccessProbability

class PoissonDistroTests(unittest.TestCase):
    def test_poisson_distribution_1(self):
        """
        When q=0.1
        """
        q=0.1
        self.assertEqual(float(format(attackerSuccessProbability(q, 0), '.7f')), 1.0000000)
        self.assertEqual(float(format(attackerSuccessProbability(q, 1), '.7f')), 0.2045873)
        self.assertEqual(float(format(attackerSuccessProbability(q, 2), '.7f')), 0.0509779)
        self.assertEqual(float(format(attackerSuccessProbability(q, 3), '.7f')), 0.0131722)
        self.assertEqual(float(format(attackerSuccessProbability(q, 4), '.7f')), 0.0034552)
        self.assertEqual(float(format(attackerSuccessProbability(q, 7), '.7f')), 0.0000647)
        self.assertEqual(float(format(attackerSuccessProbability(q, 10), '.7f')), 0.0000012)

    def test_poisson_distribution_2(self):
        """
        When q=0.3
        """
        q=0.3
        self.assertEqual(float(format(attackerSuccessProbability(q, 0), '.7f')), 1.0000000)
        self.assertEqual(float(format(attackerSuccessProbability(q, 5), '.7f')), 0.1773523)
        self.assertEqual(float(format(attackerSuccessProbability(q, 10), '.7f')), 0.0416605)
        self.assertEqual(float(format(attackerSuccessProbability(q, 15), '.7f')), 0.0101008)
        self.assertEqual(float(format(attackerSuccessProbability(q, 20), '.7f')), 0.0024804)
        self.assertEqual(float(format(attackerSuccessProbability(q, 40), '.7f')), 0.0000095)
        self.assertEqual(float(format(attackerSuccessProbability(q, 50), '.7f')), 0.0000006)

if __name__ == "__main__":
    # run tests: python unit_tests.py
    unittest.main()