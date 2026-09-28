_template_sub_geometery = {
}

_template_subs_aipaths = {
    "R-L4-3.1-2.9":
        [
            {"type": "road", "x": -4.6, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": -1.65, "width": 3.0, "direction": "forward"},
            {"type": "road", "x": 1.65, "width": 3.0, "direction": "reverse"},
            {"type": "road", "x": 4.6, "width": 2.9, "direction": "reverse"}
        ],
    "R-L2-3.1":
        [
            {"type": "road", "x": -1.65, "width": 3.0, "direction": "forward"},
            {"type": "road", "x": 1.65, "width": 3.0, "direction": "reverse"}
        ],
    "R-L2-3.1N":
        [
            {"type": "road", "x": -1.65, "width": 0.05, "direction": "forward"},
            {"type": "road", "x": 1.65, "width": 0.05, "direction": "reverse"}
        ],
    "R-L2-2.75":
        [
            {"type": "road", "x": -1.450, "width": 0.05, "direction": "forward"},
            {"type": "road", "x": 1.450, "width": 0.05, "direction": "reverse"}
        ],
    "R-L4D2+2-2.9":
        [
            {"type": "road", "x": -5.475, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": -2.300, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": 2.300, "width": 2.9, "direction": "reverse"},
            {"type": "road", "x": 5.475, "width": 2.9, "direction": "reverse"}
        ],
    "R-L5D3+2-2.9":
        [
            {"type": "road", "x": -8.750, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": -5.475, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": -2.300, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": 2.300, "width": 2.9, "direction": "reverse"},
            {"type": "road", "x": 5.475, "width": 2.9, "direction": "reverse"},
            {"type": "road", "x": 8.750, "width": 2.9, "direction": "reverse"}
        ],
    "R-L6D3+3-2.9":
        [
            {"type": "road", "x": -8.750, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": -5.475, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": -2.300, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": 2.300, "width": 2.9, "direction": "reverse"},
            {"type": "road", "x": 5.475, "width": 2.9, "direction": "reverse"},
            {"type": "road", "x": 8.750, "width": 2.9, "direction": "reverse"}
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
    "R12-L2-;+Solid":
        [
            {"type": "Edge|Outline", "x": -3.35},
            {"type": "Separation|Broken (BCC)", "x": 0},
            {"type": "Edge|Outline", "x": 3.35}
        ],
    "R10-L2-Solid":
        [
            {"type": "Separation|Broken (BCC)", "x": 0},
        ],
    "R10-L2-;+Solid":
        [
            {"type": "Edge|Standard", "x": -3.15},
            {"type": "Separation|Broken (BCC)", "x": 0},
            {"type": "Edge|Standard", "x": 3.15}
        ],
    "R10-L2-NSL1":
        [
            {"type": "Edge|NoStanding", "x": -4.9}
        ],
    "R10-L2-NSL2":
        [
            {"type": "Edge|NoStanding", "x": -4.9},
            {"type": "Edge|NoStanding", "x": 4.9}
        ],
    "R20-D2":
        [
            {"type": "Edge|Standard", "x": -7.1},
            {"type": "Separation|Broken (BCC)", "x": -3.85},
            {"type": "Edge|Standard", "x": -0.75},
            {"type": "Edge|Standard", "x": 0.75},
            {"type": "Separation|Broken (BCC)", "x": 3.85},
            {"type": "Edge|Standard", "x": 7.1}
        ]
}

_template_subs_lineGroups = {
    "R12.0L4": [
         {"name": "-I+Broken", "lines": _template_subs_lines["R-L4-I+Broken"]},
         {"name": "-I+Broken+NSL2", "lines": _template_subs_lines["R12-L4-I+Broken+NSL2"]},
         {"name": "-I+Broken+NSL1", "lines": _template_subs_lines["R12-L4-I+Broken+NSL1"]},
         {"name": "-I+Broken+TLapp", "lines": _template_subs_lines["R12-L4-I+Broken+TLApp"]},
             ],
    "R12.0L2": [
        {"name": "-;+Solid", "lines": _template_subs_lines["R12-L2-;+Solid"]},
        {"name": "-Blank", "lines": _template_subs_lines["None"]},
             ],
    "R10.0L2": [
        {"name": "-Blank", "lines": _template_subs_lines["None"]},
        {"name": "-Blank+NSL1", "lines": _template_subs_lines["R10-L2-NSL1"]},
        {"name": "-Blank+NSL2", "lines": _template_subs_lines["R10-L2-NSL2"]},
        {"name": "-;+Solid", "lines": _template_subs_lines["R10-L2-;+Solid"]},
        {"name": "-Solid", "lines": _template_subs_lines["R10-L2-Solid"]},
    ],
    "R20.0D2": [
        {"name": "$;+solid", "lines": _template_subs_lines["R20-D2"]},
    ]
}

_template_subs_surfaces = {
    "20m-asphalt": [
        {"x1": -10, "x2": 10, "mapping": None, "material": "Road_Asphalt"}
    ],
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
