from PIL import Image
from PIL.ExifTags import TAGS

def get_image_metadata(image_path):
    try:
        img = Image.open(image_path)
        exif_data = img._getexif()

        if exif_data is not None:
            metadata = {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                metadata[tag_name] = value

            return metadata
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def print_image_metadata(image_path):
    metadata = get_image_metadata(image_path)

    if metadata:
        print("Image metadata:")
        for tag, value in metadata.items():
            print(f"{tag}: {value}")
    else:
        print("The image contains no metadata.")

if __name__ == "__main__":
    while True:
        image_path = input("Enter image file path (termination: q):")

        if image_path.lower() == "q":
            break

        try:
            print_image_metadata(image_path)
        except FileNotFoundError:
            print("Error: File not found.")
        except Image.UnidentifiedImageError:
            print("Error: Invalid image file format.")
