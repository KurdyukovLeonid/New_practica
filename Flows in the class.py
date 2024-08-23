from threading import Thread
from time import sleep

class Knight(Thread):
    total_opponets = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.total = Knight.total_opponets

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.total > 0:
            sleep(1)
            self.days += 1
            self.total -= self.power
            if self.total < 0:
                self.total = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., "
                  f"осталось {self.total} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")