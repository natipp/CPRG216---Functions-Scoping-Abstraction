
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


def computeWindowsDoorsArea():
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
