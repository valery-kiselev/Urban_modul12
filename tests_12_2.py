import unittest
import runtour


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(key, cls.all_results[key])

    def tearDown(self):
        TournamentTest.all_results.update(self.all_results)

    def setUp(self):
        self.r1 = runtour.Runner('Усэйн', 10)
        self.r2 = runtour.Runner('Андрей', 9)
        self.r3 = runtour.Runner('Ник', 3)

    def test_tour(self):
        tour = runtour.Tournament(90, self.r1, self.r3)
        self.all_results = tour.start()
        self.assertTrue(self.all_results[2], self.r3)

    def test_tour_2(self):
        tour = runtour.Tournament(90, self.r2, self.r3)
        self.all_results = tour.start()
        self.assertTrue(self.all_results[2], self.r3)

    def test_tour_3(self):
        tour = runtour.Tournament(90, self.r1, self.r2, self.r3)
        self.all_results = tour.start()
        self.assertTrue(self.all_results[3], self.r3)

if __name__ == '__main__':
    unittest.main()