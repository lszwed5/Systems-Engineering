from Lista08zad01 import FleetList


fleet = FleetList()
fleet.load_from_json("conf.json")

param = input("Select the parameter to sort by: ")
robot = fleet.robots[fleet.search_binary(param, FleetList.get_search_parameters())]
print(robot.price, robot.range)
