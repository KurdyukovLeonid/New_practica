import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        res1 = Runner('Leonid')
        for _ in range(10):
            res1.walk()
        self.assertEqual(res1.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        res2 = Runner('Leonid')
        for _ in range(10):
            res2.run()
        self.assertEqual(res2.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        res3 = Runner('Leonid')
        res4 = Runner('Lydmila')
        for _ in range(10):
            res3.run()
            res4.walk()
        self.assertNotEqual(res3.distance, res4.distance)


if __name__ == '__main__':
    unittest.main()
