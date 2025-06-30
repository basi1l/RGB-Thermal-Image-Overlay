import os

folder = "input-images"  # This should match your folder name
files = os.listdir(folder)

# Get IDs for RGB and thermal images
rgb_ids = {f.replace("_Z.JPG", "") for f in files if f.endswith("_Z.JPG")}
thermal_ids = {f.replace("_T.JPG", "") for f in files if f.endswith("_T.JPG")}

# Find RGB images missing a thermal match
missing_thermal = sorted(rgb_ids - thermal_ids)

# Output results
print(f"\n✅ Total RGB images: {len(rgb_ids)}")
print(f"✅ Total thermal images: {len(thermal_ids)}")
print(f"❌ Missing thermal for {len(missing_thermal)} RGB images:\n")

for id in missing_thermal:
    print(f"{id}_Z.JPG")
