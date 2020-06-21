import math

DEFAULT_GRID_WIDTH = 10
DEFAULT_GRID_HEIGHT = 10

TIMESTEP = 0.5
DEFAULT_MAX_SIGNAL_POINTS = 128

DEFAULT_X_AXIS_TICKS = 10
X_AXIS_TICK_LABEL_FREQ = 2  # Label frequency of 2 means every other tick is labeled
X_AXIS_UNIT = 'S'
X_AXIS_PADDING = 20

DEFAULT_Y_AXIS_TICKS = 10
Y_AXIS_TICK_LABEL_FREQ = 2
Y_AXIS_UNIT = 'V'
Y_AXIS_PADDING = 10

SIGNAL_1 = 1
SIGNAL_2 = 2
SIGNAL_COLORS = [None, 'red4', 'blue']

FLOAT_EPSILON = 0.01


def distance(point1, point2):
    dx = abs(point1[0] - point2[0])
    dy = abs(point1[1] - point2[1])
    return math.sqrt(dx ** 2 + dy ** 2)
