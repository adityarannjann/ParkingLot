class ParkingLot:
    def __init__(self):
        self.parking_dict = {}
        self.levels = {'A': list(range(1, 21)), 'B': list(range(21, 41))}

    def assign_parking_spot(self, vehicle_number):
        for level, spots in self.levels.items():
            if spots:
                spot_number = spots.pop(0)
                self.parking_dict[vehicle_number] = {'level': level, 'spot': spot_number}
                return {'level': level, 'spot': spot_number}
        return None

    def fetch_parking_spot(self, vehicle_number):
        if vehicle_number in self.parking_dict:
            return self.parking_dict[vehicle_number]
        return None

# Terminal-based application
if __name__ == "__main__":
    parking_lot = ParkingLot()

    while True:
        print("1. Assign Parking Spot")
        print("2. Retrieve Parking Spot")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            vehicle_number = input("Enter vehicle number: ")
            data = parking_lot.assign_parking_spot(vehicle_number)
            if data:
                print(f"Parking spot assigned: {data}")
            else:
                print("Parking is full")

        elif choice == '2':
            vehicle_number = input("Enter vehicle number: ")
            data = parking_lot.fetch_parking_spot(vehicle_number)
            if data: 
                print(f"Parking spot fetched: {data}")
            else:
                print("Vehicle not found.")

        elif choice == '3':
            print("Exit")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3")
