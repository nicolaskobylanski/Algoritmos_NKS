from Roomtype import HotelRoomType

class Room:
    """Python class to implement a basic version of a hotel room.
    
    This Python class implements the basic functionalities of a hotel room in a 
    simple hotel management system.
    
    Syntax
    ------
    obj = Room(room_type, room_number, room_state, room_price)
    
    Parameters
    ----------
    [in] room_type : Roomtype
        Valid values are "Individual", "Doble", "Suite".
    [in] room_number : int
        Unique number of the room.
    [in] room_state : str
        Occupancy state of the room. Expected values are "Ocupada" or "Desocupada".
    [in] room_price : float
        Price per night for the room.
    
    Returns
    -------
    obj : Room
        Python object output parameter that represents an instance of the class Room.
    
    Attributes
    ----------
    room_type : Roomtype
        Type of the room (e.g., "Individual", "Doble", "Suite").
    room_number : int
        Unique number of the room.
    room_state : str
        Occupancy state of the room ("Ocupada" or "Desocupada").
    room_price : float
        Price per night for the room.
    """

    def __init__(self, room_type: HotelRoomType, room_number: int, room_state: str, room_price: float):
        self.room_type = room_type
        self.room_number = room_number
        self.room_state = room_state
        self.room_price = room_price

    def is_occupied(self) -> bool:
        """Check if the room is occupied.

        Returns
        -------
        bool
            True if the room is occupied, False otherwise.
        """
        return self.room_state == "Ocupada"

    def check_in(self) -> str:
        """Check in the room.

        Returns
        -------
        str
            Message indicating the success or failure of the check-in operation.
        """
        if self.is_occupied():
            return "La habitación ya está ocupada."
        else:
            self.room_state = "Ocupada"
            return "Check-in realizado con éxito."

    def check_out(self) -> str:
        """Check out of the room.

        Returns
        -------
        str
            Message indicating the success or failure of the check-out operation.
        """
        if not self.is_occupied():
            return "La habitación ya está desocupada."
        else:
            self.room_state = "Desocupada"
            return "Check-out realizado con éxito."

def main():
    # TESTING
    print("=================================================================")
    print("Test Case 1: Create a Room.")
    print("=================================================================")
    room1 = Room(HotelRoomType.DOBLE, 101, "Desocupada", 150)

    if room1.room_type == HotelRoomType.DOBLE:
        print("Test PASS. The parameter room_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__() for room_type.")

    if room1.room_number == 101:
        print("Test PASS. The parameter room_number has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__() for room_number.")

    if room1.room_state == "Desocupada":
        print("Test PASS. The parameter room_state has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__() for room_state.")

    if room1.room_price == 150:
        print("Test PASS. The parameter room_price has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__() for room_price.")


    print("=================================================================")
    print("Test Case 2: Check-in a Room.")
    print("=================================================================")
    room2 = Room(HotelRoomType.SUITE, 102, "Desocupada", 300)
    check_in_result = room2.check_in()

    if check_in_result == "Check-in realizado con éxito." and room2.is_occupied():
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in() for occupancy.")


    print("=================================================================")
    print("Test Case 3: Check-out a Room.")
    print("=================================================================")
    # Assuming room2 was checked in from the previous test
    check_out_result = room2.check_out()

    if check_out_result == "Check-out realizado con éxito." and not room2.is_occupied():
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out() for vacancy.")


    print("=================================================================")
    print("Test Case 4: Attempt Check-in on an Occupied Room.")
    print("=================================================================")
    room3 = Room(HotelRoomType.INDIVIDUAL, 103, "Ocupada", 100)
    check_in_result = room3.check_in()

    if check_in_result == "La habitación ya está ocupada.":
        print("Test PASS. Attempted check-in on an occupied room handled correctly.")
    else:
        print("Test FAIL. Check the method check_in() for occupied rooms.")


    print("=================================================================")
    print("Test Case 5: Attempt Check-out on a Vacant Room.")
    print("=================================================================")
    # Assuming room3 was made vacant from the previous operation or is initially vacant
    room4 = Room(HotelRoomType.DOBLE, 104, "Desocupada", 200)
    check_out_result = room4.check_out()

    if check_out_result == "La habitación ya está desocupada.":
        print("Test PASS. Attempted check-out on a vacant room handled correctly.")
    else:
        print("Test FAIL. Check the method check_out() for vacant rooms.")

if __name__ == "__main__":
    main()