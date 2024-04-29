from PIL import Image
import os

def convert_image(image_file, name):
    im = Image.open(image_file)
    print("Opened image")
    im = im.convert('RGBA')
    print("Converted to RGBA")
    data = im.getdata()
    new_data = []
    for item in data:
        new_data.append((*item[:3], 255))
    im.putdata(new_data)
    print("Transparency maxed")
    im = im.transpose(Image.FLIP_TOP_BOTTOM)
    print("Image flipped")
    im.save(name+".png")
    print("Saved image")

directory = os.getcwd()
for filename in os.listdir(directory):
    if filename.endswith(".dds"):
        file_path = os.path.join(directory, filename)
        result_name = filename.split(".")[0]
        convert_image(file_path, result_name)
        continue
    else:
        continue