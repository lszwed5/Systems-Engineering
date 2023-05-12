from Lista08zad01 import FleetList


fleet = FleetList()
fleet.load_from_json("conf.json")
fleet.show_fleet()

print(fleet.search_hash(input("Enter the attribute to search for: "),
                        input("Enter the value of the attribute: "),
                        float(input("Enter the load factor value: "))))
