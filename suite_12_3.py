import unittest
import tests_12_3

runtourST = unittest.TestSuite()
runtourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runtourST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runtourST)