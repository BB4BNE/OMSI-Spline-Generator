from templates.shared_components import _template_subs_components
from templates.shared import _template_subs_lines, _template_subs_lineGroups
from templates.decorations import _template_decorations

_templates_splines = {
    "R08.5L2[GPG-GPG]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R08.5-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 0}]),
        "decorations": ([])
    },
    "R10.0L2[G-G]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R10.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-G+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-G+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R10.0L2"]}
        )
    },
    "R10.0L2[GPG-GPG]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R10.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R10.0L2"]}
        )
    },
    "R10.0L2[C-C]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R10.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R10.0L2"]}
        )
    },
    "R10.0L2[A-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R10.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R10.0L2"]}
        )
    },
    "R10.0L2[GPG-G]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R10.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-G+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R10.0L2"]}
        )
    },
    "R10.0L2[GPG-C]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R10.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R10.0L2"]}
        )
    },
    "R10.0L2[GPG-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R10.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R10.0L2"]}
        )
    },

    "R12.0L2[GPG-GPG]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-GPG+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L2"]}
        )
    },
    "R12.0L2[A-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-A+gutterNew"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L2"]}
        )
    },
    "R12.0L2[C-GPG]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-GPG+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L2"]}
        )
    },
    "R12.0L2[C-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L2"]}
        )
    },
    "R12.0L2[C-C]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-C+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L2"]}
        )
    },
    "R12.0L2[GPG-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L2"]}
        )
    },


    "R12.0L4[GPG-GPG]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-GPG+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
                "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )
    },
    "R12.0L4[GPG-G]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-G+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
                "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )
    },
    "R12.0L4[GPG-C]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-C+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )
    },
    "R12.0L4[GPG-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
                "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )
    },
    "R12.0L4[A-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-A+gutterNew"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )
    },
    "R12.0L4[A-C]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-A+gutterNew"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-C+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )
    },
    "R12.0L4[C-C]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R12.0-L4-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_03.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_03.50m-C+gutter"], "flip": 0}]),
        "decorations": ([]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R12.0L4"]}
        )
    },

    "R20.0L4D2+2[GPG-A-GPG]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L4D2+2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },
    "R20.0L4D2+2[A-A-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L4D2+2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },
    "R20.0L4D2+2[C-A-C]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L4D2+2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },
    "R20.0L4D2+2[C-A-GPG]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L4D2+2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },

    "R20.0L5D3+2[GPG-A-GPG]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L5D3+2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },
    "R20.0L5D3+2[A-A-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L5D3+2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },
    "R20.0L5D3+2[C-A-C]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L5D3+2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },
    "R20.0L5D3+2[C-A-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L5D3+2-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },

    "R20.0L6D3+3[GPG-A-GPG]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L6D3+3-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-GPG+gutter"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },
    "R20.0L6D3+3[A-A-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L6D3+3-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },
    "R20.0L6D3+3[C-A-C]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L6D3+3-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    },
    "R20.0L6D3+3[C-A-A]": {
        "inhibit": 0,
        "centre": {
            "type": "surface",
            "name": "R20.0-L6D3+3-A",
            "flip": 0, "offset": 0
        },
        "left": ([{"component": _template_subs_components["Edge_04.50m-C+gutter"], "flip": 1}]),
        "right": ([{"component": _template_subs_components["Edge_04.50m-A+gutterNew"], "flip": 0}]),
        "decorations": ([
            {"type": "decoration", "name": "median-1.2m-oldA", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldB", "flip": 0, "offset": 0},
            {"type": "decoration", "name": "median-1.2m-oldC", "flip": 0, "offset": 0},
        ]),
        "additionalLines": (
            {"height": 0.1, "lineOffset": 0,
             "lineGroups": _template_subs_lineGroups["R20.0D2"]}
        )
    }
}
