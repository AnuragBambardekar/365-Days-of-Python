from PIL import Image
import os

def resize_images(input_folder, output_folder, target_resolution=(80, 115)):
    # Make sure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image
        image = Image.open(input_path)

        # Resize the image to the target resolution
        resized_image = image.resize(target_resolution, Image.ANTIALIAS)

        # Save the resized image to the output folder
        resized_image.save(output_path)

if __name__ == "__main__":
    # Replace 'input_folder' and 'output_folder' with your actual folder paths
    input_folder = "myfont"
    output_folder = "op"

    # Set the target resolution
    target_resolution = (80, 115)

    resize_images(input_folder, output_folder, target_resolution)
