import warnings

from Terminal import Terminal

if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    terminal = Terminal()
    while True:
        terminal.work()
        print("Хотите продолжить работу с программой? y/n")
        if not input().__eq__('y'):
            break
