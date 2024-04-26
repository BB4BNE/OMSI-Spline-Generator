import warnings


def path_directions(label, flipped):
    if label == "forward":
        return 1 if flipped else 0
    if label == "reverse":
        return 0 if flipped else 1
    if label == "both":
        return 3
    warnings.warn(f"invalid direction {label}. Using 0 (forward).")
    return 0


def path_type(label):
    match label:
        case "road":
            return 0
        case "pedestrian":
            return 1
        case "rail":
            return 2
        case "air":
            return 3
        case _:
            warnings.warn(f"invalid type {label}. Using 0 (road).")
            return 0