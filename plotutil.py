from util import FLOAT_EPSILON, distance, DEFAULT_MAX_SIGNAL_POINTS


def round_points(points, precision=2):
    _points = points.copy()
    for i in range(len(_points)):
        new_point = (round(_points[i][0], precision), round(_points[i][1], precision))
        points[i] = new_point


def enforce_one_to_one(points):
    last_good_point = None
    _points = points.copy()
    for point in _points:
        if not last_good_point:
            last_good_point = point
        elif point[0] <= last_good_point[0]:
            points.remove(point)
        else:
            last_good_point = point


def constrain_points(points, num_points=DEFAULT_MAX_SIGNAL_POINTS, already_sorted=False):
    if not already_sorted:
        points.sort()
    if len(points) > num_points:
        while len(points) > num_points:
            min_dist = None
            min_dist_index = -1
            for i in range(len(points) - 1):
                distance_candidate = distance(points[i], points[i + 1])
                if not min_dist or distance_candidate < min_dist:
                    min_dist = distance_candidate
                    min_dist_index = i
            points.pop(min_dist_index)
    elif len(points) < num_points:
        while num_points > len(points) > 1:
            max_dist = None
            max_dist_index = -1
            x, y = None, None
            for i in range(len(points) - 1):
                distance_candidate = distance(points[i], points[i + 1])
                if not max_dist or distance_candidate > max_dist:
                    max_dist = distance_candidate
                    max_dist_index = i
                    x = (points[i][0] + points[i + 1][0]) / 2
                    y = (points[i][1] + points[i + 1][1]) / 2
            points.insert(max_dist_index, (x, y))


def add_head_and_tail(points, timestep, already_sorted=False):
    if not already_sorted:
        points.sort()
    head = (points[0][0] - timestep, 0)
    tail = (points[-1][0] + timestep, 0)
    points.insert(0, head)
    points.append(tail)
