from enums import *
import math
import json

# load JSON files
json_pieces = json.load(open("data/pieces.json"))
json_surfaces = json.load(open("data/surfaces.json"))

# Generate Formatted [path] tag sections of .sli files
def format_paths(paths):
    output = "\n\n#### PATHS ####"
    for pathGroup in paths:
        for path in pathGroup["paths"]:
            output += "\n\n[path]\n"
            output += f"{path_type(path['type'])}\n"
            output += f"{(path['x'] + pathGroup['offset']):.3f}\n"
            output += f"{pathGroup['height']:.3f}\n"
            output += f"{path['width']:.2f}\n"
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


def process_components(source, dict_materials, materials, paths, lines, mode, offset):
    output_pnts = ""

    match source["type"]:
        case "piece":
            component = json_pieces[source['name']]
        case "surface":
            component = json_surfaces[source['name']]
        case _:
            warnings.warn(f"invalid use of component type ({source['type']}) for component {source['name']}. Skipping")
            return materials, paths, lines, offset, offset

    # move pointer to left bound of object
    if mode == 0:
        offset += -component["width"] / 2
    else:
        offset += component["width"] * mode

    match source["type"]:
        case "piece":
            pass
        case "surface":
            paths.append({"paths": component["aiPaths"], "height": component["height"], "offset": offset})
            lines.append({"lines": component["lines"], "height": component["height"], "offset": offset})
            for surface in component["surfaces"]:
                if surface["material"] not in materials: materials.append(surface["material"])
                materialIndex = materials.index(surface["material"])
                output_pnts += textureMapping(offset + surface["x1"], offset + surface["x2"], component["height"],
                                              dict_materials[surface["material"]], materialIndex)
        case _:
            warnings.warn(f"invalid use of component type ({component['type']}) for component {component['name']}. Skipping")
            pass

    return output_pnts, materials, paths, lines, offset, offset + component["width"]

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

