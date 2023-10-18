from PIL import Image, ImageDraw

image = Image.new('RGB', (1000, 1000), 'pink')
draw = ImageDraw.Draw(image)

draw.rectangle((100, 100, 300, 300), fill='magenta')

image.save('scripts/Lab002/pillow001.png')