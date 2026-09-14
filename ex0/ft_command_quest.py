import sys


if __name__ == "__main__":
    try:
        total_count: int = len(sys.argv)
        program_name: str = sys.argv[0].split("/")[-1]
        sys.argv.pop(0)
        print("=== Command Quest ===")
        print(f"Program name: {program_name}")
        if len(sys.argv) == 0:
            print("No arguments provided!")
        else:
            print(f"Arguments received: {len(sys.argv)}")
            for arg_num, arg in enumerate(sys.argv, 1):
                print(f"Argument {arg_num}: {arg}")
        print(f"Total arguments: {total_count}")
    except Exception as e:
        print(f"An error occurred: {e}")
