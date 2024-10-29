import logging
import unittest
import rt_with_exceptions as rtw

logging.basicConfig(level=logging.INFO, filemode='w', encoding='UTF-8',
                    filename='runner_tests.log', format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r = rtw.Runner('Bob', -1)
            for i in range(10):
                r.walk()
            self.assertEqual(r.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            r = rtw.Runner(7)
            for i in range(10):
                r.run()
            self.assertEqual(r.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner',
                            exc_info=True)

    def test_challenge(self):
        r = rtw.Runner('Bobik')
        ru = rtw.Runner('Jhonik')
        for i in range(10):
            r.run()
            ru.walk()
        self.assertNotEqual(r.distance, ru.distance)

if __name__ == "__main__":
    unittest.main()
