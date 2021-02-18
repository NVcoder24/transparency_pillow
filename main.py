from PIL import Image
from config import cfg

img = Image.open(cfg["input_file_name"])


def conv_rgba(image):
    return image.convert("RGBA")


def make_transparency(image, color, opacity):
    width = image.size[0]
    height = image.size[1]
    for x in range(0, width):
        for y in range(0, height):
            data = image.getpixel((x, y))
            if data[0] == color[0] and data[1] == color[1] and data[2] == color[2]:
                image.putpixel((x, y), (255, 255, 255, opacity))

    return image


img = make_transparency(conv_rgba(img), cfg["color"], cfg["opacity"])
img.save(cfg["output_file_name"])
if cfg["show_image"]:
    img.show()
