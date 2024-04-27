from _data_subs_components import _template_subs_components

_templates_splines = {
    "R12.0L4{;II;}[VP-VP]": {
        "inhibit": 1,
        "centre": {
            "type": "surface",
            "name": "R12.0L4{;II;}",
            "flip": 0,
            "offset": 0
        },
        "left": (
                [] +
                [{"component": _template_subs_components["GS-V03.75G-P01.00C@01.75"], "flip": 1}]
        ),
        "right": (
                [{"component": _template_subs_components["GS-V03.75G-P01.00C@01.75"], "flip": 0}] +
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
                [{"component": _template_subs_components["GS-V03.75G-P01.00C@01.75"], "flip": 1}]
        ),
        "right": (
                [{"component": _template_subs_components["GS-V03.75G-P01.00C@01.75"], "flip": 0}] +
                []
        ),
        "decorations": (
            []
        )
    },
    "R12.0L2{$II$}[VP-VP]": {
        "inhibit": 1,
        "centre": {
            "type": "surface",
            "name": "R12.0L2{$II$}",
            "flip": 0,
            "offset": 0
        },
        "left": (
                [] +
                [{"component": _template_subs_components["GS-V03.75G-P01.00C@01.75"], "flip": 1}]
        ),
        "right": (
                [{"component": _template_subs_components["GS-V03.75G-P01.00C@01.75"], "flip": 0}] +
                []
        ),
        "decorations": (
            []
        )
    }
}
