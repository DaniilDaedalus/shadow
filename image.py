from dataclasses import dataclass
from io import BufferedReader, BufferedWriter

from PIL import Image, ImageFilter


@dataclass
class Offset:
    x: int
    y: int


def blur(image: Image, iterations: int) -> Image:
    blurred_image = image
    for i in range(iterations):
        blurred_image = blurred_image.filter(ImageFilter.BLUR)

    return blurred_image


def make_shadow(
        image: Image,
        iterations: int,
        border_size: int,
        offset: Offset,
        background_color: str,
        shadow_color: str):

    # Calculate the size of the shadow's image
    image_width, image_height = image.size
    outer_width = image_width + abs(offset.x) + 2 * border_size
    outer_height = image_height + abs(offset.y) + 2 * border_size

    # Create the shadow's image. Match the parent image's mode.
    shadow = Image.new(
        image.mode, (outer_width, outer_height), background_color)

    # Place the shadow, with the required offset
    shadow_left = border_size + max(offset.x, 0)
    shadow_top = border_size + max(offset.y, 0)
    # Paste in the constant colour
    shadow.paste(
        shadow_color,
        [
            shadow_left, shadow_top,
            shadow_left + image_width,
            shadow_top + image_height,
        ],
    )

    shadow = blur(shadow, iterations)

    # Paste the original image on top of the shadow
    image_left = border_size - min(offset.x, 0)
    image_top = border_size - min(offset.y, 0)
    shadow.paste(image, (image_left, image_top))

    return shadow


def decorate_image(
        input_reader: BufferedReader,
        output_writer: BufferedWriter,
        iterations: int,
        border_size: int,
        offset: Offset,
        background_color: str,
        shadow_color: str):

    image = Image.open(input_reader)
    shadowed_image = make_shadow(
        image,
        iterations,
        border_size,
        offset,
        background_color,
        shadow_color,
    )

    shadowed_image.save(output_writer, 'PNG')
