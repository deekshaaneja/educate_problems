class VehicleType:
    CAR, TRUCK, BIKE = "CAR", "TRUCK", "BIKE"

class SlotClass:
    def __init__(self, vehicle_type, location):
        self.vehicle_type = vehicle_type
        self.location = location
        self.floor = -1

class Floor:
    def __init__(self, floor_id):
        self.floor_id = floor_id
        self.all_slots = {"CAR": [], "TRUCK":[], "BIKE":[]}
        self.num_slots = {"CAR": 0, "TRUCK":0, "BIKE":0}
        self.available_slots = {"CAR": 0, "TRUCK":0, "BIKE":0}
        self.slots_occupied = {"CAR": [], "TRUCK":[], "BIKE":[]}

    def add_slot(self, slot):
        self.all_slots[slot.vehicle_type].append(slot)
        self.num_slots[slot.vehicle_type] += 1
        self.available_slots[slot.vehicle_type] += 1
        slot.floor = self.floor_id

    def park_vehicle(self, vehicle_type):
        result = None
        if self.available_slots[vehicle_type] > 0:
            for slot in self.all_slots[vehicle_type]:
                if slot not in self.slots_occupied[vehicle_type]:
                    self.slots_occupied[vehicle_type].append(slot)
                    result = slot
                    break
        self.available_slots[vehicle_type] -= 1
        return result

    def free_slot(self, slot):
        self.slots_occupied[slot.vehicle_type].remove(slot)
        self.available_slots[slot.vehicle_type] += 1

        

class ParkingLot:
    def __init__(self):
        self.total_floors = 0
        self.list_floors = []

    def add_floor(self, floor):
        self.list_floors.append(floor)

    def find_available_slot(self, vehicle_type):
        for floor in self.list_floors:
            if floor.available_slots[vehicle_type] > 0:
                return floor.park_vehicle(vehicle_type)
        return None
    
    def exit_vehicle(self, slot):
        for floor in self.list_floors:
            if floor.floor_id == slot.floor:
                floor.free_slot(slot)


def main():
    parking_obj = ParkingLot()
    floor_obj = Floor(1)

    # add parking slots
    slot_obj_1 = SlotClass(VehicleType.CAR, (0, 1))
    slot_obj_2 = SlotClass(VehicleType.CAR, (0, 2))

    floor_obj.add_slot(slot_obj_1)
    floor_obj.add_slot(slot_obj_2)

    parking_obj.add_floor(floor_obj)

    # assign parking slots to vehicles
    vehicle_1_slot = parking_obj.find_available_slot("CAR")
    print("found slot for parking: " + "floor: " + str(vehicle_1_slot.floor) + " location: " + str(vehicle_1_slot.location))
    vehicle_2_slot = parking_obj.find_available_slot("CAR")
    print("found slot for parking: " + "floor: " + str(vehicle_2_slot.floor) + " location: " + str(vehicle_2_slot.location))
    # try to assign slot to an incoming vehicle when all available slots are filled
    vehicle_3_slot = parking_obj.find_available_slot("CAR")
    if vehicle_3_slot is None:
        print("No slot found!")
    # empty a parking slot
    parking_obj.exit_vehicle(vehicle_2_slot)
    # now try to assign available slot to a vehicle
    vehicle_3_slot = parking_obj.find_available_slot("CAR")
    print("found slot for parking: " + "floor: " + str(vehicle_3_slot.floor) + " location: " + str(vehicle_3_slot.location))

if __name__ == "__main__":
    main()