import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            res1 = Runner('Leonid', speed=-10)
        except:
            logging.warning('Неверная скорость для Runner"')
        else:
            for _ in range(10):
                res1.walk()
            self.assertEqual(res1.distance, 50)
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            res2 = Runner(32)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            for _ in range(10):
                res2.run()
            self.assertEqual(res2.distance, 100)
            logging.info('"test_run" выполнен успешно')

    def test_challenge(self):
        res3 = Runner('Leonid')
        res4 = Runner('Lydmila')
        for _ in range(10):
            res3.run()
            res4.walk()
        self.assertNotEqual(res3.distance, res4.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    format='%(levelname)s | %(message)s')


if __name__ == '__main__':
    unittest.main()

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())