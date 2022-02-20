from PIL import Image
import os

### Input variables ###
image_path = "image_to_stuff.png"  # What image to stuff with data.
stuffing_path = "aftermath.png"    # The data you wish to stuff into an image - it can be any file.
output_path = "stuffed_image.png"  # Where to place the resultant image. Must be a png or other lossless format.
repeat_stuffing = False            # Whether to repeat the stuffing. Will not break most file formats.


def byte_to_bits(_byte: int) -> list[int]:
    bits = []
    for i in range(8):
        shift_amount = 7 - i
        mask = 1 << shift_amount
        bits.append((_byte & mask) >> shift_amount)
    return bits


def set_bit(_byte: int, index: int, set_to: bool):
    mask = 1 << index
    _byte &= ~mask
    if set_to:
        _byte |= mask
    return _byte


def stuff_image_lsb(image, stuffing, times):
    """
    This image does NOT do bounds checking, so you should ensure the stuffing can fit with the given values.

    :param image: Pillow image to stuff
    :param stuffing: list of bits to stuff with
    :param times: How many times to stuff the image.
    :return:
    """
    # As we're working in RGBA, bytes will always evenly split into pixels.
    image = image.convert("RGBA")
    w = image.width
    h = image.height
    stuffing_index = 0
    for y in range(h):
        for x in range(w):
            pixel = image.getpixel((x, y))
            new_pixel = []
            for channel in pixel:
                new_pixel.append(set_bit(channel, 0, stuffing[stuffing_index]))
                stuffing_index += 1
            image.putpixel((x, y), tuple(new_pixel))

            # Are we finished?
            if stuffing_index >= len(stuffing):
                times -= 1
                stuffing_index = 0
                if not times:
                    return image


def main():
    # Image info
    image = Image.open(image_path)
    w = image.width
    h = image.height
    available_bits = (w * h * 4)

    # stuffing info
    stuffing_bytes = os.path.getsize(stuffing_path)
    stuffing_fits = (available_bits // 8) // stuffing_bytes  # How many times we can stuff the file.

    # Will the stuffing fit into the image?
    if not stuffing_fits:
        print(f"Stuffing is too big to fit!\nIn bytes:\nStuffing size: {stuffing_bytes}\nAvailable space: {available_bits // 8}")
        exit()

    with open(stuffing_path, "rb") as f:
        dat = f.read()

    # This might be very bad for space, but it's quick to throw together
    stuffing = []
    for dat_byte in dat:
        stuffing += byte_to_bits(dat_byte)

    times_to_stuff = stuffing_fits if repeat_stuffing else 1
    image = stuff_image_lsb(image, stuffing, times_to_stuff)
    image.save(output_path)


if __name__ == "__main__":
    main()
