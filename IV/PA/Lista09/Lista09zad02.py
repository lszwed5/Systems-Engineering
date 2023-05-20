from Robot_Fleet import FleetList


fleet = FleetList()
fleet.load_from_json("conf10.json")
fleet.show_fleet()
fleet.quicksort(fleet.robots, 0, len(fleet.robots) - 1)
fleet.show_fleet()
