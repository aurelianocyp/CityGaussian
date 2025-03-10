import json
light_cfg = {"mesh": {"pose": [[-5, 0, 5], ], 
                      "energy": [2.5, ], 
                      "type":["SUN", ], 
                      "scale":[1, ], 
                      "rotation":[[0.0, 0.0, 1.571], ]}, 
            "texture": {"pose": [[-5, 0, 5], ], 
                        "energy": [5, ],
                        "type":["SUN", ], 
                        "scale":[1, ], 
                        "rotation":[[0.0, 0.0, 1.571], ]}}

with open("light.json", "w") as f:
    json.dump(light_cfg, f)