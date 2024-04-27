from _data_subs import _template_subs_surfaces, _template_subs_aipaths, _template_subs_lines

_template_surfaces = {
    "R12.0L4{;II;}": {
        "width": 12,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] +
                     _template_subs_surfaces["12m-asphalt"]
                     ),
        "lines": ([] +
                  _template_subs_lines['R12.0L4{;II;}']
                  ),
        "aiPaths": ([] +
                    _template_subs_aipaths['R-L4-3.1-2.9']
                    )
    },
    "R12.0L4@2{;II;}": {
        "width": 12,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] +
                     _template_subs_surfaces["12m-asphalt"]
                     ),
        "lines": ([] +
                  _template_subs_lines['R12.0L4{;II;}']
                  ),
        "aiPaths": ([] +
                    _template_subs_aipaths['R-L2-3.1']
                    )
    },
    "R12.0L2{$II$}": {
        "width": 12,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] +
                     _template_subs_surfaces["12m-asphalt"]
                     ),
        "lines": ([] +
                  _template_subs_lines['R12.0L2{$II$}']
                  ),
        "aiPaths": ([] +
                    _template_subs_aipaths['R-L2-3.3']
                    )
    },
    "R12.0L2{II}": {
        "width": 12,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] +
                     _template_subs_surfaces["12m-asphalt"]
                     ),
        "lines": ([] +
                  _template_subs_lines['R{;II;}']
                  ),
        "aiPaths": ([] +
                    _template_subs_aipaths['R-L2-3.3']
                    )
    },
    "V03.75G-P01.00C@01.75": {
        "width": 3.75,
        "referencePointOffset": -1.875,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 3.75, "mapping": None, "material": "Grass", "offset": 0},
            {"x1": 1.75, "x2": 2.75, "mapping": None, "material": "FootpathConcrete", "offset": 0.05}
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 2.25, "width": 1, "direction": "both"}
        ]
    }
}
