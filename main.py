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
json_splines = json.load(open("data/splines.json"))

for spline in json_splines:
    output = "#### BB4BNE SPLINE GENERATOR ####\n\n"

    # create file level arrays
    materials = []
    paths = []
    lines = []

    centre = json_splines[spline]["centre"]
    # Process Centre
    if centre["type"] != "decoration":

        output_pnts_header = "\n#### POINTS ####\n"

        left = list(reversed(json_splines[spline]["left"]))
        right = json_splines[spline]["right"]

        (output_pnts, materials, paths, lines, xLeft, xRight) = process_components(centre, dict_materials, materials, paths, lines, 0, centre["offset"])

        for component in left:
            (output_pnts_body, materials, paths, lines, xLeft, _) = process_components(component, dict_materials, materials, paths, lines, -1, xLeft)
            output_pnts = output_pnts_body + output_pnts
        for component in right:
            (output_pnts_body, materials, paths, lines, _, xRight) = process_components(component, dict_materials, materials, paths, lines, 1, xRight)
            output_pnts += output_pnts_body

    # output results
    output_lines = "\n#### LINES ####\n"
    for lineGroup in lines:
        for line in lineGroup["lines"]:
            lineDetails = dict_lines[line["type"]]
            if lineDetails["Material"] not in materials: materials.append(lineDetails["Material"])
            materialIndex = materials.index(lineDetails["Material"])
            output_lines += format_lines(line["x"] + lineGroup["offset"], lineGroup["height"], lineDetails, materialIndex)

    # Generate Materials after everything else
    output_materials = "\n#### MATERIALS ####\n"
    for material in materials:
        materialDetails = dict_materials[material]
        output_materials += "\n[texture]\n"
        output_materials += f"{materialDetails['Path']}\n\n"

        # stop if no transparency
        if materialDetails['Alpha'][0] == "0":
            continue

        output_materials += "[matl_alpha]\n"
        output_materials += f"{materialDetails['Alpha'][0]}\n\n"


    decorations = json_splines[spline]["decorations"]
    output_decoration = "\n#### DECORATIONS ####\n"
    for decoration in decorations:
        pass

    # check if paths is right
    output_paths = format_paths(paths) if len(paths) > 0 else ""
    output += output_materials
    output += output_pnts_header + output_pnts
    output += output_lines
    output += output_paths

    sli = open(output_dir + "/test.sli", "w")
    sli.write(output)
    sli.close()

print("End")
