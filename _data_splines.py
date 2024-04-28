from _data_subs_components import _template_subs_components

_templates_splines = {
    "R12.0L4{;II;}[VP-VP]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0L4{;II;}",
            "flip": 0,
            "offset": 0
        },
        "left": (
                [] +
                [{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 1}]
        ),
        "right": (
                [{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 0}] +
                []
        ),
        "decorations": (
            []
        )
    },
    "R12.0L4@2{;II;}[VP-VP]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0L4@2{;II;}",
            "flip": 0,
            "offset": 0
        },
        "left": (
                [] +
                [{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 1}]
        ),
        "right": (
                [{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 0}] +
                []
        ),
        "decorations": (
            []
        )
    },
    "R12.0L2{$II$}[VP-VP]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0L2{$II$}",
            "flip": 0,
            "offset": 0
        },
        "left": (
                [] +
                [{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 1}]
        ),
        "right": (
                [{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 0}] +
                []
        ),
        "decorations": (
            []
        )
    },
    "R12.0L2{II}[VP-VP]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0L2{II}",
            "flip": 0,
            "offset": 0
        },
        "left": (
                [] +
                [{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 1}]
        ),
        "right": (
                [{"component": _template_subs_components["C04.00-V03.50G-PC01.00@01.50"], "flip": 0}] +
                []
        ),
        "decorations": (
            []
        )
    },
    "R08.5L2{}[VP-VP]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R08.5L2{}",
            "flip": 0,
            "offset": 0
        },
        "left": (
                [] +
                [{"component": _template_subs_components["C05.75-V05.25G-PC01.00@01.50"], "flip": 1}]
        ),
        "right": (
                [{"component": _template_subs_components["C05.75-V05.25G-PC01.00@01.50"], "flip": 0}] +
                []
        ),
        "decorations": (
            []
        )
    }
}
