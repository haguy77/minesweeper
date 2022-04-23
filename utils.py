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


def cell_height() -> int:
    """
    Calculates height of the cell according to settings.HEIGHT
    :return: height of the cell
    """
    return settings.HEIGHT // 180


def cell_width() -> int:
    """
    Calculates width of the cell according to settings.WIDTH
    :return: width of the cell
    """
    return settings.WIDTH // 90


def cell_count_label_height() -> int:
    """
    Calculates height of the cell count label  according to settings.HEIGHT
    :return: height of the cell
    """
    return settings.HEIGHT // 135


def cell_count_label_width() -> int:
    """
    Calculates width of the cell count label according to settings.WIDTH
    :return: width of the cell
    """
    return settings.WIDTH // 90


def cell_count_label_font_size() -> int:
    """
    Calculates font size for the cell count label according to
    (settings.WIDTH * settings.HEIGHT) // 23328
    :return: cell count label font size
    """
    return (settings.WIDTH * settings.HEIGHT) // 23328
