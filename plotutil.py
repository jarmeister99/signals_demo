from util import FLOAT_EPSILON


def constrain_points(points, num_points, timestep):
    return None


def add_head_and_tail(points, timestep, minval, maxval):
    new_points = points.copy()
    new_points.sort()
    end_head = new_points[0]
    start_tail = new_points[-1]
    i = 0
    while minval + (i * timestep) <= maxval:
        candidate_x = minval + (i * timestep)
        print(f'end_head: {end_head[0]}')
        print(f'start_tail: {start_tail[0]}')
        print(f'candidate: {candidate_x}')
        if abs(new_points[i][0] - candidate_x) > FLOAT_EPSILON:
            new_points.insert(i, (candidate_x, 0))
        else:
            i += 1
    return new_points
