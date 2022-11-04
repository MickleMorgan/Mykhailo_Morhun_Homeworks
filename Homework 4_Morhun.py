def task_1_house():
    FLOORS = 9
    ENTRANCES = 4
    ROOMS_ON_FLOOR = 4
    room_number = int(input("Please, enter the room number:"))
    amount_of_rooms = FLOORS * ENTRANCES * ROOMS_ON_FLOOR
    floor_sum = (room_number - 1) // ROOMS_ON_FLOOR + 1
    entrance = (floor_sum - 1) // FLOORS + 1
    floor = floor_sum - (entrance - 1) * FLOORS
    number_on_floor = (room_number - 1) % ROOMS_ON_FLOOR + 1
    print(room_number >= amount_of_rooms <= 1 and "There is no such flat in this house" or (room_number, entrance, floor
                                                                                            , number_on_floor))

def task_2_years():
    year = int(input("Please, enter a year:"))
    print((not(year % 4) and year % 100 or (not year % 400)) and "days in year - 366" or "days in year - 365")

def task_3_triangle():
    side_a, side_b, side_c = int(input("Side A:")), int(input("Side B:")), int(input("Side C:"))
    print((side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a) and "Good triangle"
          or "Bad Triangle")

