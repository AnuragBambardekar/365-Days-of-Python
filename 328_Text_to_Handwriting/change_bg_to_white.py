from PIL import Image
import os

def change_color(input_folder, output_folder, target_color=(245, 240, 236)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image (you may want to add more checks based on your specific use case)
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Open the image
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)

            # Convert the image to RGBA mode (if not already in RGBA)
            img = img.convert("RGBA")

            # Get the width and height of the image
            width, height = img.size

            # Loop through each pixel in the image
            for x in range(width):
                for y in range(height):
                    # Get the RGBA values of the current pixel
                    r, g, b, a = img.getpixel((x, y))

                    # Check if the pixel color is not transparent
                    if a != 0:
                        # Change the color to the target color
                        img.putpixel((x, y), target_color + (a,))

            # Save the new image to the output folder
            output_path = os.path.join(output_folder, filename)
            img.save(output_path)

if __name__ == "__main__":
    input_folder = "op"
    output_folder = "op2"

    change_color(input_folder, output_folder)
