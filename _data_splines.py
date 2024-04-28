from _data_subs_components import _template_subs_components
from _data_subs import _template_subs_lines, _template_subs_lineGroups

_templates_splines = {
    "R12.0L4[VP-VP]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
                "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )},
    "R12.0L4[P-VP]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["C04.00-V03.50-P-P03.00@-01.50"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )},
    "R12.0L4[P-P]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["C04.00-V03.50-P-P03.00@-01.50"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["C04.00-V03.50-P-P03.00@-01.50"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )},
    "R10.0L2[VP-VP]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R10.0-L2",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["C05.00-V04.50-G-P01.00C@-01.50"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["C05.00-V04.50-G-P01.00C@-01.50"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R10.0L2"]}
        )}
}
