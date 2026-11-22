import qrcode
while True:
    data = input("Enter the name of the URL to be converted into a QR code: ").strip()
    if data:
        break
    else:
        print("URL name cannot be EMPTY!")
while True:
    filename = input("Enter the filename: ").strip()
    if filename:
        break
    else:
        print("FILENAME name cannot be EMPTY!")


print("\nChoose QR code color: ")
print("1. Black")
print("2. Blue")
print("3. Red")
print("4. Green")

while True:
    color_choice = input("Enter your colour choice(1 - 4): ")
    colors = {
    "1": "black",
    "2": "blue",
    "3": "red",
    "4": "green"
 }
    if color_choice in colors:
        fill_color=colors[color_choice]
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

while True:
    try:
        size = int(input("Enter the size of the QR(1 - 10): "))
        if 1 <= size <= 10:
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 10.")
    except ValueError:
        print("Please enter a valid number.")


try:
    qr = qrcode.QRCode(
        version = 1,
        box_size = size,
        border = 4
    )
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color=fill_color, back_color="white")
    image.save(filename + ".png")
    print(f"\nQR code successfully saved as {filename}.png")

except Exception as e:
    print(f"Something went wrong: {e}")