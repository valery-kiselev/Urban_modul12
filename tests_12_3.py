import unittest
import runtour


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r = runtour.Runner('Bob')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r = runtour.Runner('Jhon')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r = runtour.Runner('Bobik')
        ru = runtour.Runner('Jhonik')
        for i in range(10):
            r.run()
            ru.walk()
        self.assertNotEqual(r.distance, ru.distance)

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.r1 = runtour.Runner('Усэйн', 10)
        self.r2 = runtour.Runner('Андрей', 9)
        self.r3 = runtour.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour(self):
        tour = runtour.Tournament(90, self.r1, self.r3)
        self.all_results = tour.start()
        self.assertTrue(self.all_results[2], self.r3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        tour = runtour.Tournament(90, self.r2, self.r3)
        self.all_results = tour.start()
        self.assertTrue(self.all_results[2], self.r3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour_3(self):
        tour = runtour.Tournament(90, self.r1, self.r2, self.r3)
        self.all_results[3] = tour.start()
        self.assertTrue(self.all_results[3], self.r3)


if __name__ == "__main__":
    unittest.main()