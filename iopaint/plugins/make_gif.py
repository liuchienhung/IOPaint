from pathlib import Path
from typing import Iterable

from PIL import Image
import imageio


def make_gif(original: Path, cleaned: Path, gif_path: Path, duration: float = 0.5) -> None:
    """Create a GIF comparing original and cleaned images.

    Parameters
    ----------
    original : Path
        Path to the original image.
    cleaned : Path
        Path to the cleaned image.
    gif_path : Path
        Output path for the GIF file.
    duration : float, optional
        Duration of each frame in seconds, by default 0.5
    """
    orig_img = Image.open(original).convert("RGBA")
    cleaned_img = Image.open(cleaned).convert("RGBA")

    max_w = max(orig_img.width, cleaned_img.width)
    max_h = max(orig_img.height, cleaned_img.height)

    def pad(img: Image.Image) -> Image.Image:
        if img.width == max_w and img.height == max_h:
            return img
        canvas = Image.new("RGBA", (max_w, max_h))
        canvas.paste(img, (0, 0))
        return canvas

    frames: Iterable[Image.Image] = [pad(orig_img), pad(cleaned_img)]
    imageio.mimsave(gif_path, frames, format="GIF", duration=duration)
