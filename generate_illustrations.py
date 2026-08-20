"""
Generate story-022 illustrations using Pillow.
Creates cartoon-vector-style images for the firefly story.
"""

import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

random.seed(42)

WIDTH = 768
HEIGHT = 1024

OUTPUT_DIR = r"c:\Users\hexiaohua\WorkBuddy\20260408094523\bedtimestories\assets\images"


def lerp_color(c1, c2, t):
    """Linearly interpolate between two RGB colors."""
    return tuple(int(a + (b - a) * t) for a, b in zip(c1, c2))


def draw_sky(draw, w, h, colors):
    """Draw a gradient sky."""
    for y in range(h):
        t = y / h
        color = lerp_color(colors[0], colors[1], t)
        draw.line([(0, y), (w, y)], fill=color)


def draw_stars(draw, w, h, count=40):
    """Draw small white/yellow stars."""
    for _ in range(count):
        x = random.randint(0, w)
        y = random.randint(0, int(h * 0.6))
        r = random.choice([1, 1, 2])
        alpha = random.randint(150, 255)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 200, alpha))


def draw_moon(draw, x, y, r, color=(255, 255, 220)):
    """Draw a crescent moon."""
    draw.ellipse([x - r, y - r, x + r, y + r], fill=color)
    draw.ellipse([x - r + 15, y - r - 10, x + r + 15, y + r - 10], fill=(20, 24, 50))


def draw_tree(draw, x, y, trunk_h=200, canopy_r=100, color="darkgreen"):
    """Draw a simple tree."""
    # Trunk
    draw.rectangle([x - 8, y - trunk_h, x + 8, y], fill=(80, 50, 30))
    # Canopy
    draw.ellipse([x - canopy_r, y - trunk_h - canopy_r, x + canopy_r, y - trunk_h], fill=color)
    # Highlight
    hx, hy = x - 20, y - trunk_h - canopy_r + 20
    draw.ellipse([hx - 30, hy - 30, hx + 30, hy + 30], fill=(70, 120, 50, 100))


def draw_firefly(draw, x, y, glow_size=40, body_color=(255, 220, 50), show_glow=True):
    """Draw a firefly with a glowing abdomen."""
    # Glow aura
    if show_glow:
        for i in range(5, 0, -1):
            r = glow_size * i // 5
            alpha = 30 + i * 10
            draw.ellipse([x - r, y - r + 10, x + r, y + r + 10], fill=(255, 255, 150, alpha))

    # Body (oval)
    draw.ellipse([x - 6, y - 4, x + 6, y + 8], fill=(40, 30, 25))
    # Glowing abdomen
    draw.ellipse([x - 5, y + 2, x + 5, y + 10], fill=body_color)

    # Wings
    draw.ellipse([x - 10, y - 6, x - 2, y + 2], fill=(200, 220, 255, 150))
    draw.ellipse([x + 2, y - 6, x + 10, y + 2], fill=(200, 220, 255, 150))

    # Head
    draw.ellipse([x - 3, y - 5, x + 3, y - 1], fill=(35, 30, 25))
    # Eyes
    draw.ellipse([x - 2, y - 4, x - 1, y - 3], fill=(255, 255, 255))
    draw.ellipse([x + 1, y - 4, x + 2, y - 3], fill=(255, 255, 255))

    return glow_size


def draw_grass(draw, x, y, height=30, color="green"):
    """Draw grass blades."""
    for i in range(-5, 6):
        px = x + i * 8
        py = y
        bh = height + random.randint(-5, 10)
        draw.line([(px, py), (px + random.randint(-3, 3), py - bh)], fill=color, width=2)


def draw_mouse(draw, x, y, color=(180, 160, 140)):
    """Draw a cute mouse."""
    # Body
    draw.ellipse([x - 12, y - 8, x + 12, y + 10], fill=color)
    # Head
    draw.ellipse([x - 8, y - 14, x + 8, y - 2], fill=color)
    # Ears
    draw.ellipse([x - 9, y - 20, x - 3, y - 12], fill=color)
    draw.ellipse([x + 3, y - 20, x + 9, y - 12], fill=color)
    draw.ellipse([x - 8, y - 19, x - 4, y - 13], fill=(255, 200, 200))
    draw.ellipse([x + 4, y - 19, x + 8, y - 13], fill=(255, 200, 200))
    # Eyes
    draw.ellipse([x - 4, y - 12, x - 2, y - 10], fill=(20, 20, 20))
    draw.ellipse([x + 2, y - 12, x + 4, y - 10], fill=(20, 20, 20))
    # Nose
    draw.ellipse([x - 1, y - 9, x + 1, y - 7], fill=(255, 150, 150))
    # Whiskers
    for dx in [-6, -8, -10]:
        draw.line([(x - 2, y - 8), (x + dx, y - 10 + random.randint(-2, 2))], fill=(100, 100, 100), width=1)
        draw.line([(x + 2, y - 8), (x - dx, y - 10 + random.randint(-2, 2))], fill=(100, 100, 100), width=1)
    # Tail
    draw.arc([x + 10, y - 5, x + 30, y + 20], 0, 180, fill=(200, 180, 160), width=2)


def draw_leaf(draw, x, y, size=40, angle=0, color=(50, 120, 50)):
    """Draw a leaf."""
    points = []
    for a in range(0, 360, 10):
        rad = math.radians(a + angle)
        r = size * abs(math.sin(math.radians(a)))
        px = x + r * math.cos(rad)
        py = y + r * math.sin(rad) * 0.5
        points.append((px, py))
    if len(points) > 2:
        draw.polygon(points, fill=color)


def draw_flower(draw, x, y, color=(255, 100, 150)):
    """Draw a small flower."""
    # Stem
    draw.line([(x, y), (x, y + 25)], fill=(50, 150, 50), width=2)
    # Petals
    for i in range(5):
        a = math.radians(i * 72)
        px = x + 7 * math.cos(a)
        py = y + 7 * math.sin(a)
        draw.ellipse([px - 4, py - 4, px + 4, py + 4], fill=color)
    # Center
    draw.ellipse([x - 3, y - 3, x + 3, y + 3], fill=(255, 255, 100))


def generate_cover():
    """Cover: Flora the firefly with her small warm glow in a moonlit meadow."""
    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Night sky gradient
    draw_sky(draw, WIDTH, HEIGHT, [(10, 5, 40), (25, 20, 60)])
    draw_stars(draw, WIDTH, HEIGHT, 50)
    draw_moon(draw, WIDTH - 120, 120, 50)

    # Ground / meadow
    draw.rectangle([(0, HEIGHT - 250), (WIDTH, HEIGHT)], fill=(20, 60, 25))
    # Grass
    for x in range(0, WIDTH, 12):
        draw_grass(draw, x, HEIGHT - 250, random.randint(25, 50), (30, 90, 35))

    # Large tree on the right
    draw_tree(draw, WIDTH - 150, HEIGHT - 250, trunk_h=300, canopy_r=130, color=(25, 70, 30))
    # Small tree on the left
    draw_tree(draw, 100, HEIGHT - 250, trunk_h=150, canopy_r=70, color=(30, 80, 35))

    # Flowers in the meadow
    for _ in range(8):
        fx = random.randint(50, WIDTH - 50)
        fy = HEIGHT - random.randint(30, 80)
        draw_flower(draw, fx, fy, (255, 200, 100))

    # Other fireflies in the background (small)
    for _ in range(6):
        fx = random.randint(50, WIDTH - 50)
        fy = random.randint(200, HEIGHT - 300)
        draw_firefly(draw, fx, fy, glow_size=15 + random.randint(5, 20), show_glow=True)

    # Main firefly Flora (center, slightly glowing)
    flora_x, flora_y = WIDTH // 2, HEIGHT // 2 - 50
    draw_firefly(draw, flora_x, flora_y, glow_size=35, body_color=(255, 240, 100), show_glow=True)

    # Large leaf that Flora sits on
    draw_leaf(draw, flora_x + 5, flora_y + 20, size=50, angle=0, color=(40, 130, 50))

    # Title text at bottom
    try:
        font_large = ImageFont.truetype("arial.ttf", 36)
        font_small = ImageFont.truetype("arial.ttf", 20)
    except Exception:
        font_large = ImageFont.load_default()
        font_small = font_large

    # Title background
    draw.rectangle([(0, HEIGHT - 130), (WIDTH, HEIGHT - 10)], fill=(0, 0, 0, 160))
    draw.text((WIDTH // 2, HEIGHT - 100), "The Little Firefly", fill=(255, 255, 200), font=font_large, anchor="mm")
    draw.text((WIDTH // 2, HEIGHT - 65), "Who Found Her Light", fill=(255, 255, 200), font=font_large, anchor="mm")
    draw.text((WIDTH // 2, HEIGHT - 30), "✨ A Bedtime Story ✨", fill=(200, 200, 255), font=font_small, anchor="mm")

    path = os.path.join(OUTPUT_DIR, "story-022-cover.png")
    img.save(path)
    print(f"Saved cover: {path}")


def generate_scene1():
    """Scene 1: Flora hides behind a leaf, sad while other fireflies glow brightly."""
    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Night sky
    draw_sky(draw, WIDTH, HEIGHT, [(15, 10, 45), (30, 25, 55)])
    draw_stars(draw, WIDTH, HEIGHT, 30)
    draw_moon(draw, WIDTH - 100, 100, 40)

    # Ground
    draw.rectangle([(0, HEIGHT - 200), (WIDTH, HEIGHT)], fill=(25, 55, 30))
    for x in range(0, WIDTH, 10):
        draw_grass(draw, x, HEIGHT - 200, random.randint(20, 40), (35, 80, 40))

    # Trees
    draw_tree(draw, 80, HEIGHT - 200, trunk_h=180, canopy_r=90, color=(25, 65, 30))
    draw_tree(draw, WIDTH - 100, HEIGHT - 200, trunk_h=220, canopy_r=100, color=(25, 65, 30))

    # Other fireflies playing (bright, in the open)
    for i in range(5):
        fx = 200 + i * 80
        fy = 250 + random.randint(-30, 30)
        draw_firefly(draw, fx, fy, glow_size=30, body_color=(255, 220, 50), show_glow=True)

    # A large bush/leaf cluster on the right side
    for bx in range(WIDTH - 250, WIDTH - 100, 30):
        for by in range(HEIGHT - 220, HEIGHT - 100, 30):
            draw_leaf(draw, bx, by, size=35, angle=random.randint(0, 360), color=(40, 100, 45))

    # Flora hiding behind a big leaf (bottom-right)
    flora_x, flora_y = WIDTH - 160, HEIGHT - 160
    draw_leaf(draw, flora_x, flora_y, size=50, angle=20, color=(50, 120, 55))
    draw_firefly(draw, flora_x - 5, flora_y - 15, glow_size=18, body_color=(255, 200, 80), show_glow=True)

    # Text caption
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        font = ImageFont.load_default()
    draw.rectangle([(0, HEIGHT - 50), (WIDTH, HEIGHT)], fill=(0, 0, 0, 160))
    draw.text((WIDTH // 2, HEIGHT - 28), "Flora hides her light — it's too small, she thinks...", fill=(220, 220, 255), font=font, anchor="mm")

    path = os.path.join(OUTPUT_DIR, "story-022-scene-1.png")
    img.save(path)
    print(f"Saved scene 1: {path}")


def generate_scene2():
    """Scene 2: Max the mouse lost in the dark forest, scared."""
    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Very dark forest sky
    draw_sky(draw, WIDTH, HEIGHT, [(5, 3, 20), (10, 8, 30)])

    # Few dim stars
    draw_stars(draw, WIDTH, HEIGHT, 15)
    # Moon behind clouds
    draw_moon(draw, WIDTH - 120, 100, 35, (200, 200, 220))
    # Cloud overlay on moon
    draw.ellipse([WIDTH - 170, 70, WIDTH - 30, 140], fill=(15, 12, 40, 200))

    # Ground
    draw.rectangle([(0, HEIGHT - 180), (WIDTH, HEIGHT)], fill=(10, 25, 15))

    # Dark looming trees
    draw_tree(draw, 60, HEIGHT - 180, trunk_h=280, canopy_r=110, color=(8, 30, 15))
    draw_tree(draw, WIDTH - 70, HEIGHT - 180, trunk_h=300, canopy_r=120, color=(8, 30, 15))
    draw_tree(draw, WIDTH // 2 - 100, HEIGHT - 180, trunk_h=200, canopy_r=80, color=(10, 35, 18))

    # Some tree trunks (bare)
    for tx in [150, 300, 500, 650]:
        draw.rectangle([tx - 5, HEIGHT - 350, tx + 5, HEIGHT - 180], fill=(25, 20, 15))

    # Scary eyes in the dark (tiny dots)
    for _ in range(4):
        ex = random.randint(100, WIDTH - 100)
        ey = random.randint(200, 400)
        draw.ellipse([ex - 2, ey - 2, ex + 2, ey + 2], fill=(255, 200, 50, 100))

    # Blown-out lantern on the ground
    lantern_x, lantern_y = 400, HEIGHT - 190
    draw.rectangle([lantern_x - 8, lantern_y - 15, lantern_x + 8, lantern_y], fill=(150, 100, 50))
    draw.rectangle([lantern_x - 12, lantern_y - 20, lantern_x + 12, lantern_y - 15], fill=(100, 70, 30))
    # Faint smoke from extinguished lantern
    for sy in range(5):
        draw.ellipse([lantern_x - 4 + random.randint(-2, 2), lantern_y - 25 - sy * 8,
                       lantern_x + 4 + random.randint(-2, 2), lantern_y - 17 - sy * 8],
                      fill=(60, 60, 60, 80 - sy * 10))

    # Max the mouse, sitting on a rock, scared
    mouse_x, mouse_y = 350, HEIGHT - 200
    # Rock
    draw.ellipse([mouse_x - 25, mouse_y + 5, mouse_x + 25, mouse_y + 25], fill=(40, 40, 45))
    draw_mouse(draw, mouse_x, mouse_y, color=(160, 140, 120))

    # Tear on Max's face
    draw.ellipse([mouse_x + 1, mouse_y - 9, mouse_x + 3, mouse_y - 7], fill=(150, 180, 255, 150))

    # Text
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        font = ImageFont.load_default()
    draw.rectangle([(0, HEIGHT - 50), (WIDTH, HEIGHT)], fill=(0, 0, 0, 180))
    draw.text((WIDTH // 2, HEIGHT - 28), "Max is lost in the Deep Dark Woods... \"Is anyone there?\"", fill=(200, 200, 255), font=font, anchor="mm")

    path = os.path.join(OUTPUT_DIR, "story-022-scene-2.png")
    img.save(path)
    print(f"Saved scene 2: {path}")


def generate_scene3():
    """Scene 3: Flora shines her light to guide Max home."""
    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Warm-toned night sky (hope)
    draw_sky(draw, WIDTH, HEIGHT, [(20, 15, 50), (40, 30, 60)])
    draw_stars(draw, WIDTH, HEIGHT, 25)
    draw_moon(draw, 100, 120, 45)

    # Ground / path home
    draw.rectangle([(0, HEIGHT - 200), (WIDTH, HEIGHT)], fill=(20, 50, 28))

    # Trees along the path
    draw_tree(draw, 60, HEIGHT - 200, trunk_h=200, canopy_r=90, color=(25, 65, 30))
    draw_tree(draw, WIDTH - 80, HEIGHT - 200, trunk_h=250, canopy_r=110, color=(25, 65, 30))

    # A winding path of light on the ground
    for px in range(200, WIDTH - 50, 15):
        py = HEIGHT - 140 + int(20 * math.sin(px * 0.05))
        glow_r = 8 + int(5 * math.sin(px * 0.1))
        draw.ellipse([px - glow_r, py - glow_r, px + glow_r, py + glow_r], fill=(255, 240, 150, 80 + int(30 * math.sin(px * 0.1))))

    # Flora glowing brightly, leading the way
    flora_x, flora_y = 300, HEIGHT - 300
    draw_firefly(draw, flora_x, flora_y, glow_size=50, body_color=(255, 255, 100), show_glow=True)

    # Light beam from Flora
    for i in range(3):
        beam_alpha = 30 - i * 8
        draw.ellipse([flora_x - 80 - i * 20, flora_y - 80 - i * 20,
                       flora_x + 80 + i * 20, flora_y + 80 + i * 20],
                      fill=(255, 255, 150, beam_alpha))

    # Max following behind Flora
    mouse_x, mouse_y = flora_x + 60, HEIGHT - 210
    draw_mouse(draw, mouse_x, mouse_y, color=(170, 150, 130))

    # Max looking up with relief/smile
    draw.arc([mouse_x - 5, mouse_y - 8, mouse_x + 5, mouse_y], 0, 180, fill=(200, 100, 100), width=1)

    # Flowers along the path
    for _ in range(6):
        fx = random.randint(150, WIDTH - 80)
        fy = HEIGHT - random.randint(40, 100)
        draw_flower(draw, fx, fy, (255, 180, 200))

    # Meadow visible in the distance (warm glow on horizon)
    draw.rectangle([(WIDTH - 100, HEIGHT - 220), (WIDTH, HEIGHT - 200)], fill=(60, 80, 50, 100))

    # Fireflies welcoming in the distance
    for _ in range(4):
        fx = WIDTH - random.randint(30, 90)
        fy = HEIGHT - random.randint(120, 250)
        draw_firefly(draw, fx, fy, glow_size=12, show_glow=True)

    # Text
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except Exception:
        font = ImageFont.load_default()
    draw.rectangle([(0, HEIGHT - 50), (WIDTH, HEIGHT)], fill=(0, 0, 0, 160))
    draw.text((WIDTH // 2, HEIGHT - 28), "Flora's small light guides Max home — it was enough all along.", fill=(220, 220, 255), font=font, anchor="mm")

    path = os.path.join(OUTPUT_DIR, "story-022-scene-3.png")
    img.save(path)
    print(f"Saved scene 3: {path}")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Generating story-022 illustrations...")
    generate_cover()
    generate_scene1()
    generate_scene2()
    generate_scene3()
    print("All illustrations generated!")
