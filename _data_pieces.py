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
    }    
}
