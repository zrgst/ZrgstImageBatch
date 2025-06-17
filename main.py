# Import the necessary libraries
import os
#from pillow import PIL
import questionary
from pathlib import Path
import sys

#############################################################
# Defining the input directory:
def get_input_directory():
    # Prompt user to select a path
    while True:
        path_str: str = questionary.text("Enter the path to your images:").ask()
        
        # Checking if user inputs data
        if path_str is None:
            print("No input provided. Exiting...")
            sys.exit(0)
        
        # Using pathlib's Path to convert string to a path
        path = Path(path_str)
        
        # Checking if it is a valid path
        if not path.exists():
            print("That path does not exist. Please try again.")
        elif not path.is_dir():
            print("That is not a directory. Please try again")
        elif not any(path.glob("*.jpg")) and not any(path.glob("*.png")) and not any(path.glob("*.jpeg")):
            print("No images of type .jpg, .jpeg og .png found. Try another directory.")
        else:
            return path # Valid path

        # Invalid input - offer retry/quit
        retry = questionary.select(
                "What would you like to do?",
                choices=["Retry", "Exit"]
        ).ask()

        if retry == "Exit":
            print("Exiting program.")
            sys.exit(0)
##############################################################

# Defining the edits function:
def get_edit_options():
    # Step 1: Let the user decide what edits to enable:
    choices = questionary.checkbox(
        "Select the edits you want to apply:",
    choices=[
        "Contrast",
        "Sharpness",
        "Exposure",
        "Grayscale"
        ]
    ).ask()

    if not choices:
        print("No edits selected.")
        return {}
    
    edits = {}
    
    # Step 2: For each choice, sk for a value if needed
    if "Contrast" in choices:
        value = questionary.text("Enter Contrast level (e.g., 1.0 = no change):").ask()
        edits["contrast"] = float(value)

    if "Sharpness" in choices:
        value = questionary.text("Enter Sharpness level (e.g., 1.0 = no change)").ask()
        edits["sharpness"] = float(value)

    if "Exposure" in choices:
        value = questionary.text("Enter Exposure level (e.g., 1.0 = no change)").ask()
        edits["exposure"] = float(value)

    if "Grayscale" in choices:
        edits["grayscale"] = True

    return edits
############################################################################


if __name__ == "__main__":
    #input_path = get_input_directory() - TEST OK
    #print(f"Selected input directory: {input_path}") - TEST OK
    #options = get_edit_options() - TEST OK
    #print("You selected:") - TEST OK
    #print(options) - TEST OK



