import settings


def height_prct(percentage: float) -> float:
    """
    Calculates percentage of settings.height
    :param percentage: percentage to calculate (between 0 and 100)
    :return: the part of the height according to the percentage
    """
    return (settings.HEIGHT / 100) * percentage


def width_prct(percentage: float) -> float:
    """
    Calculates percentage of settings.width
    :param percentage: percentage to calculate (between 0 and 100)
    :return: the part of the width according to the percentage
    """
    return (settings.WIDTH / 100) * percentage
