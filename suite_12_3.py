import unittest as ut
import Methods_unittest
import Simple_unittesst


untest = ut.TestSuite()
untest.addTest(ut.TestLoader().loadTestsFromTestCase(Simple_unittesst.RunnerTest))
untest.addTest(ut.TestLoader().loadTestsFromTestCase(Methods_unittest.TournamentTest))

runner = ut.TextTestRunner(verbosity=2)
runner.run(untest)

