class Colored:
    @staticmethod
    def custom(children, color):
        return f"{color}{str(children)}\033[39m"

    @staticmethod
    def red(children):
        return f"\033[31m{str(children)}\033[39m"
