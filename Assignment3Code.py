def computeRectangleWallsArea():
    length = int(input("Enter the length of the room in feet:\n"))
    width = int(input("Enter the width of the room in feet:\n"))
    height = int(input("Enter the height of the room in feet:\n"))
    room_surface_area = (2 * calculateRectangleArea(length, width)) + (2 * calculateRectangleArea(length, height)) + (2 * calculateRectangleArea(height, width))
    return room_surface_area

def calculateRectangleArea(length, width):
    rec_area = length * width
    return rec_area

def computeSquareWallsArea():
    '''Asks the user to enter the side length of one walls side, calculates and returns the surface area of the 4 walls in the room.'''

    # Get the side length of one wall from the user
    side_length = float(
        input("Enter the length of one side of the room in feet:\n"))

    # Calculate the area of the 4 walls
    area_to_paint = 4 * computeSquareArea(side_length)

    # Calculate the area of the windows and doors
    windows_doors_area = computeWindowsDoorsArea()

    # Subtract the area of the windows and doors from the total area
    area_to_paint -= windows_doors_area

    return area_to_paint

def computeSquareArea(side_length):
    '''Takes one side length of a square and returns the value of its area'''
    area = side_length ** 2
    return area

def computeCustomWallsArea():
    pass

def computeWindowsDoorArea():
    '''Asks the user for the number of windows and doors in a room, then asks for the length and width of each door or window, and calculates the sum of areas of all doors and windows in the room'''

    # Get the number of windows and doors from the user
    number_of_windows_doors = int(
        input("How many windows and doors does the room contain? \n"))

    # Initialize the area to 0
    area = 0

    # Loop through the number of windows and doors
    for i in range(number_of_windows_doors):

        # Get the length and width of the window or door
        window_door_length = float(
            input(f"Enter window/door length for window/door {i+1} in feet:\n"))
        window_door_width = float(
            input(f"Enter window/door width for window/door {i+1} in feet:\n"))

        # Calculate the area of the window or door and add it to the total area
        area += window_door_length * window_door_width

    return area

def computeGallons(room_area):
    pass

def computePaintPrice(room_area):
    pass

def computeRoomArea(room_number):
    num_room = 1
    while(num_room <= room_number):
        print(f"Room: {num_room}")
        room_shape = int(input("Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom(more or less than 4 walls, all square or rectangles)\n"))
        if(room_shape == 1):
            room_area = computeRectangleWallsArea()
        elif(room_shape == 2):
            room_area = computeSquareWallsArea()
        elif(room_shape == 3):
            room_area = computeCustomWallsArea()
        else:
            print("Please enter an option from 1 to 3.")
            return
        windows_door_area = computeWindowsDoorArea()
        painted_area = room_area - windows_door_area
        print(f"For Room: {num_room}, the area to be painted is {painted_area:.1f} square ft and will require {(computeGallons(room_area)):.2f} to paint. This will cost the customer ${(computePaintPrice(room_area)):.2f}")
        num_room += 1

print("Welcome to Shiny Paint Company for indoor painting!")
room_number = int(input("How many Rooms do you want to paint:\n"))
print("Thank you!")
computeRoomArea(room_number)


