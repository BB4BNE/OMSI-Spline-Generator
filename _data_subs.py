_template_sub_geometery = {
}

_template_subs_aipaths = {
    "R-L4-3.1-2.9":
        [
            {"type": "road", "x": -4.55, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": -1.65, "width": 3.0, "direction": "forward"},
            {"type": "road", "x": 1.65, "width": 3.0, "direction": "reverse"},
            {"type": "road", "x": 4.50, "width": 2.9, "direction": "reverse"}
        ],
    "R-L2-3.1":
        [
            {"type": "road", "x": -1.65, "width": 3.0, "direction": "forward"},
            {"type": "road", "x": 1.65, "width": 3.0, "direction": "reverse"}
        ],
    "R-L2-2.75":
        [
            {"type": "road", "x": -1.375, "width": 2.75, "direction": "forward"},
            {"type": "road", "x": 1.375, "width": 2.75, "direction": "reverse"}
        ]
}

_template_subs_lines = {
    "None": [],
    "R-L4-I+Broken":
        [
            {"type": "Lane|Broken", "x": -3.1},
            {"type": "Separation|Solid (3L+)", "x": 0},
            {"type": "Lane|Broken", "x": 3.1}
        ],
    "R12-L4-I+Broken+NSL2":
        [
            {"type": "Edge|NoStanding", "x": -5.9},
            {"type": "Lane|Broken", "x": -3.1},
            {"type": "Separation|Solid (3L+)", "x": 0},
            {"type": "Lane|Broken", "x": 3.1},
            {"type": "Edge|NoStanding", "x": 5.9}
        ],
    "R12-L4-I+Broken+NSL1":
        [
            {"type": "Edge|NoStanding", "x": -5.9},
            {"type": "Lane|Broken", "x": -3.1},
            {"type": "Separation|Solid (3L+)", "x": 0},
            {"type": "Lane|Broken", "x": 3.1},
        ],
    "R12-L4-I+Broken+TLApp":
        [
            {"type": "Edge|NoStanding", "x": -5.9},
            {"type": "Lane|Continuous", "x": -3.1},
            {"type": "Separation|Solid (3L+)", "x": 0},
            {"type": "Lane|Broken", "x": 3.1},
            {"type": "Edge|NoStanding", "x": 5.9}
        ],
    "R10-L2-;+Solid":
        [
            {"type": "Edge|Standard", "x": -3.1},
            {"type": "Separation|Broken (BCC)", "x": 0},
            {"type": "Edge|Standard", "x": 3.1}
        ]
}

_template_subs_lineGroups = {
    "R12.0L4": [
                 {"name": "-I+Broken", "lines": _template_subs_lines["R-L4-I+Broken"]},
                 {"name": "-I+Broken+NSL2", "lines": _template_subs_lines["R12-L4-I+Broken+NSL2"]},
                 {"name": "-I+Broken+NSL1", "lines": _template_subs_lines["R12-L4-I+Broken+NSL1"]},
                 {"name": "-I+Broken+TLapp", "lines": _template_subs_lines["R12-L4-I+Broken+TLApp"]},
             ],
    "R10.0L2": [
        {"name": "-Blank", "lines": _template_subs_lines["None"]},
        {"name": "-;+Solid", "lines": _template_subs_lines["R10-L2-;+Solid"]}
    ]
}

_template_subs_surfaces = {
    "14m-asphalt": [
        {"x1": -7, "x2": 7, "mapping": None, "material": "Road_Asphalt"}
    ],
    "12m-asphalt": [
        {"x1": -6, "x2": 6, "mapping": None, "material": "Road_Asphalt"}
    ],
    "10m-asphalt": [
        {"x1": -5, "x2": 5, "mapping": None, "material": "Road_Asphalt"}
    ],
    "8.5m-asphalt": [
        {"x1": -4.25, "x2": 4.25, "mapping": None, "material": "Road_Asphalt"}
    ],
    "7.0m-asphalt": [
        {"x1": -3.5, "x2": 3.5, "mapping": None, "material": "Road_Asphalt"}
    ],
    "5.5m-asphalt": [
        {"x1": -2.75, "x2": 2.75, "mapping": None, "material": "Road_Asphalt"}
    ]
}
