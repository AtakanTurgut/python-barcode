import barcode
from barcode.writer import ImageWriter

text0 = "Atakan Turgut"
text1 = str(text0)

code = barcode.get_barcode_class("code128")

image = code(text0, writer=ImageWriter())

save_img = image.save('AtakanTurgutBarcode')