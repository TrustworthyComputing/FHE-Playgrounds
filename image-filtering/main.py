# Convert an RGB image represented as three separate arrays for R, G, and B components to grayscale using a simple filter.
import sys
from PIL import Image


def rgb_to_grayscale(r, g, b, width, height):
    assert len(r) == len(g) == len(b) == width * height, "Arrays must have the same dimensions."
    grayscale_image = [0 for _ in range(width * height)]

    for i in range(width * height):
        red, green, blue = r[i], g[i], b[i]
        grayscale_value = (1224 * red + 2404 * green + 475 * blue)

        grayscale_image[i] = grayscale_value
    return grayscale_image


def png_to_rgb_arrays(png_file):
    image = Image.open(png_file)
    image = image.convert('RGB')
    width, height = image.size

    r_values, g_values, b_values = [], [], []
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            r_values.append(r)
            g_values.append(g)
            b_values.append(b)
    return r_values, g_values, b_values, width, height


def rgb_to_png(grayscale_values, width, height, output_file):
    assert len(grayscale_values) == width * height, "Array must have the same dimensions as width x height."

    output_image = Image.new('RGB', (width, height))
    for i in range(width * height):
        grayscale_value = grayscale_values[i]
        output_image.putpixel((i % width, i // width), (grayscale_value, grayscale_value, grayscale_value))
    output_image.save(output_file)


def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input.png")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.replace(".png", "_gray.png")

    r_values, g_values, b_values, width, height = png_to_rgb_arrays(input_file)

    print('r_values', r_values)
    print('g_values', g_values)
    print('b_values', b_values)
    print('width', width)
    print('height', height)

    grayscale_values = rgb_to_grayscale(r_values, g_values, b_values, width, height)

    print('grayscale_values', grayscale_values)
    for i in range(len(grayscale_values)):
        grayscale_values[i] >>= 12
    print('grayscale_values', grayscale_values)


    rgb_to_png(grayscale_values, width, height, output_file)
    print(f"Grayscale image saved as {output_file}")


if __name__ == "__main__":
    main()
