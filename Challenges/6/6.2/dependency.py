import datetime
import sys


class Logger:
    def event(self, s):
        print(s)

    def warning(self, s):
        print(s, file=sys.stderr)


class TimeLogger:
    def isotime(self):
        return datetime.datetime.now().isoformat()

    def event(self, s):
        print(f"{self.isotime()}: {s}")

    def warning(self, s):
        print(f"{self.isotime()}: WARNING: {s}")


class Divider:
    def __init__(self, logger=None):
        if logger != None:
            self.logger = logger
        else:
            self.logger = Logger() #To retain default functionality

    def divide(self, a, b):
        if b == 0:
            self.logger.warning("division by zero")
            return None
        self.logger.event(f"dividing {a} by {b}")
        return a / b


if __name__ == "__main__":
    normal_divider = Divider(Logger())
    timed_divider = Divider(TimeLogger())

    normal_divider.divide(1, 2)
    normal_divider.divide(10, 5)
    normal_divider.divide(99, 0)

    timed_divider.divide(1, 2)
    timed_divider.divide(10, 5)
    timed_divider.divide(99, 0)