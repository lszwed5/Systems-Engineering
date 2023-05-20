from Robot_Fleet import FleetList


fleet = FleetList()
fleet.load_from_json("conf10.json")
fleet.show_fleet()
fleet.past_robots = fleet.robots[:]
fleet.heap_sort("price")
fleet.show_fleet()
