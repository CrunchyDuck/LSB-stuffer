from PIL import Image

### Input variables ###
image_path = "stuffed_image.png"     # Image to unstuff
output_path = "unstuffed_image.png"  # Where to place unstuffed data.




image = Image.open(image_path)
unstuffed_bits = []

print("Unstuffing image...")
for y in range(image.height):
    for x in range(image.width):
        pixel = image.getpixel((x, y))
        for channel in pixel:
            unstuffed_bits.append(channel & 1)
print("Finished unstuffing...")
print("Converting to bytes...")
unstuffed_bytes = []
for i in range(len(unstuffed_bits) // 8):
    byte_bits = unstuffed_bits[i * 8: i * 8 + 9]
    byte = 0
    for j in range(8):
        byte |= byte_bits[j] << (7 - j)
    unstuffed_bytes.append(byte)
print("Finished converting...")
print("Writing to file...")
with open(output_path, "wb") as f:
    for b in unstuffed_bytes:
        f.write(b.to_bytes(1, "big"))
