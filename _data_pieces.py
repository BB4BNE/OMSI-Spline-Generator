from _data_subs import _template_sub_geometery, _template_subs_aipaths

from _data_subs_sections import _template_subs_sections

_template_pieces = {
    "gutter": {
        "width": 0.5,
        "referencePointOffset": -0.25,
        "sections": [
            {
            "material": "GutterA",
            "orientation": 0,
            "geometry":
                [
                    {"x": 0.000, "y": 0.100, "mapping": None},
                    {"x": 0.350, "y": 0.100, "mapping": 0.5},
                    {"x": 0.350, "y": 0.250, "mapping": None},
                    {"x": 0.500, "y": 0.250, "mapping": None}
                ]
            }],
        "aipath": []
    },
    "gutterNew": {
        "width": 0.5,
        "referencePointOffset": -0.25,
        "sections": [
            {
            "material": "GutterNew",
            "orientation": 0,
            "geometry":
                [
                    {"x": 0.000, "y": 0.100, "mapping": None},
                    {"x": 0.350, "y": 0.100, "mapping": 0.5},
                    {"x": 0.350, "y": 0.250, "mapping": None},
                    {"x": 0.500, "y": 0.250, "mapping": None}
                ]
            }],
        "aipath": []
    },
    "gutter_BCC_E": {
        "width": 0.450,
        "referencePointOffset": -0.25,
        "sections": [
            {
            "material": "Gutter_Type_D_E_Concrete_Weathered_TC0440",
            "orientation": 0,
            "geometry":
                [
                    {"x": -0.150, "y": 0.225, "mapping": 0.623047},
                    {"x": -0.040, "y": 0.225, "mapping": 0.697266},
                    {"x":  0.000, "y": 0.075, "mapping": 0.800781},
                    {"x":  0.300, "y": 0.100, "mapping": 1.000000}
                ]
            }],
        "aipath": []
    },

    "gutter_BCC_D": {
        "width": 0.6,
        "referencePointOffset": -0.25,
        "sections": [
            {
                "material": "Gutter_Type_D_E_Concrete_Weathered_TC0440",
                "orientation": 0,
                "geometry":
                    [
                        {"x": -0.150, "y": 0.210, "mapping": 0.423828},
                        {"x": -0.100, "y": 0.210, "mapping": 0.390625},
                        {"x":  0.180, "y": 0.070, "mapping": 0.181641},
                        {"x":  0.450, "y": 0.100, "mapping": 0.000000}
                    ]
            }],
        "aipath": []
    },
    "gutter_BCC_E_Optional": {
        "width": 0.750,
        "referencePointOffset": -0.25,
        "sections": [
            {
            "material": "Gutter_Type_D_E_Concrete_Weathered_TC0440",
            "orientation": 0,
            "geometry":
                [
                    {"x": -0.450, "y": 0.225, "mapping": 0.423828},
                    {"x": -0.150, "y": 0.225, "mapping": 0.623047},
                    {"x": -0.040, "y": 0.225, "mapping": 0.697266},
                    {"x":  0.000, "y": 0.075, "mapping": 0.800781},
                    {"x":  0.300, "y": 0.100, "mapping": 1.000000}
                ]
            }],
        "aipath": []
    },

    "gutter_BCC_D_Optional": {
        "width": 0.9,
        "referencePointOffset": -0.25,
        "sections": [
            {
                "material": "Gutter_Type_D_E_Concrete_Weathered_TC0440",
                "orientation": 0,
                "geometry":
                    [
                        {"x": -0.450, "y": 0.210, "mapping": 0.623047},
                        {"x": -0.150, "y": 0.210, "mapping": 0.423828},
                        {"x": -0.100, "y": 0.210, "mapping": 0.390625},
                        {"x":  0.180, "y": 0.070, "mapping": 0.181641},
                        {"x":  0.450, "y": 0.100, "mapping": 0.000000}
                    ]
            }],
        "aipath": []
    }
}
