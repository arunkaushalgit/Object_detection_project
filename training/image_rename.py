import os

def rename_images(folder_path, prefix="test"):
    # Folder ke andar sab files list karo
    files = os.listdir(folder_path)

    # Sirf images (jpg, png, jpeg) filter karo
    images = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    # Images ko rename karo prefix + number ke saath
    for i, image_name in enumerate(images, start=1):
        ext = os.path.splitext(image_name)[1]  # extension nikal lo
        new_name = f"{prefix}{i}{ext}"
        src = os.path.join(folder_path, image_name)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f"Renamed {image_name} to {new_name}")

if __name__ == "__main__":
    folder = "/Users/winnovation/Downloads/Archive"  # yahan apna image folder ka path daalo
    rename_images(folder)
