from chatgpt import remove_invalid_windows_chars
from outputFormatting import *

from datetime import datetime
from config import (output_dir, input_excel, excel_sheet_lines, excel_sheet_lines_key,
                    excel_sheet_materials, excel_sheet_materials_key)

# load data
from _data_splines import _templates_splines

# load Excel tables
# https://stackoverflow.com/questions/14196013/python-creating-dictionary-from-excel-data
from pandas import *

try:
    open(input_excel)
except PermissionError as e:
    raise Exception("##### - Excel file in use - #####") from e
else:
    xls = ExcelFile(input_excel)
    dict_lines = xls.parse(excel_sheet_lines).set_index(excel_sheet_lines_key).to_dict('index')
    dict_materials = xls.parse(excel_sheet_materials).set_index(excel_sheet_materials_key).to_dict('index')

for spline in _templates_splines:
    if "inhibit" in _templates_splines[spline] and _templates_splines[spline]["inhibit"] == 1:
        print(f"skipping spline: {spline}")
        continue

    output = "#### BB4BNE SPLINE GENERATOR ####\n\n"

    # create file level arrays
    materials = []
    paths = []
    lines = []
    heightProfiles = []

    centre = _templates_splines[spline]["centre"]
    # Process Centre
    if centre["type"] != "decoration":

        output_pnts_header = "\n#### POINTS ####\n"

        left = list(reversed(_templates_splines[spline]["left"]))
        right = _templates_splines[spline]["right"]

        (output_pnts, materials, paths, lines, heightProfiles, xLeft, xRight) = (
            process_components(centre, dict_materials, materials, paths, lines, heightProfiles,
                               0, 0, centre["offset"]))

        for componentGroup in left:
            groupFlip = componentGroup["flip"] == 1 if "flip" in componentGroup else False
            if "component" not in componentGroup: continue
            for component in componentGroup["component"]:
                (output_pnts_body, materials, paths, lines, heightProfiles, xLeft, _) = (
                    process_components(component, dict_materials, materials, paths, lines, heightProfiles,
                    groupFlip, -1, xLeft))
                output_pnts = output_pnts_body + output_pnts
        for componentGroup in right:
            groupFlip = componentGroup["flip"] == 1 if "flip" in componentGroup else False
            if "component" not in componentGroup: continue
            for component in componentGroup["component"]:
                (output_pnts_body, materials, paths, lines, heightProfiles, _, xRight) = process_components(
                    component, dict_materials, materials, paths, lines, heightProfiles,
                    groupFlip, 1, xRight)
                output_pnts += output_pnts_body

    # output results
    output_lines = "\n#### LINES ####\n"
    for lineGroup in lines:
        for line in lineGroup["lines"]:
            lineDetails = dict_lines[line["type"]]
            if lineDetails["Material"] not in materials: materials.append(lineDetails["Material"])
            materialIndex = materials.index(lineDetails["Material"])
            lineX = lineGroup['width'] - line['x'] if lineGroup["flipped"] else line['x']
            output_lines += format_lines(lineX + lineGroup["offset"], lineGroup["height"], lineDetails, materialIndex)

    decorations = _templates_splines[spline]["decorations"]
    output_decoration_header = "\n#### DECORATIONS ####\n"
    output_decoration = ""
    for componentGroup in decorations:
        (output_pnts_body, materials, _, _, _, _, _) = process_components(componentGroup, dict_materials,
                                                                          materials, [], [], [],
                                                                          0, 3, 0)
        output_decoration += output_pnts_body

    # Generate Height Profiles
    output_heightprofiles = "\n#### Height Profiles ####\n"
    heightProfiles.sort(key=xPosSort)
    newHeightProfiles = []
    index1 = 0
    index2 = 1
    skip = False
    while index2 < len(heightProfiles):
        if heightProfiles[index1]["y2"] == heightProfiles[index2]["y1"] and heightProfiles[index1]["y1"] == heightProfiles[index2]["y2"]:
            if heightProfiles[index2 - 1]["x2"] == heightProfiles[index2]["x1"]:
                skip = True
            else:
                skip = False
        else:
            skip = False
        if not skip:
            newHeightProfiles.append({
                'x1': heightProfiles[index1]["x1"],
                'x2': heightProfiles[index2 - 1]["x2"],
                'y1': heightProfiles[index1]["y1"],
                'y2': heightProfiles[index2 - 1]["y2"]
            })
            index1 = index2

        if index2 + 1 == len(heightProfiles):
            newHeightProfiles.append({
                'x1': heightProfiles[index2]["x1"],
                'x2': heightProfiles[index2]["x2"],
                'y1': heightProfiles[index2]["y1"],
                'y2': heightProfiles[index2]["y2"]
            })

        index2 += 1

    for pair in newHeightProfiles:
        output_heightprofiles += "[heightprofile]\n"
        output_heightprofiles += f"{pair['x1']:.3f}\n"
        output_heightprofiles += f"{pair['x2']:.3f}\n"
        output_heightprofiles += f"{pair['y1']:.3f}\n"
        output_heightprofiles += f"{pair['y2']:.3f}\n"
        output_heightprofiles += "\n"

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

    # check if paths is right
    output_paths = format_paths(paths) if len(paths) > 0 else ""
    output += output_heightprofiles
    output += output_materials
    output += output_pnts_header + output_pnts
    output += output_lines
    output += output_decoration_header + output_decoration
    output += output_paths

    fileName = remove_invalid_windows_chars(spline)

    sli = open(output_dir + "/" + fileName + ".sli", "w")
    sli.write(output)
    sli.close()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("End | Current Time =", current_time)
