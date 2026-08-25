import math

class IndexError(Exception):
     


def get_player_pos() -> tuple[float, float, float]:
    coordinates: str = input("Enter new coodinates as "
                             "floats in format 'x,y,z': ")
    separate: list[str] = coordinates.split(",")
    if len(separate) > 3 or len(separate) < 3
            print("Invalid syntax")
            return get_player_pos()
    for parameter in separate:
        try:
            float(parameter)
        except ValueError as error:
            print(f"Error on parameter '{parameter}': {error}")
            return get_player_pos()
    try:
        tuple_coord: tuple[float, float, float] = (float(separate[0]), float(separate[1]), float(separate[2]))
    except IndexError:
        print("Invalid syntax")
        return get_player_pos()
    return tuple_coord


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_tuple_coord: tuple[float, float, float] = get_player_pos()
    first_x: float = first_tuple_coord[0]
    first_y: float = first_tuple_coord[1]
    first_z: float = first_tuple_coord[2]
    print(f"Got a first tuple: {first_tuple_coord}")
    print(f"It includes: X={first_x}, Y={first_y}, Z={first_z}")
    first_center: float = round(math.sqrt(first_x ** 2 + first_y ** 2 + first_z ** 2), 4)
    print(f"Distance to center: {first_center}\n")

    print("Get a second set of coordinates")
    second_tuple_coord: tuple[float, float, float]= get_player_pos()
    second_x: float = second_tuple_coord[0]
    second_y: float = second_tuple_coord[1]
    second_z: float = second_tuple_coord[2]
    distance: float = round(math.sqrt(((second_x - first_x) ** 2) + (second_y - first_y) ** 2 + (second_z - first_z) ** 2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")
