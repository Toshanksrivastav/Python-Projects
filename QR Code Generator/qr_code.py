import qrcode                         # QR code library
from qrcode.constants import ERROR_CORRECT_H  # High error correction

def generate_qr():
    data = input("Enter text / URL: ").strip()
    if not data:
        return                        # Stop if input is empty

    filename = input("Enter file name: ").strip() or "qr_code"

    fill_color = input("QR color: ").strip() or "black"
    back_color = input("Background color: ").strip() or "white"

    qr = qrcode.QRCode(
        version=1,                   # QR size
        error_correction=ERROR_CORRECT_H,  # Better scan reliability
        box_size=10,                 # Pixel size
        border=4                     # White border
    )

    qr.add_data(data)                # Add user data
    qr.make(fit=True)                # Generate QR

    img = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    )

    img.save(f"{filename}.png")      # Save image

if __name__ == "__main__":
    generate_qr()                    # Run program
