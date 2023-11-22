# import cv2
# import numpy as np

# # Load the image
# img = cv2.imread('Alaska-Outline-Map.jpg')

# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Threshold input image as a mask
# mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]

# # Negate mask
# mask = 255 - mask

# # Apply morphology to remove isolated extraneous noise
# # Use borderconstant of black since the foreground touches the edges
# kernel = np.ones((3, 3), np.uint8)
# mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# # Anti-alias the mask -- blur then stretch
# # Blur alpha channel
# mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=2, sigmaY=2, borderType=cv2.BORDER_DEFAULT)

# # Linear stretch so that 127.5 goes to 0, but 255 stays 255
# mask = (2 * (mask.astype(np.float32)) - 255.0).clip(0, 255).astype(np.uint8)

# # Put the mask into the alpha channel
# result = img.copy()
# result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
# result[:, :, 3] = mask

# # Save the intermediate result with alpha channel preserved
# cv2.imwrite('intermediate_result.png', result)

# # Now, load the intermediate result for black-to-blue pixel conversion
# image_with_alpha = cv2.imread('intermediate_result.png', cv2.IMREAD_UNCHANGED)

# # Define the RGB values for black and blue
# black_lower = np.array([0, 0, 0, 0], dtype=np.uint8)
# black_upper = np.array([10, 10, 10, 255], dtype=np.uint8)
# blue_color = np.array([255, 0, 0, 255], dtype=np.uint8)

# # Create a binary mask for black pixels
# black_mask = cv2.inRange(image_with_alpha, black_lower, black_upper)

# # Replace black pixels with blue pixels
# image_with_alpha[black_mask > 0] = blue_color

# # Save the final result with alpha channel preserved
# cv2.imwrite('final_output.png', image_with_alpha)

# # Display result, though it won't show transparency
# cv2.imshow("INPUT", img)
# cv2.imshow("GRAY", gray)
# cv2.imshow("MASK", mask)
# cv2.imshow("INTERMEDIATE RESULT", result)
# cv2.imshow("FINAL OUTPUT", image_with_alpha)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
import os

# Function to process each image
def process_image(image_path, output_folder):
    # Load the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold input image as a mask
    mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]

    # Negate mask
    mask = 255 - mask

    # Apply morphology to remove isolated extraneous noise
    # Use borderconstant of black since the foreground touches the edges
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Anti-alias the mask -- blur then stretch
    # Blur alpha channel
    mask = cv2.GaussianBlur(mask, (0, 0), sigmaX=2, sigmaY=2, borderType=cv2.BORDER_DEFAULT)

    # Linear stretch so that 127.5 goes to 0, but 255 stays 255
    mask = (2 * (mask.astype(np.float32)) - 255.0).clip(0, 255).astype(np.uint8)

    # Put the mask into the alpha channel
    result = img.copy()
    result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
    result[:, :, 3] = mask

    # Now, load the intermediate result for black-to-blue pixel conversion
    image_with_alpha = result  # Use the result from the background removal

    # Define the RGB values for black and blue
    black_lower = np.array([0, 0, 0, 0], dtype=np.uint8)
    black_upper = np.array([10, 10, 10, 255], dtype=np.uint8)
    blue_color = np.array([255, 0, 0, 255], dtype=np.uint8)

    # Create a binary mask for black pixels
    black_mask = cv2.inRange(image_with_alpha, black_lower, black_upper)

    # Replace black pixels with blue pixels
    image_with_alpha[black_mask > 0] = blue_color

    # Save the final output with a modified filename
    output_path = os.path.join(output_folder, f'{os.path.splitext(os.path.basename(image_path))[0]}_output.png')
    cv2.imwrite(output_path, image_with_alpha)

    # Display result, though it won't show transparency
    # cv2.imshow("INPUT", img)
    # cv2.imshow("MASK", mask)
    # cv2.imshow("FINAL OUTPUT", image_with_alpha)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# Specify the folder containing your images
folder_path = 'USA'

# Create an 'output' subfolder if it doesn't exist
output_folder = os.path.join(folder_path, 'output')
os.makedirs(output_folder, exist_ok=True)

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Assuming you're working with jpg or png files
        # Construct the full path to the image
        image_path = os.path.join(folder_path, filename)

        # Process the image
        process_image(image_path, output_folder)
