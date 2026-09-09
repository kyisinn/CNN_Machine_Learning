from PIL import Image, ImageOps, ImageDraw
import glob, os

files = sorted(glob.glob('tmp/pdfs/ml6_review/slide-*.png'))
for batch in range(0, len(files), 12):
    selected = files[batch:batch+12]
    sheet = Image.new('RGB', (1600, 900), 'white')
    draw = ImageDraw.Draw(sheet)
    for j, fn in enumerate(selected):
        im = Image.open(fn).convert('RGB')
        im.thumbnail((380, 250))
        x = (j % 4) * 400 + 10
        y = (j // 4) * 300 + 25
        sheet.paste(im, (x, y))
        draw.text((x, 5 + (j // 4) * 300), os.path.basename(fn), fill='black')
    sheet.save(f'tmp/pdfs/ml6_review/contact-{batch//12+1}.jpg', quality=88)
