from _data_subs_sections import _template_subs_sections
from _data_subs import _template_sub_geometery

_template_decorations = {
    "tunnelTestDummy": {
        "sections": [
            {
                "material": "ConcreteBarrier",
                "geometry": [
                    {"x": 12.0, "y": 0.00, "mapping": None},
                    {"x": -12.0, "y": 0.00, "mapping": None}
                ]
            }
        ]
    },
    "tunnelTest": {
        "sections": [
            {
                "material": "ConcreteBarrier",
                "geometry": [
                    {"x": 10.0, "y": 0.00, "mapping": None},
                    {"x": 10.0, "y": 3.00, "mapping": None},
                    {"x": 6.0, "y": 6.00, "mapping": None},
                    {"x": -6.0, "y": 6.00, "mapping": None},
                    {"x": -10.0, "y": 3.00, "mapping": None},
                    {"x": -10.0, "y": 0.00, "mapping": None}
                ]
            }
        ]
    },
    "median-1.2m-oldA": {
        "sections": [
            {
                "material": "ConcreteBarrier",
                "geometry": [
                    {"x": -0.6, "y": 0.10, "mapping": None},
                    {"x": -0.5, "y": 0.15, "mapping": None},
                ]
            },
        ]
    },
    "median-1.2m-oldB": {
        "sections": [
            {
                "material": "AggregateOld",
                "geometry": [
                    {"x": -0.5, "y": 0.15, "mapping": None},
                    {"x": 0.5, "y": 0.15, "mapping": None},
                ]
            },
        ]
    },
    "median-1.2m-oldC": {
        "sections": [
            {
                "material": "ConcreteBarrier",
                "geometry": [
                    {"x": 0.5, "y": 0.15, "mapping": None},
                    {"x": 0.6, "y": 0.10, "mapping": None},
                ]
            },
        ]
    },
}