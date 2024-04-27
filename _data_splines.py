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
                _template_subs_components["Left|GS-V03.75G-P01.00C@01.75"]
        ),
        "right": (
                _template_subs_components["Right|GS-V03.75G-P01.00C@01.75"] +
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
                _template_subs_components["Left|GS-V03.75G-P01.00C@01.75"]
        ),
        "right": (
                _template_subs_components["Right|GS-V03.75G-P01.00C@01.75"] +
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
                _template_subs_components["Left|GS-V03.75G-P01.00C@01.75"]
        ),
        "right": (
                _template_subs_components["Right|GS-V03.75G-P01.00C@01.75"] +
                []
        ),
        "decorations": (
            []
        )
    }
}
