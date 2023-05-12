from Lista08zad01 import FleetList


fleet = FleetList()
fleet.load_from_json("conf.json")

params = fleet.get_search_parameters()
print(params)
print(fleet.search_linear(params))
