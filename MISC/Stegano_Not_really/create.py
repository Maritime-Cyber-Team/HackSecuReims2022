from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import base64

img = Image.open("./medias/original.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("./medias/Roboto-Regular.ttf", 12)

message = "Je protégeais jadis le plus grand port militaire d'europe"

message_bytes = message.encode("utf8")
  
base64_bytes = base64.b64encode(message_bytes)
base64_string = base64_bytes.decode("ascii")

draw.text((0, 0),base64_string,(255,255,255),font=font)
img.save('./medias/not_stegano.jpg')