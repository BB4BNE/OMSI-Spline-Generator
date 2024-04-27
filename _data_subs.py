_template_sub_geometery = {
    "Piece|Gutter-Standard":
        [
            {"x": 0.000, "y": 0.100, "mapping": None},
            {"x": 0.350, "y": 0.100, "mapping": 0.5},
            {"x": 0.350, "y": 0.250, "mapping": None},
            {"x": 0.500, "y": 0.250, "mapping": None}
        ]
}

_template_subs_aipaths = {
    "R12.0L4":
        [
            {"type": "road", "x": 1.45, "width": 2.9, "direction": "forward"},
            {"type": "road", "x": 4.45, "width": 3.1, "direction": "forward"},
            {"type": "road", "x": 7.55, "width": 3.1, "direction": "reverse"},
            {"type": "road", "x": 10.55, "width": 2.9, "direction": "reverse"}
        ],
    "R12.0L4@2":
        [
            {"type": "road", "x": 4.45, "width": 3.1, "direction": "forward"},
            {"type": "road", "x": 7.55, "width": 3.1, "direction": "reverse"}
        ],
    "R12.0L2":
        [
            {"type": "road", "x": 4.35, "width": 3.3, "direction": "forward"},
            {"type": "road", "x": 7.65, "width": 3.3, "direction": "reverse"}
        ]
}

_template_subs_lines = {
    "R12.0L4{;II;}":
        [
            {"type": "Lane|Broken", "x": 2.9},
            {"type": "Barrier|Both", "x": 6},
            {"type": "Lane|Broken", "x": 9.1}
        ],
    "R12.0L2{$II$}":
        [
            {"type": "Edge|Standard", "x": 1.7},
            {"type": "Barrier|Both", "x": 6},
            {"type": "Edge|Standard", "x": 10.3}
        ]
}

_template_subs_surfaces = {
    "12m-asphalt": [
        {"x1": 0, "x2": 12, "mapping": None, "material": "Road_Asphalt"}
    ]
}
