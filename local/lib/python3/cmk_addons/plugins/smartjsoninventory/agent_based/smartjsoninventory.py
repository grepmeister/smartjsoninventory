#!/usr/bin/env python3

import json

from cmk.agent_based.v2 import (
    AgentSection,
    InventoryPlugin,
    InventoryResult,
    StringTable,
    TableRow,
)

# In my opinion the formatting of pprintpp is much nicer than
# the one of pprint unfortunately but checkmk only ships pprint
# pip install pprintpp
try:
    from pprintpp import pprint as pp
except ImportError:
    from pprint import pprint as pp

# The parse function
# it get's the data from one or more <<<smartjsoninventory:sep(0)>>> section as a list of lists
#pp(section)
def parse_smartjsoninventory(string_table: StringTable):
    pp(string_table)
    result = {}
    for i, line in enumerate(string_table):
        result[f"path{i}"] = json.loads(line[0])
    #pp(section)
    return result


# add table rows to the inventory
def inventory_smartjsoninventory(section) -> InventoryResult:
    #pp(section)
    for path, table in section.items():

        for index, row in enumerate(table):

            yield TableRow(
                path=["smartjsoninventory", path],
                key_columns={"index": index},
                inventory_columns=row,
            )


# Variable has to start with 'agent_section_'
agent_section_smartjsoninventory = AgentSection(
    name="smartjsoninventory",
    parse_function=parse_smartjsoninventory,
)

# Variable has to start with 'inventory_plugin_'
inventory_plugin_smartjsoninventory = InventoryPlugin(
    name="smartjsoninventory", inventory_function=inventory_smartjsoninventory
)
