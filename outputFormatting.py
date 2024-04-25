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


def output_points(points, tiling, materialIndex):
    output = "\n[profile]\n"
    output += f"{materialIndex}\n"
    for point in points:
        output += "\n[profilepnt]\n"
        output += f"{point['xPosition']:.3f}\n"
        output += f"{point['yPosition']:.3f}\n"
        output += f"{(round(point['relativePosition'],3) + 0.0):.3f}\n"
        output += f"{tiling:.4f}\n"
    return output


def calc_distances(geometry, checkmapping=False):
    counter = 0
    mappings = []
    mappingsCount = 0
    mappingIndexFirst = -1
    distances = []

    x = -1
    y = -1
    while counter < len(geometry):
        mappings.append(geometry[counter]["mapping"])
        if geometry[counter]["mapping"] is not None:
            mappingsCount += 1
            if mappingIndexFirst == -1: mappingIndexFirst = counter

        x_old = x
        y_old = y
        x = geometry[counter]["x"]
        y = geometry[counter]["y"]
        if counter > 0:
            distances.append(math.dist([x_old, y_old], [x, y]))
        counter += 1
    if checkmapping:
        if mappingsCount <= 1 or (
                mappingsCount == 2 and geometry[0]["mapping"] is not None and geometry[-1]["mapping"] is not None):
            pass
        else:
            warnings.warn(f"More than one mapping point defined except ends. Using first for {distances}")
        return distances, mappings, mappingIndexFirst, mappingsCount
    else:
        return distances


def checkMapping(point):
    if "mapping" in point:
        if point["mapping"] is not None:
            return True
    return False

def tilingBetweenPoints(textureDetails, xRelativeStart, point1, point2, x_offset, y_offset, y=False):
    output_pts = []
    xPosCurrent = point1["x"] + x_offset
    xPosEnd = point2["x"] + x_offset
    yPosCurrent = (point1["y"] if y else 0) + y_offset
    yPosEnd = (point2["y"] if y else 0) + y_offset

    distanceToGo = math.dist([xPosCurrent, yPosCurrent], [xPosEnd, yPosEnd])

    if checkMapping(point1):
        if checkMapping(point2):
            # true + true
            repeatFreq = distanceToGo
            xRelativeCurrent = point1["mapping"]
            xRelativeEnd = point2["mapping"]
        else:
            # true + false
            repeatFreq = textureDetails["dimX"]
            xRelativeCurrent = point1["mapping"]
            xRelativeEnd = distanceToGo / repeatFreq + xRelativeCurrent
    else:
        if checkMapping(point2):
            # false + true
            repeatFreq = textureDetails["dimX"]
            xRelativeEnd = point2["mapping"]
            xRelativeCurrent = (xRelativeEnd - distanceToGo / repeatFreq) % 1
        else:
            # false + false
            repeatFreq = textureDetails["dimX"]
            xRelativeCurrent = xRelativeStart
            xRelativeEnd = distanceToGo / repeatFreq + xRelativeCurrent

    output_pts.append({"xPosition": xPosCurrent, "yPosition": yPosCurrent, "relativePosition": xRelativeCurrent})

    # check if on same tile
    if distanceToGo <= repeatFreq and xRelativeEnd <= 1 and xRelativeCurrent < xRelativeEnd:
        output_pts.append({"xPosition": xPosEnd, "yPosition": yPosEnd, "relativePosition": xRelativeEnd})
    else:
        if textureDetails["TileableX"] != "Yes":
            warnings.warn("Tiling using non-tileable texture: " + textureDetails["Path"])
        # calculate when to tile

        distanceTravelled = 0
        # do while loop
        while True:
            if xRelativeCurrent < 1:
                distanceTravelled = repeatFreq * (1 - xRelativeCurrent)
                xRelativeCurrent = 1
            else:
                output_pts.append(
                    {"xPosition": xPosCurrent, "yPosition": yPosCurrent, "relativePosition": 0})
                distanceTravelled += repeatFreq

            distanceTravelledRatio = distanceTravelled / distanceToGo
            xPosCurrent += distanceTravelledRatio * (xPosEnd - xPosCurrent)
            yPosCurrent += distanceTravelledRatio * (yPosEnd - yPosCurrent)
            distanceToGo = math.dist([xPosCurrent, yPosCurrent], [xPosEnd, yPosEnd])

            output_pts.append(
                {"xPosition": xPosCurrent, "yPosition": yPosCurrent, "relativePosition": 1})

            if xRelativeCurrent + 1 >= math.floor(xRelativeEnd): break

            xRelativeCurrent += 1

        # final Tile
        output_pts.append(
            {"xPosition": xPosCurrent, "yPosition": yPosCurrent, "relativePosition": 0})
        xRelativeEnd = xRelativeEnd - xRelativeCurrent
        output_pts.append(
            {"xPosition": xPosEnd, "yPosition": yPosEnd, "relativePosition": xRelativeEnd})
    return output_pts, xRelativeEnd


def textureMappingComplex(pt_details, textureDetails, materialIndex, leftOffset):
    repeatFreq = textureDetails["dimX"]
    zRepeatRate = 1 / textureDetails["dimZ"]

    points = []

    # --------- replace for in loop as not really used --------------
    for pts in pt_details:
        # use right end of leftmost pts
        referencePos = leftOffset + sum(pt_details[0]["distances"])
        referenceRelative = (referencePos % repeatFreq) / repeatFreq

        # reverse mode
        if pts["mode"] == -1 or pts["geometry"][-1]["mapping"] is not None:
            print("reverse")
            index = 0
            distance = sum(pt_details[index]["distances"])
            relativePosition = referenceRelative - (distance / repeatFreq)

        # forward mode
        else:
            print("forward")
            index = -1
            distance = sum(pt_details[index]["distances"])
            relativePosition = referenceRelative

        counter = 1
        while counter < len(pt_details[index]["geometry"]):
            (pts, relativePosition) = tilingBetweenPoints(textureDetails, relativePosition, pt_details[index]["geometry"][counter - 1],
                                    pt_details[index]["geometry"][counter], referencePos, 0, True)
            points.extend(pts)
            counter += 1
    return output_points(points, zRepeatRate, materialIndex)


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

    if "aiPaths" in component:
        paths.append({"paths": component["aiPaths"], "height": component["height"], "offset": offset})
    if "lines" in component:
        lines.append({"lines": component["lines"], "height": component["height"], "offset": offset})

    match source["type"]:
        case "piece":
            pass

            pt_details = []
            for section in component["sections"]:
                distances, mappings, mappingIndexFirst, mappingsCount = calc_distances(section["geometry"], True)
                print(distances, mappings, mappingIndexFirst, mappingsCount)

                # split if mappingIndex is mid-point
                if mappingIndexFirst != -1 and mappingIndexFirst != 0 and mappingIndexFirst != len(mappings) - 1:
                    pt_details.append({
                        "geometry": section["geometry"][:mappingIndexFirst + 1],
                        "distances": distances[:mappingIndexFirst],
                        "mappings": mappings[:mappingIndexFirst + 1],
                        "mode": -1
                    })
                    pt_details.append({
                        "geometry": section["geometry"][mappingIndexFirst:],
                        "distances": distances[mappingIndexFirst:],
                        "mappings": mappings[mappingIndexFirst:],
                        "mode": 1
                    })
                else:
                    pt_details.append({
                        "geometry": section["geometry"],
                        "distances": distances,
                        "mappings": mappings,
                        "mode": 0
                    })

                pass
                if section["material"] not in materials: materials.append(section["material"])
                materialIndex = materials.index(section["material"])
                output_pnts += textureMappingComplex(pt_details, dict_materials[section["material"]], materialIndex, offset)

        case "surface":
            for surface in component["surfaces"]:
                if surface["material"] not in materials: materials.append(surface["material"])
                materialIndex = materials.index(surface["material"])

                textureDetails = dict_materials[surface["material"]]
                repeatFreq = textureDetails["dimX"]
                zRepeatRate = 1 / textureDetails["dimZ"]
                xStartRelative = ((offset + surface["x1"]) % repeatFreq) / repeatFreq
                (pts, relativePosition) = tilingBetweenPoints(textureDetails, xStartRelative, {"x": surface["x1"]}, {"x": surface["x2"]}, offset, component["height"], False)
                output_pnts += output_points(pts, zRepeatRate, materialIndex)

        case _:
            warnings.warn(
                f"invalid use of component type ({component['type']}) for component {component['name']}. Skipping")
            pass

    return output_pnts, materials, paths, lines, offset, offset + component["width"]

def format_lines(centre, height, lineDetails, materialIndex):
    line_height_offset = 0.01

    points = [
        {"xPosition": centre - (lineDetails["WidthReal"] / 1000 / 2), "yPosition": height + line_height_offset, "relativePosition": lineDetails["Start%"]},
        {"xPosition": centre + (lineDetails["WidthReal"] / 1000 / 2), "yPosition": height + line_height_offset, "relativePosition": lineDetails["End%"]}
    ]

    return output_points(points, lineDetails['Tiling'], materialIndex)
