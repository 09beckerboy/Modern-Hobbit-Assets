from PIL import Image, ImageEnhance
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def convert_image(root, file_path, filename):
    result_name = filename.split(".")[0]
    im = Image.open(file_path).convert('RGBA')
    print("Opened {0}".format(result_name))
    print("Converted {0} to RGBA".format(result_name))
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(1)
    im.putalpha(alpha)
    print("Transparency for {0} maxed".format(result_name))
    #im = im.transpose(Image.FLIP_TOP_BOTTOM)
    #print("{0} flipped".format(result_name))
    im.save("{0}/{1}.png".format(root, result_name))
    print("Saved {0}".format(result_name))
    os.remove(file_path)

for root, dirs, files in os.walk(script_dir):
    for filename in files:
        if filename.endswith(".dds"):
            file_path = os.path.join(root, filename)
            convert_image(root, file_path, filename)