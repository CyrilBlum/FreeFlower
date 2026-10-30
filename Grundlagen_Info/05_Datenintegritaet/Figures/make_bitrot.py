"""Erzeugt bitrot.jpg: ein JPEG, in dessen Bilddaten einzelne Bits gekippt werden.

Aufruf: python3 make_bitrot.py <original.jpg> <ausgabe.jpg>
Das Ergebnis wird mit ImageMagick neu kodiert, damit der Fehler fest im Bild steht
und nicht je nach PDF-Betrachter anders dargestellt wird.
"""
import random
import subprocess
import sys
import tempfile

FLIPS = 3  # Anzahl gekippter Bits
SEED = 11  # fester Startwert, damit das Bild reproduzierbar bleibt

source, target = sys.argv[1], sys.argv[2]
data = bytearray(open(source, "rb").read())

# Nur die komprimierten Bilddaten nach dem Marker «Start of Scan» verändern
start = data.index(b"\xff\xda") + 2 + int.from_bytes(data[data.index(b"\xff\xda") + 2:data.index(b"\xff\xda") + 4], "big")

random.seed(SEED)
for _ in range(FLIPS):
    position = random.randrange(start + (len(data) - start) // 6, len(data) - 2)
    data[position] ^= 1 << random.randrange(8)

with tempfile.NamedTemporaryFile(suffix=".jpg") as damaged:
    damaged.write(data)
    damaged.flush()
    subprocess.run(["magick", damaged.name, "-quality", "85", target], check=True)
