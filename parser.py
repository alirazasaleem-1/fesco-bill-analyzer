from bs4 import BeautifulSoup


def parse_bill(html):

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(" ", strip=True)

    current_bill = extract_amount(
    soup,
    "Current Bill"
    )

    grand_total = extract_amount(
        soup,
        "Grand Total"
    )

    return {
    "reference_no": extract_between(
        text,
        "REFERENCE NO",
        "CONSUMER ID"
    ),

    "consumer_name": extract_between(
        text,
        "NAME & ADDRESS",
        "TRANSFORMER"
    ),

    "units": extract_between(
        text,
        "UNITS",
        "BILL CHARGES"
    ),

    "billing_month": extract_between(
        text,
        "BILL MONTH",
        "READING DATE"
    ),

    "due_date": extract_between(
        text,
        "DUE DATE",
        "PAYABLE"
    ),

    "current_bill": current_bill,

    "grand_total": grand_total
    }

def clean_value(value):

    urdu_words = [
        "حوالہ نمبر",
        "کنزیومر نمبر",
        "نام و پتہ",
        "یونٹ",
        "مہینہ بل",
        "مقررہ تاریخ"
    ]

    for word in urdu_words:
        value = value.replace(word, "")

    return " ".join(value.split()).strip()

def extract_between(text, start, end):

    try:
        result = text.split(start)[1]
        result = result.split(end)[0]

        return clean_value(result)

    except:
        return "Not Found"

def extract_amount(soup, label):
    element = soup.find(
        string=lambda text: text and label in text
    )

    if element:
        value = element.find_next(
            class_="charges-bd-val"
        )

        if value:
            return value.get_text(strip=True)

    return None