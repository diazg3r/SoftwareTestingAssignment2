
from pathlib import Path
from analyzer import analyze_code


# Display the main menu
def show_menu():
    print("\nOO METRICS TESTING TOOL")
    print("-----------------------")
    print("1. Analyze a Python file")
    print("2. Paste Python code")
    print("3. Exit")


# Option 1: Analyze a Python file
def analyze_file():
    file_path = input("\nEnter the Python file path: ").strip()

    try:
        source_code = Path(file_path).read_text(encoding="utf-8")
        analyze_code(source_code)

    except FileNotFoundError:
        print("Error: The file was not found.")

    except IsADirectoryError:
        print("Error: Please provide a file, not a directory.")

    except UnicodeError:
        print("Error: The file could not be read as UTF-8 text.")

    except OSError as error:
        print(f"Error reading file: {error}")

    except SyntaxError as error:
        print(f"Error: Invalid Python syntax: {error}")


# Option 2: Analyze pasted Python code
def analyze_pasted_code():
    print("\nPaste your Python code below.")
    print("Type END on a separate line when finished:\n")

    lines = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    source_code = "\n".join(lines)

    if not source_code.strip():
        print("Error: No Python code was provided.")
        return

    try:
        analyze_code(source_code)

    except SyntaxError as error:
        print(f"Error: Invalid Python syntax: {error}")


# Main application
def main():
    while True:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            analyze_file()

        elif choice == "2":
            analyze_pasted_code()

        elif choice == "3":
            print("Exiting the application...")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


# Start the application
if __name__ == "__main__":
    main()
