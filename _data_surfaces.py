from _data_subs import _template_subs_surfaces, _template_subs_aipaths, _template_subs_lines

_template_surfaces = {
    "R12.0-L4-A": {
        "width": 12,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] + _template_subs_surfaces["12m-asphalt"]),
        "lines": ([]),
        "aiPaths": ([] + _template_subs_aipaths['R-L4-3.1-2.9'])
    },
    "R12.0-L2-A": {
        "width": 12,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] + _template_subs_surfaces["12m-asphalt"]),
        "lines": ([]),
        "aiPaths": ([] + _template_subs_aipaths['R-L2-3.1'])
    },
    "R10.0W-L2-A": {
        "width": 10,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] + _template_subs_surfaces["10m-asphalt"]),
        "lines": ([]),
        "aiPaths": ([] + _template_subs_aipaths['R-L2-3.1'])
    },
    "R10.0-L2-A": {
        "width": 10,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] + _template_subs_surfaces["10m-asphalt"]),
        "lines": ([]),
        "aiPaths": ([] + _template_subs_aipaths['R-L2-3.1N'])
    },
    "R08.5-L2-A": {
        "width": 8.5,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] + _template_subs_surfaces["8.5m-asphalt"]),
        "lines": ([]),
        "aiPaths": ([] + _template_subs_aipaths['R-L2-2.75'])
    },
    "R20.0-L4D2+2-A": {
        "width": 20,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] + _template_subs_surfaces["20m-asphalt"]),
        "lines": ([]),
        "aiPaths": ([] + _template_subs_aipaths['R-L4D2+2-2.9'])
    },
    "R20.0-L5D3+2-A": {
        "width": 20,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] + _template_subs_surfaces["20m-asphalt"]),
        "lines": ([]),
        "aiPaths": ([] + _template_subs_aipaths['R-L5D3+2-2.9'])
    },
    "R20.0-L6D3+3-A": {
        "width": 20,
        "referencePointOffset": 0,
        "height": 0.1,
        "surfaces": ([] + _template_subs_surfaces["20m-asphalt"]),
        "lines": ([]),
        "aiPaths": ([] + _template_subs_aipaths['R-L6D3+3-2.9'])
    },
    "Verge_03.50m-A-AI@-01.50m": {
        "width": 3.5,
        "referencePointOffset": -1.750,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 3.5, "mapping": None, "material": "AggregateNew", "offset": 0}
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 2.0, "width": 3, "direction": "both"}
        ]
    },
    "Verge_03.50m-C-AI@-01.50m": {
        "width": 3.5,
        "referencePointOffset": -1.750,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 3.5, "mapping": None, "material": "SideConcrete", "offset": 0}
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 2.0, "width": 3, "direction": "both"}
        ]
    },
    "Verge_03.50m-GPG-AI@-01.50m": {
        "width": 3.5,
        "referencePointOffset": -1.750,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 3.5, "mapping": None, "material": "Grass", "offset": 0},
            {"x1": 1.5, "x2": 2.5, "mapping": None, "material": "FootpathConcrete", "offset": 0.05}
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 2.0, "width": 1, "direction": "both"}
        ]
    },
    "Verge_03.50m-G-AI@-01.50m": {
        "width": 3.5,
        "referencePointOffset": -1.750,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 3.5, "mapping": None, "material": "Grass", "offset": 0},
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 2.0, "width": 1, "direction": "both"}
        ]
    },
    "Verge_03.75m-GPG-AI@01.50m": {
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
    },
    "Verge_04.00m-A-AI@-1.00m": {
        "width": 4.00,
        "referencePointOffset": -2.000,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 4.00, "mapping": None, "material": "AggregateNew", "offset": 0},
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 3.0, "width": 1, "direction": "both"}
        ]
    },
    "Verge_04.50m-GPG-AI@-01.50m": {
        "width": 4.5,
        "referencePointOffset": -2.250,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 4.5, "mapping": None, "material": "Grass", "offset": 0},
            {"x1": 2.5, "x2": 3.5, "mapping": None, "material": "FootpathConcrete", "offset": 0.05}
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 3.00, "width": 1, "direction": "both"}
        ]
    },
    "Verge_04.50m-G-AI@-01.50m": {
        "width": 4.5,
        "referencePointOffset": -2.250,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 4.5, "mapping": None, "material": "Grass", "offset": 0},
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 3.00, "width": 1, "direction": "both"}
        ]
    },
    "Verge_04.50m-C-AI@-01.50m": {
        "width": 4.5,
        "referencePointOffset": -2.250,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 4.5, "mapping": None, "material": "FootpathConcrete", "offset": 0},
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 3.00, "width": 1, "direction": "both"}
        ]
    },
    "Verge_04.50m-A-AI@-01.50m": {
        "width": 4.5,
        "referencePointOffset": -2.250,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 4.5, "mapping": None, "material": "AggregateNew", "offset": 0},
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 3.00, "width": 1, "direction": "both"}
        ]
    },
    "Verge_05.25m-GPG-AI@-01.50m": {
        "width": 5.25,
        "referencePointOffset": -2.625,
        "height": 0.25,
        "surfaces": [
            {"x1": 0, "x2": 5.25, "mapping": None, "material": "Grass", "offset": 0},
            {"x1": 3.25, "x2": 4.25, "mapping": None, "material": "FootpathConcrete", "offset": 0.01}
        ],
        "lines": [],
        "aiPaths": [
            {"type": "pedestrian", "x": 3.75, "width": 1, "direction": "both"}
        ]
    },
}
