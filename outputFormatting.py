from enums import *
import math

# Generate Formatted [path] tag sections of .sli files
def format_paths(centre, paths):
    output = "\n\n#### PATHS ####"
    for path in paths:
        output += "\n\n[path]\n"
        output += f"{path_type(path['type'])}\n"
        output += f"{path['x']}\n"
        output += f"{centre['height']}\n"
        output += f"{path['width']}\n"
        output += f"{path_directions(path['direction'])}\n"
    return output

def output_points(points, height, tiling, materialIndex):
    output = "\n[profile]\n"
    output += f"{materialIndex}\n"
    for point in points:
        output += "\n[profilepnt]\n"
        output += f"{point['xPosition']}\n"
        output += f"{height}\n"
        output += f"{point['relativePosition']}\n"
        output += f"{tiling:.4f}\n"
    return output


def format_lines(centre, height, lineDetails, materialIndex):

    line_height_offset = 0.01

    points = [
        {"xPosition": centre - (lineDetails["WidthReal"] / 1000 / 2), "relativePosition": lineDetails["Start%"]},
        {"xPosition": centre + (lineDetails["WidthReal"] / 1000 / 2), "relativePosition": lineDetails["End%"]}
    ]

    return output_points(points, height + line_height_offset, lineDetails['Tiling'], materialIndex)

# assumes flat | only works in positive x direction
def textureMapping(xStart, xEnd, height, textureDetails, materialIndex):

    repeatFreq = textureDetails["dimX"]
    yRepeatRate = 1 / textureDetails["dimY"]

    distance = xEnd - xStart
    xStartRelative = (xStart % repeatFreq)/repeatFreq
    xEndRelatative = distance / repeatFreq + xStartRelative

    points = [{"xPosition": xStart, "relativePosition": xStartRelative}]

    # check if on same tile
    if distance <= repeatFreq and xEndRelatative <= 1:
        points.append({"xPosition": xEnd, "relativePosition": xEndRelatative})
    else:
        if textureDetails["TileableX"] != "Yes":
            warnings.warn("Tiling using non-tileable texture: " + textureDetails["Path"])
        # calculate when to tile
        xRelativeCurrent = 1
        xPosCurrent = xStart + repeatFreq * (1 - xStartRelative)
        points.append({"xPosition": xPosCurrent, "relativePosition": 1})
        while xRelativeCurrent + 1 < math.floor(xEndRelatative):
            points.append({"xPosition": xPosCurrent, "relativePosition": 0})
            xPosCurrent += distance
            xRelativeCurrent += 1
            points.append({"xPosition": xPosCurrent, "relativePosition": 1})

        # final Tile
        points.append({"xPosition": xPosCurrent, "relativePosition": 0})
        points.append({"xPosition": xEnd, "relativePosition": xEndRelatative-xRelativeCurrent})
    #print(f"Start: {xStart}, End: {xEnd} || {points}")

    return output_points(points, height, yRepeatRate, materialIndex)
# --- unit tests ---
# textureMapping(0,6)
# textureMapping(0,12)
# textureMapping(1,12)
# textureMapping(0,7)
# textureMapping(-3,3)
# textureMapping(-3,4)
# textureMapping(-7.5,4)
# textureMapping(3,-3)

