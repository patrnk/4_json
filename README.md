# Prettify JSON

A simple script that takes raw json and pretty prints it.

# Quickstart

The script requires Python 3 to run.

Example of script launch on Linux, Python 3.5 (part of the output is omitted):

```#!bash

$ python3 pprint_json.py bars.json
[
    {
        "global_id": 20660594,
        "Latitude_WGS84": "55.7653669567739740",
        "IsNetObject": "нет",
        "PublicPhone": [
            {
                "global_id": 21025.0,
                "global_object_id": 20660594.0,
                "PublicPhone": "(495) 621-19-63",
                "system_object_id": "000069302_1"
            }
        ],
        ...
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
