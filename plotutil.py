from util import FLOAT_EPSILON


def constrain_points(points, num_points, timestep):
    return None


def add_head_and_tail(points, timestep, already_sorted=False):
    if not already_sorted:
        points.sort()
    head = [(points[0][0] - timestep, 0)]
    tail = [(points[-1][0] + timestep, 0)]
    return head + points + tail
