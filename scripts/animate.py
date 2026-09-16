"""Encode the generated painting as a quiet, seamless camera-motion GIF.

Usage: python3 scripts/animate.py
Requires Pillow. The source illustration was created with Image Generation;
this script only renders the camera movement and encodes the animation.
"""

from math import cos, pi
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/ambassadors-still.png"
OUTPUT = ROOT / "assets/ambassadors.gif"
SIZE = (660, 440)
FRAME_COUNT = 64
DURATION_MS = 125


def main():
    source = Image.open(SOURCE).convert("RGB")
    width, height = source.size
    palette = source.resize(SIZE, Image.Resampling.LANCZOS).quantize(colors=128)
    frames = []
    for index in range(FRAME_COUNT):
        # A cosine cycle comes to rest at both ends, including the loop seam.
        progress = (1 - cos(2 * pi * index / FRAME_COUNT)) / 2
        scale = 1 + 0.025 * progress
        view_width, view_height = width / scale, height / scale
        left = (width - view_width) / 2
        top = (height - view_height) / 2
        frame = source.resize(
            SIZE,
            Image.Resampling.LANCZOS,
            box=(left, top, left + view_width, top + view_height),
        )
        # One shared palette prevents colours from flickering between frames.
        frames.append(frame.quantize(palette=palette, dither=Image.Dither.NONE))
    frames[0].save(
        OUTPUT,
        save_all=True,
        append_images=frames[1:],
        # GIF timing is in centiseconds: alternate 120/130 ms for 8 seconds.
        duration=[120 if i % 2 == 0 else 130 for i in range(FRAME_COUNT)],
        loop=0,
        optimize=True,
        disposal=1,
    )
    with Image.open(OUTPUT) as gif:
        duration = 0
        for index in range(gif.n_frames):
            gif.seek(index)
            gif.load()
            duration += gif.info.get("duration", 0)
        assert gif.size == SIZE
        assert gif.info.get("loop") == 0
        assert duration == FRAME_COUNT * DURATION_MS
        print(f"{OUTPUT}: {gif.size}, {gif.n_frames} frames, {duration} ms, "
              f"{OUTPUT.stat().st_size / 1024 / 1024:.2f} MiB")


if __name__ == "__main__":
    main()
