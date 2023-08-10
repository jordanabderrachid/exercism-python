import math

colors_to_value = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

tolerance = {
    "grey": "0.05",
    "violet": "0.1",
    "blue": "0.25",
    "green": "0.5",
    "brown": "1",
    "red": "2",
    "gold": "5",
    "silver": "10",
}


def resistor_label(colors):
    if len(colors) == 1:
        return resistor_labels_one_band(colors[0])

    if len(colors) == 4:
        return resistor_labels_four_bans(colors)

    if len(colors) == 5:
        return resistor_labels_five_bans(colors)

    return ""


def resistor_labels_one_band(color):
    value = colors_to_value.index(color)
    return f"{value} ohms"


def resistor_labels_four_bans(colors):
    power = 10 ** colors_to_value.index(colors[2])
    value = (
        colors_to_value.index(colors[0]) * 10 + colors_to_value.index(colors[1])
    ) * power

    return f"{format_value(value)} ±{tolerance.get(colors[3])}%"


def resistor_labels_five_bans(colors):
    power = 10 ** colors_to_value.index(colors[3])
    value = (
        colors_to_value.index(colors[0]) * 100
        + colors_to_value.index(colors[1]) * 10
        + colors_to_value.index(colors[2])
    ) * power

    return f"{format_value(value)} ±{tolerance.get(colors[4])}%"


def format_value(value) -> str:
    if value > 1000000:
        value /= 1000000
        if math.floor(value) == value:
            value = int(value)
        return f"{value} megaohms"

    if value > 1000:
        value /= 1000
        if math.floor(value) == value:
            value = int(value)
        return f"{value} kiloohms"

    return f"{value} ohms"
