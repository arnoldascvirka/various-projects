from PIL import Image
import time
import logging
import argparse
import typing
import random
from random import randint, random as random_range
from PIL import ImageFilter, Image
from PIL import Image
from PIL import PyAccess
DEFAULTS = {
    "interval_function": "threshold",
    "lower_threshold": 0.25,
    "upper_threshold": 0.8,
    "char_length": 50,
    "angle": 0,
    "randomness": 0,
    "sorting_function": "sorted",
}

def parse_args():
    parser = argparse.ArgumentParser(description="Pixel mangle an image.")
    parser.add_argument("image", help="Input image file path.")
    parser.add_argument(
        "-o",
        "--output",
        help="Output image file path, DEFAULTS to the time created.")
    parser.add_argument("-i", "--int_function",
                        choices=choices.keys(),
                        default=DEFAULTS["interval_function"],
                        help="Function to determine sorting intervals")
    parser.add_argument("-f", "--int_file",
                        help="Image used for defining intervals.")
    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        default=DEFAULTS["lower_threshold"],
        help="Pixels darker than this are not sorted, between 0 and 1")
    parser.add_argument(
        "-u",
        "--upper_threshold",
        type=float,
        default=DEFAULTS["upper_threshold"],
        help="Pixels brighter than this are not sorted, between 0 and 1")
    parser.add_argument(
        "-c",
        "--char_length",
        type=int,
        default=DEFAULTS["char_length"],
        help="Characteristic length of random intervals")
    parser.add_argument(
        "-a",
        "--angle",
        type=float,
        default=DEFAULTS["angle"],
        help="Rotate the image by an angle (in degrees) before sorting")
    parser.add_argument(
        "-r",
        "--randomness",
        type=float,
        default=DEFAULTS["randomness"],
        help="What percentage of intervals are NOT sorted")
    parser.add_argument("-s", "--sorting_function",
                        choices=choices.keys(),
                        default=DEFAULTS["sorting_function"],
                        help="Function to sort pixels by.")
    parser.add_argument(
        "-m", "--mask", help="Image used for masking parts of the image")
    parser.add_argument(
        "-l",
        "--log_level",
        default="WARNING",
        help="Print more or less info",
        choices=[
            "DEBUG",
            "INFO",
            "WARNING",
            "ERROR",
            "CRITICAL"])

    _args = parser.parse_args()

    logging.basicConfig(
        format="%(name)s: %(levelname)s - %(message)s",
        level=logging.getLevelName(
            _args.log_level))

    return {
        "image_input_path": _args.image,
        "image_output_path": _args.output,
        "interval_function": _args.int_function,
        "interval_file_path": _args.int_file,
        "lower_threshold": _args.threshold,
        "upper_threshold": _args.upper_threshold,
        "char_length": _args.char_length,
        "angle": _args.angle,
        "randomness": _args.randomness,
        "sorting_function": _args.sorting_function,
        "mask_path": _args.mask
    }

def id_generator() -> str:
    timestr = time.strftime("%Y%m%d-%H%M%S")
    return timestr


def crop_to(image_to_crop: Image.Image, reference_image: Image.Image) -> Image.Image:
    """
    Crops image to the size of a reference image. This function assumes that the relevant image is located in the center
    and you want to crop away equal sizes on both the left and right as well on both the top and bottom.
    :param image_to_crop
    :param reference_image
    :return: image cropped to the size of the reference image
    """
    reference_size = reference_image.size
    current_size = image_to_crop.size
    dx = current_size[0] - reference_size[0]
    dy = current_size[1] - reference_size[1]
    left = dx / 2
    upper = dy / 2
    right = dx / 2 + reference_size[0]
    lower = dy / 2 + reference_size[1]
    return image_to_crop.crop(
        box=(
            int(left),
            int(upper),
            int(right),
            int(lower)))
def sort_image(
        size: typing.Tuple[int, int],
        image_data: PyAccess.PyAccess,
        mask_data: PyAccess.PyAccess,
        intervals: typing.List[typing.List[int]],
        randomness: float,
        sorting_function: typing.Callable[[typing.List[typing.Tuple[int, int, int]]], float]):
    sorted_pixels = []

    for y in range(size[1]):
        row = []
        x_min = 0
        for x_max in intervals[y] + [size[0]]:
            interval = []
            for x in range(x_min, x_max):
                if mask_data[x, y]:
                    interval.append(image_data[x, y])
            if random.random() * 100 < randomness:
                row += interval
            else:
                row += sort_interval(interval, sorting_function)
            x_min = x_max
        sorted_pixels.append(row)
    return sorted_pixels


def sort_interval(interval: typing.List,
                  sorting_function: typing.Callable[[typing.List[typing.Tuple[int, int, int]]], float]):
    return [] if interval == [] else sorted(interval, key=sorting_function)

def pixelsort(
        image: Image.Image,
        mask_image: typing.Optional[Image.Image] = None,
        interval_image: typing.Optional[Image.Image] = None,
        randomness: float = DEFAULTS["randomness"],
        char_length: float = DEFAULTS["char_length"],
        sorting_function: typing.Literal["lightness", "hue", "saturation", "intensity", "minimum"] = DEFAULTS[
            "sorting_function"],
        interval_function: typing.Literal["random", "threshold", "edges", "waves", "file", "file-edges", "none"] =
        DEFAULTS["interval_function"],
        lower_threshold: float = DEFAULTS["lower_threshold"],
        upper_threshold: float = DEFAULTS["upper_threshold"],
        angle: float = DEFAULTS["angle"]
        
) -> Image.Image:
    """
    pixelsorts an image
    :param image: image to pixelsort
    :param mask_image: Image used for masking parts of the image.
    :param interval_image: Image used to define intervals. Must be black and white.
    :param randomness: What percentage of intervals *not* to sort. 0 by default.
    :param char_length:	Characteristic length for the random width generator. Used in mode `random` and `waves`.
    :param sorting_function: Sorting function to use for sorting the pixels.
    :param interval_function: Controls how the intervals used for sorting are defined.
    :param lower_threshold: How dark must a pixel be to be considered as a 'border' for sorting? Takes values from 0-1.
        Used in edges and threshold modes.
    :param upper_threshold: How bright must a pixel be to be considered as a 'border' for sorting? Takes values from
        0-1. Used in threshold mode.
    :param angle: Angle at which you're pixel sorting in degrees.
    :return: pixelsorted image
    """
    original = image
    image = image.convert('RGBA').rotate(angle, expand=True)
    image_data = image.load()

    mask_image = mask_image if mask_image else Image.new(
        "1", original.size, color=255)
    mask_image = mask_image.convert('1').rotate(angle, expand=True, fillcolor=0)
    mask_data = mask_image.load()

    interval_image = (interval_image
                      .convert('1')
                      .rotate(angle, expand=True)) if interval_image else None
    logging.debug("Determining intervals...")
    intervals = choices[interval_function](
        image,
        lower_threshold=lower_threshold,
        upper_threshold=upper_threshold,
        char_length=char_length,
        interval_image=interval_image,
    )
    logging.debug("Sorting pixels...")
    sorted_pixels = sort_image(
        image.size,
        image_data,
        mask_data,
        intervals,
        randomness,
        choices[sorting_function])

    output_img = _place_pixels(
        sorted_pixels,
        mask_data,
        image_data,
        image.size)
    if angle != 0:
        output_img = output_img.rotate(-angle, expand=True)
        output_img = crop_to(output_img, original)

    return output_img


def _place_pixels(pixels: PyAccess.PyAccess, mask: PyAccess.PyAccess, original: PyAccess.PyAccess,
                  size: typing.Tuple[int, int]):
    output_img = Image.new('RGBA', size)
    outputdata = output_img.load()  # modifying pixelaccess modified original
    for y in range(size[1]):
        count = 0
        for x in range(size[0]):
            if not mask[x, y]:
                outputdata[x, y] = original[x, y]
            else:
                outputdata[x, y] = pixels[y][count]
                count += 1
    return output_img



def edge(image: Image.Image, lower_threshold: float, **_) -> typing.List[typing.List[int]]:
    """Performs an edge detection, which is used to define intervals. Tweak threshold with threshold."""
    edge_data = image.filter(ImageFilter.FIND_EDGES).convert('RGBA').load()
    intervals = []

    for y in range(image.size[1]):
        intervals.append([])
        flag = True
        for x in range(image.size[0]):
            if lightness(edge_data[x, y]) < lower_threshold * 255:
                flag = True
            elif flag:
                intervals[y].append(x)
                flag = False
    return intervals


def threshold(image: Image.Image, lower_threshold: float, upper_threshold: float, **_) -> typing.List[typing.List[int]]:
    """Intervals defined by lightness thresholds; only pixels with a lightness between the upper and lower thresholds
     are sorted."""
    intervals = []
    image_data = image.load()
    for y in range(image.size[1]):
        intervals.append([])
        for x in range(image.size[0]):
            level = lightness(image_data[x, y])
            if level < lower_threshold * 255 or level > upper_threshold * 255:
                intervals[y].append(x)
    return intervals


def random(image, char_length, **_) -> typing.List[typing.List[int]]:
    """Randomly generate intervals. Distribution of widths is linear by default. Interval widths can be scaled using
    char_length."""
    intervals = []

    for y in range(image.size[1]):
        intervals.append([])
        x = 0
        while True:
            x += int(char_length * random_range())
            if x > image.size[0]:
                break
            else:
                intervals[y].append(x)
    return intervals


def waves(image, char_length, **_) -> typing.List[typing.List[int]]:
    """Intervals are waves of nearly uniform widths. Control width of waves with char_length."""
    intervals = []

    for y in range(image.size[1]):
        intervals.append([])
        x = 0
        while True:
            x += char_length + randint(0, 10)
            if x > image.size[0]:
                break
            else:
                intervals[y].append(x)
    return intervals


def file_mask(image, interval_image, **_) -> typing.List[typing.List[int]]:
    """Intervals taken from another specified input image. Must be black and white, and the same size as the input
    image."""
    intervals = []
    data = interval_image.load()

    for y in range(image.size[1]):
        intervals.append([])
        flag = True
        for x in range(image.size[0]):
            if data[x, y]:
                flag = True
            elif flag:
                intervals[y].append(x)
                flag = False
    return intervals


def file_edges(image, interval_image, lower_threshold, **_) -> typing.List[typing.List[int]]:
    """Intervals defined by performing edge detection on the file specified by -f. Must be the same size as the input
    image."""
    edge_data = interval_image.filter(
        ImageFilter.FIND_EDGES).convert('RGBA').load()
    intervals = []

    for y in range(image.size[1]):
        intervals.append([])
        flag = True
        for x in range(image.size[0]):
            if lightness(edge_data[x, y]) < lower_threshold * 255:
                flag = True
            elif flag:
                intervals[y].append(x)
                flag = False
    return intervals


def none(image, **_) -> typing.List[typing.List[int]]:
    """Sort whole rows, only stopping at image borders."""
    intervals = []
    for y in range(image.size[1]):
        intervals.append([])
    return intervals


choices = {
    "random": random,
    "threshold": threshold,
    "edges": edge,
    "waves": waves,
    "file": file_mask,
    "file-edges": file_edges,
    "none": none
}
args = parse_args()
image_input_path = args.pop("image_input_path")
image_output_path = args.pop("image_output_path")
interval_file_path = args.pop("interval_file_path")
mask_path = args.pop("mask_path")

if image_output_path is None:
    image_output_path = id_generator() + ".png"
    logging.warning("No output path provided, using " + image_output_path)

logging.debug("Opening image...")
args["image"] = Image.open(image_input_path)
if mask_path:
    logging.debug("Opening mask...")
    args["mask_image"] = Image.open(mask_path)
if interval_file_path:
    logging.debug("Opening interval file...")
    args["interval_image"] = Image.open(interval_file_path)

logging.debug("Saving image...")
pixelsort(**args).save(image_output_path)