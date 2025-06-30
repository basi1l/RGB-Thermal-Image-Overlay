import cv2
import numpy as np
import os

# ==== Configuration ====
INPUT_DIR = "input-images"          # Folder with XXXX_T.JPG and XXXX_Z.JPG
OUTPUT_DIR = "task_1_output"        # Folder for XXXX_AT.JPG output

# ==== Ensure output directory exists ====
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==== Find matching image pairs ====
def get_image_pairs(folder):
    files = os.listdir(folder)
    thermal_files = [f for f in files if f.endswith("_T.JPG")]
    rgb_files = [f for f in files if f.endswith("_Z.JPG")]
    
    pairs = []
    for t_file in thermal_files:
        base_name = t_file.replace("_T.JPG", "")
        z_file = base_name + "_Z.JPG"
        if z_file in rgb_files:
            pairs.append((os.path.join(folder, t_file), os.path.join(folder, z_file), base_name))
    return pairs

# ==== Align thermal image by resizing ====
def align_thermal_to_rgb(thermal, rgb):
    resized_thermal = cv2.resize(thermal, (rgb.shape[1], rgb.shape[0]))
    return resized_thermal

# ==== Overlay using color map and transparency ====
def overlay_images(rgb, aligned_thermal):
    # Convert to grayscale then apply colormap
    gray_thermal = cv2.cvtColor(aligned_thermal, cv2.COLOR_BGR2GRAY)
    color_thermal = cv2.applyColorMap(gray_thermal, cv2.COLORMAP_JET)
    
    # Blend images
    blended = cv2.addWeighted(rgb, 0.7, color_thermal, 0.3, 0)
    return blended

# ==== Main process ====
def process_all_images():
    pairs = get_image_pairs(INPUT_DIR)
    if not pairs:
        print("No matching image pairs found.")
        return

    print(f"Found {len(pairs)} image pairs. Processing...")

    for thermal_path, rgb_path, base in pairs:
        thermal = cv2.imread(thermal_path)
        rgb = cv2.imread(rgb_path)

        if thermal is None or rgb is None:
            print(f"Skipping {base} due to read error.")
            continue

        aligned_thermal = align_thermal_to_rgb(thermal, rgb)
        overlaid_image = overlay_images(rgb, aligned_thermal)

        output_path = os.path.join(OUTPUT_DIR, f"{base}_AT.JPG")
        cv2.imwrite(output_path, overlaid_image)
        print(f"Saved: {output_path}")

if __name__ == "__main__":
    process_all_images()
