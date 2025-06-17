# ZrgstImageBatch

## Planning

### Defining the flow
1. Prompt user for input directory
2. Display a menu to select wich edits to apply
    - Contrast
    - Sharpness
    - Exposure
    - Grayscale
    - The first 3 need numeric values
3. Prompt user for output directory
4. Process all images in source folder and output them in output-folder.

### Libraries
<os> or <pathlib> - To work with directories.
<os> first choice

<PIL>(from <pillow>) - To edit the images

<inquirer> or <questionary> - To create terminal based checkbox menus and prompts
(User friendly UI)

### Nessesary Functions i need

1. get_input_directory()
    - Uses <questionary> to let the user type or **browse** a folder path.
    - Checks if its valid (does it contain image files?)

2. get_edit_options()
    - Display a checklist menu
    - For options that need values (like contrast), prompt user afterward.

3. get_output_directory()
    - Same as input (1)

4. process_images(input_path, output_path, edits)
    - Loops through all images in folder.
    - Applies the selected edits
    - Saves to output directory

5. apply_edits(image, edits)
    - Takes a single image and applies the selected effects using <PIL>

### Identify where loops go
- In process_images(): We need to loop over each image in the input directory.
- In apply_edits() We need to check which edits were selecte and apply them conditionally.


## Summary
### Pseudo-code:
```python
def main():
    input_dir = get_input_directory()
    edits = get_edit_options()
    output_dir = get_output_directory()
    process_images(input_dir, output_dir, edits)
```
