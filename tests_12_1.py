import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r = runner.Runner('Bob')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)
    def test_run(self):
        r = runner.Runner('Jhon')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)
    def test_challenge(self):
        r = runner.Runner('Bobik')
        ru = runner.Runner('Jhonik')
        for i in range(10):
            r.run()
            ru.walk()
        self.assertNotEqual(r.distance, ru.distance)

if __name__ == "__main__":
    unittest.main()