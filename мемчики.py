from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")
top_text = input("введите вверхний текст: ")
bottom_text = input("введите нижний текст: ")

print(top_text,bottom_text)

print("список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")

player = int(input( "введите номер мема: " ))

if player == 1:
    image = "Кот в ресторане.png"
if player == 2:
    image = "Кот в очках.png"
print(image)

Image = Image.open(image)
width, height = Image.size

draw = ImageDraw.Draw(Image)

font = ImageFont.truetype("arial.ttf",size=70)

text = draw.textbbox((0,0), top_text, font)
text_widght = text[2]

draw.text(((width - text_widght) / 2,10),top_text,font=font, fill="black")

text = draw.textbbox((0, 0), bottom_text , font)
text_widght = text[2]
text_height = text[3]

draw.text(((width - text_widght) / 2, height - text_height - 10),bottom_text,font=font, fill="black")


Image.save("new_meme.jpg")