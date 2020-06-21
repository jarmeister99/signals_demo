from util import FLOAT_EPSILON


def constrain_points(points, num_points, timestep):
    return None


def add_head_and_tail(points, timestep, minval, maxval, already_sorted=False):
    if not already_sorted:
        points.sort()
    head = []
    tail = []
    i = 0
    while minval + (i * timestep) < points[0][0]:
        head.append((minval + (i * timestep), 0))
        i += 1
    i = 1
    tail_start = round(points[-1][0] * 2.0) / 2.0
    while tail_start + (i * timestep) < maxval + timestep:
        tail.append((tail_start + (i * timestep), 0))
        i += 1
    points = head + points + tail
    return points
