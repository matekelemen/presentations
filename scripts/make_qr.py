#!/usr/bin/env python3

# --- STD Imports ---
import argparse
import pathlib

# --- External Imports ---
try:
    import qrcode
except ImportError:
    import sys
    print("'qrcode' package is unavailable", file = sys.stderr)
    exit(1)


parser = argparse.ArgumentParser(pathlib.Path(__file__).stem)
parser.add_argument("url",
                    type = str,
                    help = "URL to encode in the QR code")
parser.add_argument("-o",
                    "--output",
                    dest = "output",
                    type = pathlib.Path,
                    required = True,
                    help = "Output path for the generated QR code image")

args = parser.parse_args()
qr = qrcode.QRCode(border = 4,
                   version = None,
                   error_correction = qrcode.ERROR_CORRECT_L,
                   box_size = 50)
qr.add_data(args.url)
qr.make(fit = True)

tubs_red = (190, 30, 60)
image = qr.make_image(fill_color = "black",
                      back_color = "white")

margin = qr.box_size * qr.border
image = image.crop((margin,
                    margin,
                    image.size[0] - margin,
                    image.size[1] - margin))
image.save(args.output)
