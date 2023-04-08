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
    pass

def calculateSquareArea(side):
    pass

def computeCustomWallsArea():
    pass

def computeWindowsDoorArea():
    pass

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
