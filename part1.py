def computeCustomWallsArea():
    wall_number = int(input('Please enter the number of walls in the room:'))
    room_area = 0
    for x in range(wall_number):
        length = int(input('Enter the length of this room:'))
        width = int(input('Enter the width of this room:'))
        room_area += length * width
        return room_area


def computeGallons():
    gallons_need = computeRoomArea() / 350 
    print(f'This room will require {gallons_need} gallons to paint.')
    return gallons_need

def computePaintPrice():
    price = computeGallons() * 42
    print('This will cost the customer $',price)
    return price