import math

def get_player_pos() -> tuple[float, float, float]:
    coordinates: str = input("Enter new coodinates as floats in format 'x,y,z': ")
    separate: list[str] = coordinates.split(",")
    for parameter in separate:
        try:
            float(parameter)
        except ValueError as error:
            print(f"Error on parameter '{parameter}': {error}")
            get_player_pos()
    try:
        tuple_coord: tuple[float, float, float] = (float(separate[0]), float(separate[1]), float(separate[2]))
    except IndexError:
        print("Invalid syntax")
        get_player_pos()
    return tuple_coord



if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    tuple_coord: tuple[float, float, float] = get_player_pos()
    x: float = tuple_coord[0]
    y: float = tuple_coord[1]
    z: float = tuple_coord[2]
    print(f"Got a first tuple: {tuple_coord}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    center: int = round(math.sqrt(x ** 2 + y ** 2 + z ** 2), 4)
    print(f"Distance to the center: {center}")