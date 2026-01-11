import qrcode

textoyaya = input ("Dime el texto para el QR yaya: ")
img = qrcode.make(textoyaya)

textoimg = input("Dime el texto para el QR yaya: ")
img.save (textoimg +".png")