import requests
from bs4 import BeautifulSoup


def get_bill(ref_no):

    print("🔥 SCRAPER FUNCTION STARTED")
    print("REF:", repr(ref_no))

    session = requests.Session()

    url = "https://bill.pitc.com.pk/fescobill"

    response = session.get(url, timeout = 10)

    soup = BeautifulSoup(response.text, "html.parser")

    form = soup.find("form")

    if not form:
        print("FORM NOT FOUND")
        return None

    data = {}

    for input_tag in form.find_all("input"):
        name = input_tag.get("name")
        value = input_tag.get("value", "")

        if name:
            data[name] = value


    # important fields
    data["searchTextBox"] = ref_no
    data["rbSearchByList"] = "refno"
    data["btnSearch"] = "Search"

    print(data)
    response = session.post(
    url,
    data=data,
    timeout=10
    )

    print("STATUS:", response.status_code)
    print("LOCATION:", response.headers.get("Location"))
    print("FINAL URL:", response.url)
    print("HTML SIZE:", len(response.text))
    return response.text
