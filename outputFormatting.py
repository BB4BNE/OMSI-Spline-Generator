from enums import *
import math
import json

from config import json_dir, input_json_pieces, input_json_decorations, input_json_surfaces

# load JSON files
json_pieces = json.load(open(json_dir + input_json_pieces))
json_decorations = json.load(open(json_dir + input_json_decorations))
json_surfaces = json.load(open(json_dir + input_json_surfaces))


def xPosSort(ptArray):
    return ptArray['x1']


def xPosSort1(ptArray):
    return ptArray['pathX']

# Generate Formatted [path] tag sections of .sli files
def format_paths(paths):
    output = "\n\n#### PATHS ####"
    pathGroupSorted = []
    for pathGroup in paths:
        for path in pathGroup["paths"]:
            pathGroupSorted.append({
                'type': path_type(path['type']),
                'pathX': ((pathGroup['width'] - path['x']) if pathGroup["flipped"] else path['x']) + pathGroup['offset'],
                'height': pathGroup['height'],
                'width': path['width'],
                'direction': path_directions(path['direction'], pathGroup['flipped'])
            })
    pathGroupSorted.sort(key=xPosSort1)
    for pathSorted in pathGroupSorted:
        output += "\n\n[path]\n"
        output += f"{pathSorted['type']}\n"
        output += f"{pathSorted['pathX']:.3f}\n"
        output += f"{pathSorted['height']:.3f}\n"
        output += f"{pathSorted['width']:.2f}\n"
        output += f"{pathSorted['direction']}\n"
    return output


def output_points(points, tiling, materialIndex):
    output = "\n[profile]\n"
    output += f"{materialIndex}\n"
    lastPoint = []
    for point in points:
        if point == lastPoint: continue
        output += "\n[profilepnt]\n"
        output += f"{point['xPosition']:.3f}\n"
        output += f"{point['yPosition']:.3f}\n"
        output += f"{(round(point['relativePosition'],3) + 0.0):.3f}\n"
        output += f"{tiling:.4f}\n"
        lastPoint = point
    return output


def calc_distances(geometry, width, checkmapping=False, flipped=False):
    counter = 0
    mappings = []
    mappingsCount = 0
    mappingIndexFirst = -1
    distances = []

    newGeometry = []
    if not flipped:
        newGeometry = geometry
    else:
        for point in geometry:
            newGeometry.insert(0,
                {
                    "x": width - point['x'],
                    "y": point['y'],
                    "mapping": 1 - point['mapping'] if point['mapping'] is not None else point['mapping'],
                }
            )

    x = -1
    y = -1
    while counter < len(newGeometry):
        mappings.append(newGeometry[counter]["mapping"])
        if newGeometry[counter]["mapping"] is not None:
            mappingsCount += 1
            if mappingIndexFirst == -1: mappingIndexFirst = counter

        x_old = x
        y_old = y
        x = newGeometry[counter]["x"]
        y = newGeometry[counter]["y"]
        if counter > 0:
            distances.append(math.dist([x_old, y_old], [x, y]))
        counter += 1
    if checkmapping:
        if mappingsCount <= 1 or (
                mappingsCount == 2 and newGeometry[0]["mapping"] is not None and newGeometry[-1]["mapping"] is not None):
            pass
        else:
            warnings.warn(f"More than one mapping point defined except ends. Using first for {distances}")
        return distances, newGeometry, mappings, mappingIndexFirst, mappingsCount
    else:
        return distances, newGeometry


def checkMapping(point):
    if "mapping" in point:
        if point["mapping"] is not None:
            return True
    return False


def tilingBetweenPoints(textureDetails, uvStart, point1, point2, x_offset, y_offset, y=False):
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
            uvCurrent = point1["mapping"]
            uvEnd = point2["mapping"]
        else:
            # true + false
            repeatFreq = textureDetails["dimX"]
            uvCurrent = point1["mapping"]
            uvEnd = distanceToGo / repeatFreq + uvCurrent
    else:
        if checkMapping(point2):
            # false + true
            repeatFreq = textureDetails["dimX"]
            uvEnd = point2["mapping"]
            uvCurrent = (uvEnd - distanceToGo / repeatFreq) % 1
        else:
            # false + false
            repeatFreq = textureDetails["dimX"]
            uvCurrent = uvStart
            uvEnd = distanceToGo / repeatFreq + uvCurrent

    output_pts.append({"xPosition": xPosCurrent, "yPosition": yPosCurrent, "relativePosition": uvCurrent})

    # check if on same tile
    if distanceToGo <= repeatFreq and uvEnd <= 1:
        output_pts.append({"xPosition": xPosEnd, "yPosition": yPosEnd, "relativePosition": uvEnd})
    else:
        if textureDetails["TileableX"] != "Yes":
            warnings.warn("Tiling using non-tileable texture: " + textureDetails["Path"])
        # calculate when to tile

        # do while loop
        while True:
            if uvCurrent < 1:
                # do section of do... while
                distanceTravelled = repeatFreq * (1 - uvCurrent)
                uvCurrent = 1
            else:
                output_pts.append(
                    {"xPosition": xPosCurrent, "yPosition": yPosCurrent, "relativePosition": 0})
                distanceTravelled = repeatFreq

            distanceTravelledRatio = distanceTravelled / distanceToGo
            xPosCurrent += distanceTravelledRatio * (xPosEnd - xPosCurrent)
            yPosCurrent += distanceTravelledRatio * (yPosEnd - yPosCurrent)
            distanceToGo = math.dist([xPosCurrent, yPosCurrent], [xPosEnd, yPosEnd])

            output_pts.append(
                {"xPosition": xPosCurrent, "yPosition": yPosCurrent, "relativePosition": 1})
            if uvCurrent + 1 >= math.floor(uvEnd): break

            uvCurrent += 1

        # final Tile
        output_pts.append(
            {"xPosition": xPosCurrent, "yPosition": yPosCurrent, "relativePosition": 0})
        uvEnd -= uvCurrent # as file tile difference is remaining tile
        output_pts.append(
            {"xPosition": xPosEnd, "yPosition": yPosEnd, "relativePosition": uvEnd})
    return output_pts, uvEnd % 1


def textureMappingComplex(pt_details, textureDetails, materialIndex, offset = {"x": 0,"y": 0}):
    repeatFreq = textureDetails["dimX"]
    zRepeatRate = 1 / textureDetails["dimZ"]

    points = []

    # --------- replace for in loop as not really used --------------
    for pts in pt_details:
        # use right end of leftmost pts
        referenceRelative = (offset['x'] % repeatFreq) / repeatFreq

        # reverse mode
        if pts["mode"] == -1 or pts["geometry"][-1]["mapping"] is not None:
            index = 0
            distance = sum(pt_details[index]["distances"])
            relativePosition = referenceRelative - (distance / repeatFreq)
        # forward mode
        else:
            index = -1
            distance = sum(pt_details[index]["distances"])
            relativePosition = referenceRelative

        counter = 1
        while counter < len(pt_details[index]["geometry"]):
            (pts, relativePosition) = tilingBetweenPoints(textureDetails, relativePosition, pt_details[index]["geometry"][counter - 1],
                                    pt_details[index]["geometry"][counter], offset['x'], offset['y'], True)
            points.extend(pts)
            counter += 1
    return output_points(points, zRepeatRate, materialIndex)


def complexComponentBreakdown(component, dict_materials, materials, offset, flip):
    pt_details = []
    for section in component["sections"]:
        distances, newGeometry, mappings, mappingIndexFirst, mappingsCount = calc_distances(section["geometry"], component["width"], True, flip)

        # split if mappingIndex is mid-point
        if mappingIndexFirst != -1 and mappingIndexFirst != 0 and mappingIndexFirst != len(mappings) - 1:
            pt_details.append({
                "geometry": newGeometry[:mappingIndexFirst + 1],
                "distances": distances[:mappingIndexFirst],
                "mappings": mappings[:mappingIndexFirst + 1],
                "mode": -1
            })
            pt_details.append({
                "geometry": newGeometry[mappingIndexFirst:],
                "distances": distances[mappingIndexFirst:],
                "mappings": mappings[mappingIndexFirst:],
                "mode": 1
            })
        else:
            pt_details.append({
                "geometry": newGeometry,
                "distances": distances,
                "mappings": mappings,
                "mode": 0
            })

        pass
        if section["material"] not in materials: materials.append(section["material"])
        materialIndex = materials.index(section["material"])
        return textureMappingComplex(pt_details, dict_materials[section["material"]], materialIndex, offset)


def process_components(source, dict_materials, materials, paths, lines, heightProfiles, mode, offset):
    output_pnts = ""

    flip = source["flip"] == 1

    match source["type"]:
        case "piece":
            component = json_pieces[source['name']]
        case "surface":
            component = json_surfaces[source['name']]
        case "decoration":
            component = json_decorations[source['name']]
        case _:
            warnings.warn(f"invalid use of component type ({source['type']}) for component {source['name']}. Skipping")
            return materials, paths, lines, heightProfiles, offset, offset

    component["height"] = component["height"] if "height" in component else 0
    y_offset = (source["y"] if "y" in source else 0) + component["height"]
    x_offset = source["x"] if "x" in source else 0

    # move pointer to left bound of object
    if mode == 0:
        # middle
        offset += -component["width"] / 2
        offset2 = offset
    elif mode == 1:
        # right
        offset2 = offset
        offset += 0
    elif mode == 3:
        # decorations
        offset = x_offset
        offset2 = x_offset
        component["width"] = 0
    else:
        # left (-1)
        #   offset2 = offset + component["width"] * mode
        offset += component["width"] * mode
        offset2 = offset

    if "aiPaths" in component:
        paths.append({
            "paths": component["aiPaths"],
            "height": component["height"],
            "width": component["width"],
            "flipped": flip,
            "offset": offset2
        })
    if "lines" in component:
        lines.append({
            "lines": component["lines"],
            "height": component["height"],
            "width": component["width"],
            "flipped": flip,
            "offset": offset2
        })

    # Switch. Process different types
    if source["type"] == "piece" or source["type"] == "decoration":
            output_pnts += complexComponentBreakdown(component, dict_materials, materials, {"x": offset, "y": y_offset}, flip)

    elif source["type"] == "surface":
        for surface in component["surfaces"]:
            if surface["material"] not in materials: materials.append(surface["material"])
            materialIndex = materials.index(surface["material"])

            textureDetails = dict_materials[surface["material"]]
            repeatFreq = textureDetails["dimX"]
            zRepeatRate = 1 / textureDetails["dimZ"]
            xStartRelative = ((offset + surface["x1"]) % repeatFreq) / repeatFreq
            x1 = component["width"] - surface["x2"] if source['flip'] else surface["x1"]
            x2 = component["width"] - surface["x1"] if source['flip'] else surface["x2"]
            y_offset = component["height"] + (surface["offset"] if "offset" in surface else 0)
            (pts, relativePosition) = tilingBetweenPoints(textureDetails, xStartRelative, {"x": x1}, {"x": x2}, offset, y_offset, False)
            if x1 >= x2:
                warnings.warn(f"Invalid data for heightProfile: x1: {x1}, x2: {x2}")
            else:
                heightProfiles.append({"x1": x1 + offset, "x2": x2 + offset, "y1": component["height"], "y2": component["height"]})
            output_pnts += output_points(pts, zRepeatRate, materialIndex)

    else:
        warnings.warn(
            f"invalid use of component type ({source['type']}) for component {source['name']}. Skipping")

    return output_pnts, materials, paths, lines, heightProfiles, offset, offset + component["width"]

def format_lines(centre, height, lineDetails, materialIndex):
    line_height_offset = 0.01

    points = [
        {"xPosition": centre - (lineDetails["WidthReal"] / 1000 / 2), "yPosition": height + line_height_offset, "relativePosition": lineDetails["Start%"]},
        {"xPosition": centre + (lineDetails["WidthReal"] / 1000 / 2), "yPosition": height + line_height_offset, "relativePosition": lineDetails["End%"]}
    ]

    return output_points(points, lineDetails['Tiling'], materialIndex)
