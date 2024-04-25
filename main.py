import sys
import json
import warnings

from enums import *
from outputFormatting import *

output_dir = "O:/SteamLibrary/steamapps/common/OMSI 2/Splines/BB4BNE/generated"
excel_input = "C:/OneDrive/BB4BNE Working/OMSI/RoadSplineDetails.xlsx"

# load Excel tables
# https://stackoverflow.com/questions/14196013/python-creating-dictionary-from-excel-data
from pandas import *

try:
    open(excel_input)
except PermissionError as e:
    raise Exception("##### - Excel file in use - #####") from e
else:
    xls = ExcelFile(excel_input)
    dict_lines = xls.parse("Lines").set_index('LineName').to_dict('index')
    dict_materials = xls.parse("Materials").set_index('MaterialName').to_dict('index')

# load JSON files
json_decorations = json.load(open("data/decorations.json"))
json_pieces = json.load(open("data/pieces.json"))
json_splines = json.load(open("data/splines.json"))
json_surfaces = json.load(open("data/surfaces.json"))


for spline in json_splines:
    output = "#### BB4BNE SPLINE GENERATOR ####\n\n"
    materials = []
    baseHeightOffset = 0
    paths = []
    xLeft = 0

    # Process Centre
    print(json_splines[spline]["centre"])
    centre = json_surfaces[json_splines[spline]["centre"]]
    xLeft = 0 - (centre["width"] / 2) - json_splines[spline]["offset"]
    paths.extend(centre["aiPaths"])

    output_pnts = "\n#### POINTS ####\n"
    output_materials = "\n#### MATERIALS ####\n"
    output_lines = "\n#### LINES ####\n"

    for surface in centre["surfaces"]:
        if surface["material"] not in materials: materials.append(surface["material"])
        materialIndex = materials.index(surface["material"])
        output_pnts += textureMapping(xLeft + surface["x1"], xLeft + surface["x2"], centre["height"], dict_materials[surface["material"]], materialIndex)

    for line in centre["lines"]:
        lineDetails = dict_lines[line["type"]]
        if lineDetails["Material"] not in materials: materials.append(lineDetails["Material"])
        materialIndex = materials.index(lineDetails["Material"])
        output_lines += format_lines(line["x"], centre["height"], lineDetails, materialIndex)

    # output results

    for material in materials:
        materialDetails = dict_materials[material]
        output_materials += "\n[texture]\n"
        output_materials += f"{materialDetails['Path']}\n\n"

        # stop if no transparency
        if materialDetails['Alpha'][0] == "0":
            continue

        output_materials += "\n[matl_alpha]\n"
        output_materials += f"{materialDetails['Alpha'][0]}\n"

    output_paths = format_paths(centre, paths) if len(paths) > 0 else ""
    output += output_materials
    output += output_pnts
    output += output_lines
    output += output_paths
    print(output)

    sli = open(output_dir + "/test.sli", "w")
    sli.write(output)
    sli.close()

print("Stop")
