from Robot_Fleet import FleetList


fleet = FleetList()
fleet.load_from_json("conf100.json")
fleet.show_fleet()
fleet.counting_sort("range")
fleet.show_fleet()
