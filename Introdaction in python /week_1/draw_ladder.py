import sys


def draw_ladder(height):
    [print(f"%{height}s" % ("#" * i)) for i in range(1, int(height) + 1)]


draw_ladder(sys.argv[1])
