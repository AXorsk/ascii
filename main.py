from PIL import Image, ImageDraw, ImageFont
import argparse
import numpy as np

sample_rate = 1


def code(file, op):
    im = Image.open("input/" + file)

    # font = ImageFont.load_default()
    font = ImageFont.truetype("fonts/SourceCodePro-Bold.ttf", size=12)
    aspect_ratio = font.getbbox("x")[2] / font.getbbox("x")[3]
    new_im_size = np.array(
        [im.size[0] * sample_rate, im.size[1] * sample_rate * aspect_ratio]
    ).astype(int)

    im = im.resize(new_im_size)
    im_color = np.array(im)
    im = im.convert("L")
    im = np.array(im)

    color_set = list(r"@BMH&8AG%h#$521sir;:,. ")
    symbols, bg_color = np.array([]), ""
    if op == 1:
        symbols = np.array(color_set)
        bg_color = "white"
    else:
        symbols = np.array(color_set[::-1])
        bg_color = "black"

    im_min = im.min()
    im_max = im.max()
    if im_min == im_max:
        im = np.zeros_like(im)
    else:
        im = (im - im_min) / (im_max - im_min) * (symbols.size - 1)
    
    ascii = symbols[im.astype(int)]

    letter_size = font.getbbox("x")[2:4]
    im_out_size = new_im_size * letter_size
    im_out = Image.new("RGB", tuple(im_out_size), bg_color)
    draw = ImageDraw.Draw(im_out)

    y = 0
    for i, line in enumerate(ascii):
        for j, ch in enumerate(line):
            color = tuple(im_color[i, j])
            draw.text((letter_size[0] * j, y), ch[0], fill=color, font=font)
        y += letter_size[1]

    if op == 1:
        im_out.save("output/b_" + file)
    else:
        im_out.save("output/w_" + file)
    print("Done!")
        

if __name__ == "__main__":
    file_name = ""
    code(file_name, 1)
    code(file_name, 2)