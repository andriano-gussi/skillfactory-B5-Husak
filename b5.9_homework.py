import time

class Secundomer:
    """ Класс-декоратор для подсчета времени выполнения оборачиваемой функции"""
    def __init__(self, func):
        # func - оборачиваемая функция
        self.func = func

    def __call__(self, num_runs, *args, **kwargs):
        # num_runs - количество запусков
        # *args, **kwargs - аргументы оборачиваемой функции
        avg_time = 0
        for i in range(num_runs):
            start = time.time()
            result = self.func(*args, **kwargs)
            end = time.time()
            avg_time +=(end-start)
        avg_time /= num_runs
        print("\nКоличество запусков функции '{}': {}\nСреднее время выполнения составило: {} секунд".format(self.func.__name__, num_runs, round(avg_time, 5)))
        return result

@Secundomer
def f(n):
    """ Функция для тестирования """
    for i in range(n):
        pass

def main():
    """ Вызываем задекорированную функцию """

    # При вызове уже задекорированной функции f(n)- первым передаем
    # параметр - количество запусков для декоратора
    f(10, 1000000)    

if __name__ == "__main__":
    main()