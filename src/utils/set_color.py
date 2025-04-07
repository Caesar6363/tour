class Colored:
  def custom(children, color):
    return f"{color}{str(children)}\033[39m"
  def red(children):
    return f"\033[31m{str(children)}\033[39m"