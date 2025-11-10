#!/usr/bin/env python3

# You have to restart the site apache if you do changes here.
# omd restart apache

from cmk.gui.views.inventory.registry import inventory_displayhints

# our root node
inventory_displayhints.update(
    {
        ".smartjsoninventory.": {
            "title": "Smart JSON Inventory",
            "icon": "entertainment",
        },
    }
)

# our first level child nodes
inventory_displayhints.update(
    {
        ".smartjsoninventory.path0:": {
            "title": "Section Zero",
            "icon": "banana",
            #"icon": "log",
            "keyorder": ["col1", "col2", "col3", "index"],
        },
        ".smartjsoninventory.path1:": {
            "title": "Section One",
            "icon": "beer",
            "keyorder": ["col1", "col2", "col3", "index"],
        },
    }
)

# paint our columns
inventory_displayhints.update(
    {
        ".smartjsoninventory.path0:*.col1": {
            "title": "column1",
        },
        ".smartjsoninventory.path1:*.col1": {
            "title": "column1",
        },
        ".smartjsoninventory.path2:.*col1": {
            "title": "column1",
        },
    }
)
