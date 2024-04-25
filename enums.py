import warnings

def path_directions(label):
    match label:
        case "forward":
            return 0
        case "reverse":
            return 1
        case "both":
            return 2
        case _:
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