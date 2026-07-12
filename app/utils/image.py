from PIL import Image


def load_image(path):

    return Image.open(path)


def resize_image(path, size=(512, 512)):

    image = Image.open(path)

    image = image.resize(size)

    return image