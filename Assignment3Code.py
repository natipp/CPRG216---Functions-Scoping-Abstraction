# Description:      This program calculates the amount of paint and money needed in order to paint a given room.
#                   The room can be rectangular, square, or custom.
#
# Team Members:     Nathalia P., Anna R., Jubril S.
#
# Date:             April 9th, 2023
#
# Inputs:           The user will choose how many rooms need to be calculated, the shape of the room, the dimensions
#                   of the room, number of windows/door in the room, and the size of those windows.
#
# Outputs:          For each room it will output the total area to be painted, the amount of paint needed, and the cost of the job.
#                   At the end, it will also calculate a total for all of the rooms.


def computeRectangleWallsArea():
    '''Asks the user to enter the length, width and height of the rectangular room, 
    calculates and returns the walls surface area to be painted'''

    # Get the length, width and height of the room from the user
    length = float(input("Enter the length of the room in feet:\n"))
    width = float(input("Enter the width of the room in feet:\n"))
    height = float(input("Enter the height of the room in feet:\n"))

    # Calculate the area of the 4 walls
    room_surface_area = 2 * \
        (calculateRectangleArea(length, height) +
         calculateRectangleArea(width, height))

    # Calculate the area of the windows and doors
    windows_doors_area = computeWindowsDoorArea()

    # Subtract the area of the windows and doors from the total area
    painted_area = room_surface_area - windows_doors_area

    return painted_area


def calculateRectangleArea(length, width):
    '''Takes the length and width of a rectangle and returns the value of its area'''
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
    windows_doors_area = computeWindowsDoorArea()

    # Subtract the area of the windows and doors from the total area
    area_to_paint -= windows_doors_area

    return area_to_paint


def computeSquareArea(side_length):
    # Takes one side length of a square and returns the value of its area
    area = side_length ** 2
    return area


def computeCustomWallsArea():
    '''Asks the user to enter the number of walls in the room, then ask for the height and length of each wall in order to calculate the room area, and then return the room area'''

    # Get the number of walls from the user
    number_of_walls = int(input("How many walls are there in the room \n"))

    # Initialize the area to 0
    area_to_paint = 0

    # Loop through the number of walls
    for i in range(number_of_walls):

        # Get the height and length of the wall from the user
        wall_height = float(
            input(f"Enter the height of wall {i+1} in feet:\n"))
        wall_length = float(
            input(f"Enter the length of wall {i+1} in feet:\n"))

        # Calculate the area of the wall and add it to the total area
        area_to_paint += wall_height * wall_length

    # Calculate the area of the windows and doors
    windows_doors_area = computeWindowsDoorArea()

    # Subtract the area of the windows and doors from the total area
    area_to_paint -= windows_doors_area

    return area_to_paint


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
    '''Takes the area as a parameter and returns the number of gallons of paint needed'''
    square_feet_per_gallon = 350
    return room_area / square_feet_per_gallon


def computePaintPrice(room_area):
    '''Takes the area as a parameter and returns the price of the gallons of paint needed'''
    paint_price_per_gallon = 42
    return computeGallons(room_area) * paint_price_per_gallon


def computeRoomArea(room_number):
    num_room = 1
    total_painted_area = 0
    total_paint_used = 0
    total_price = 0

    # Keep looping until the total number of rooms are reached
    while (num_room <= room_number):
        print(f"Room: {num_room}")

        # Prompt the user to select the shape of the room
        room_shape = int(input(
            "Select the shape of the room:\n1 - Rectangular\n2 - Square\n3 - Custom(more or less than 4 walls, all square or rectangles)\n"))

        # Handle the user's selection
        if (room_shape == 1):
            painted_area = computeRectangleWallsArea()
        elif (room_shape == 2):
            painted_area = computeSquareWallsArea()
        elif (room_shape == 3):
            painted_area = computeCustomWallsArea()
        else:
            print("Please enter an option from 1 to 3.")
            return

        # Calculate the number of gallons and price
        paint_gallon = computeGallons(painted_area)
        paint_price = computePaintPrice(painted_area)

        # Print the results
        print(f"For Room: {num_room}, the area to be painted is {painted_area:.1f} square ft and will require {paint_gallon:.2f} gallons to paint. This will cost the customer ${paint_price:.2f}")

        total_painted_area += painted_area
        total_paint_used += paint_gallon
        total_price += paint_price
        num_room += 1
    # print the total results
    print(
        f"Area to be painted is {total_painted_area:.2f} square ft and will require {total_paint_used:.2f} gallons to paint. This will cost the customer ${total_price:.2f}")


# Welcome message
print("Welcome to Shiny Paint Company for indoor painting!")

# Get user input and handle input
room_number = int(input("How many Rooms do you want to paint:\n"))
print("Thank you!")
computeRoomArea(room_number)
