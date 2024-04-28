_template_sub_geometery = {
}

_template_subs_aipaths = {
    "R-L4-3.1-2.9":
        [
            {"type": "road", "x": -4.55, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": -1.65, "width": 3.1, "direction": "forward"},
            {"type": "road", "x": 1.65, "width": 3.1, "direction": "reverse"},
            {"type": "road", "x": 4.50, "width": 2.9, "direction": "reverse"}
        ],
    "R-L2-3.1":
        [
            {"type": "road", "x": -1.65, "width": 3.1, "direction": "forward"},
            {"type": "road", "x": 1.65, "width": 3.1, "direction": "reverse"}
        ],
    "R-L2-3.3":
        [
            {"type": "road", "x": -1.65, "width": 3.3, "direction": "forward"},
            {"type": "road", "x": 1.65, "width": 3.3, "direction": "reverse"}
        ],
    "R-L2-2.75":
        [
            {"type": "road", "x": -1.375, "width": 2.75, "direction": "forward"},
            {"type": "road", "x": 1.375, "width": 2.75, "direction": "reverse"}
        ]
}

_template_subs_lines = {
    "R12.0-L4{;II;}":
        [
            {"type": "Lane|Broken", "x": -3.1},
            {"type": "Barrier|Both", "x": 0},
            {"type": "Lane|Broken", "x": 3.1}
        ],
    "R{;II;}":
        [
            {"type": "Barrier|Both", "x": 0},
        ],
    "R12.0-L2{$II$}":
        [
            {"type": "Edge|Standard", "x": -3.3},
            {"type": "Barrier|Both", "x": 0},
            {"type": "Edge|Standard", "x": 3.3}
        ],
    "R10.0-L2{$II$}":
        [
            {"type": "Edge|Standard", "x": -3.3},
            {"type": "Barrier|Both", "x": 0},
            {"type": "Edge|Standard", "x": 3.3}
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
