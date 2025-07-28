import base64

with open("background.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

with open("encoded_image.txt", "w") as output_file:
    output_file.write(encoded_string)

print("✅ Image has been encoded and saved to 'encoded_image.txt'")
