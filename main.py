# Import the necessary libraries
import os
from PIL import Image, ImageEnhance
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
# Define funtion to get the output directory
def get_output_directory():
    while True:
        path_str = questionary.text("Please enter path to the directory you want the pictures saved to:").ask()
        if path_str is None:
            print("No input provided. Exiting...")
            sys.exit(0)
        
        path = Path(path_str)
        
        if path.exists() and not path.is_dir():
            print("That is not a directory.")
        else:
            if not path.exists():
                create = questionary.confirm(
                        "That direcory does not exist. Create it?"
                ).ask()

                if not create:
                    retry = questionary.select(
                            "What would you like to do?",
                            choices =["Try another path", "Quit"]
                    ).ask()

                    if retry == "Quit":
                        print("Exiting program...")
                        sys.exit(0)
                    continue #retry loop

                path.mkdir(parents=True)

            return path
######################################################
# Defining the core engine, image processing:
def process_images(input_path, output_path, edits):
    for image_file in input_path.glob("*"):
        if image_file.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
            continue #Skip non-image files

        try:
            image = Image.open(image_file)

            # Apply edits:
            edited_image = apply_edits(image, edits)

            # Save to output path:
            output_file = output_path / image_file.name
            edited_image.save(output_file)
            print(f"Saved: {output_file.name}")

        except Exception as e:
            print(f"Failed to process {image_file.name}: {e}")


######################################################
    # Define helper funtion to apply the edits:
def apply_edits(image, edits):
        result = image

        if "contrast" in edits:
            enhancer = ImageEnhance.Contrast(result)
            result = enhancer.enhance(edits["contrast"])

        if "sharpness" in edits:
            enhancer = ImageEnhance.Sharpness(result)
            result = enhancer.enhance(edits["sharpness"])

        if "exposure" in edits:
            enhancer = ImageEnhance.Brightness(result)
            result = enhancer.enhance(edits["exposure"])

        if edits.get("grayscale"):
            result = result.convert("L") #Grayscale

        return result

######################################################
def main():
        input_dir = get_input_directory()
        edits = get_edit_options()
        output_dir = get_output_directory()
        process_images(input_dir, output_dir, edits)

#######################################################
if __name__ == "__main__":
    main()    
    #output_path = get_output_directory() # TEST OK
    #print(f"Output directory: {output_path}") # TEST OK
    #input_path = get_input_directory() # - TEST OK
    #print(f"Selected input directory: {input_path}") #  - TEST OK
    #options = get_edit_options() # - TEST OK
    #print("You selected:") # - TEST OK
    #print(options) # - TEST OK

##############################################

