import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'deps'))
import fitz

src, out = sys.argv[1:]
doc = fitz.open(src)
parts = []
for i, page in enumerate(doc):
    parts.append(f"\n===== SLIDE {i+1} =====\n{page.get_text('text')}")
    pix = page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False)
    pix.save(os.path.join(out, f"slide-{i+1:03}.png"))
open(os.path.join(out, 'slides.txt'), 'w', encoding='utf-8').write(''.join(parts))
print(f"pages={len(doc)}")
