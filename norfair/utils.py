import numpy as np


def validate_points(points: np.array) -> np.array:
    # If the user is tracking only a single point, reformat it slightly.
    if points.shape == (2,):
        points = points[np.newaxis, ...]
    elif len(points.shape) == 1:
        raise_detection_error(points)
    else:
        if points.shape[1] != 2 or len(points.shape) > 2:
            raise_detection_error(points)
    return points


def raise_detection_error(points):
    message = (
        f"Each `Detection` object should have a property `points` of shape (num_of_points_to_track, 2), not {points.shape}. "
        "Check your `Detection` list creation code. "
        "You can read the documentation for the `Detection` class here: "
        "https://github.com/tryolabs/norfair/tree/master/docs#detection\n"
    )
    raise ValueError(message)
