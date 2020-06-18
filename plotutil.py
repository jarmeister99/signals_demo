from util import FLOAT_EPSILON


def constrain_points(points, num_points, timestep):
    return None


def add_head_and_tail(points, timestep, min, max):
    new_points = points.copy()
    i = 0
    while min + (i * timestep) <= max:
        candidate_x = min + (i * timestep)
        if abs(new_points[i][0] - candidate_x) > FLOAT_EPSILON:
            new_points.insert(i, (candidate_x, 0))
        else:
            i += 1
    return new_points


