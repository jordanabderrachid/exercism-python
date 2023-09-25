# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry:
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, "%Y-%m-%d")
    entry.description = description
    entry.change = change
    return entry


def header(locale):
    match locale:
        case "en_US":
            return "Date       | Description               | Change       "
        case "nl_NL":
            return "Datum      | Omschrijving              | Verandering  "
        case _:
            raise ValueError("unsupported locale")


def format_date(locale: str, d: datetime) -> str:
    match locale:
        case "en_US":
            return d.strftime("%m/%d/%Y")
        case "nl_NL":
            return d.strftime("%d-%m-%Y")
        case _:
            raise ValueError("unsupported locale")


def format_description(description: str):
    if len(description) > 25:
        return description[:22] + "..."

    return description.ljust(25, " ")


def format_currency(currency: str, locale: str, amount: int) -> str:
    match currency:
        case "USD":
            currency_symbol = "$"
        case "EUR":
            currency_symbol = "€"
        case _:
            raise ValueError("unsupported currency")

    match locale:
        case "en_US":
            decimal_sep = "."
            major_sep = ","
        case "nl_NL":
            decimal_sep = ","
            major_sep = "."
        case _:
            raise ValueError("unsupported locale")

    major = str(abs(int(amount / 100)))
    minor = str(abs(amount) % 100).rjust(2, "0")
    formatted_major = ""  # group digits by 3 and separate with a ","
    for i in range(len(major) - 1, -1, -1):
        if (len(major) - 1 - i) == 0 or (len(major) - 1 - i) % 3 != 0:
            formatted_major = major[i] + formatted_major
        else:
            formatted_major = major[i] + major_sep + formatted_major

    match locale:
        case "en_US":
            res = f"{currency_symbol}{formatted_major}{decimal_sep}{minor}"
            if amount < 0:
                return f"({res})"
            else:
                return res + " "
        case "nl_NL":
            if amount < 0:
                return f"{currency_symbol} -{formatted_major}{decimal_sep}{minor} "
            else:
                return f"{currency_symbol} {formatted_major}{decimal_sep}{minor} "
        case _:
            raise ValueError("unsupported locale")


def format_entries(currency, locale, entries):
    table = [header(locale)]
    for entry in sorted(entries, key=lambda e: (e.date, e.change, e.description)):
        date_str = format_date(locale, entry.date)
        description_str = format_description(entry.description)
        currency_str = format_currency(currency, locale, entry.change).rjust(13)
        table.append(f"{date_str} | {description_str} | {currency_str}")

    return "\n".join(table)
