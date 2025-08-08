import requests
from bs4 import BeautifulSoup

BASE_URL = "https://districts.ecourtsindia.com/CNR/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

def scrape_case_details(cnr_number):
    url = f"{BASE_URL}{cnr_number}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"[ERROR] Failed to fetch data for {cnr_number} - HTTP {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        card_body = soup.select_one('.info-card .card-body')
        if not card_body:
            print("[WARNING] Card body not found — invalid CNR?")
            return None

        columns = card_body.select('.col-md-6')
        if len(columns) < 2:
            print("[WARNING] Expected 2 columns of data, got less.")
            return None

        # Left column
        left = [p.get_text(strip=True) for p in columns[0].find_all('p')]
        right = [p.get_text(strip=True) for p in columns[1].find_all('p')]

        # Extracting safely
        cnr = left[0].split(":")[-1].strip() if len(left) > 0 else ""
        case_number = left[1].split(":")[-1].strip() if len(left) > 1 else ""
        parties_raw = left[2].split(":")[-1].strip() if len(left) > 2 else ""
        filing_date = left[3].split(":")[-1].strip() if len(left) > 3 else ""
        registration_date = left[4].split(":")[-1].strip() if len(left) > 4 else ""

        court_name = right[0].split(":")[-1].strip() if len(right) > 0 else ""
        hearing_date = right[1].split(":")[-1].strip() if len(right) > 1 else ""
        status = right[2].split(":")[-1].strip() if len(right) > 2 else ""

        # Robust split
        if "versus" in parties_raw.lower():
            parts = parties_raw.lower().split("versus")
        elif "vs" in parties_raw.lower():
            parts = parties_raw.lower().split("vs")
        else:
            parts = [parties_raw, ""]

        petitioner = parts[0].strip().title()
        respondent = parts[1].strip().title() if len(parts) > 1 else ""

        # Orders
        orders = []
        for item in soup.select('.timeline-item'):
            marker = item.select_one('.timeline-marker')
            if not marker or 'marker-order' not in marker.get("class", []):
                continue

            order_date = item.select_one('.event-date')
            summary = item.select_one('h6')
            pdf_link_tag = item.select_one('a.btn-view-order')

            orders.append({
                "date": order_date.get_text(strip=True) if order_date else "",
                "summary": summary.get_text(strip=True) if summary else "",
                "pdf_url": (
                    "https://districts.ecourtsindia.com" + pdf_link_tag['href']
                    if pdf_link_tag and 'href' in pdf_link_tag.attrs else ""
                )
            })

        return {
            "cnr": cnr,
            "case_number": case_number,
            "petitioner": petitioner,
            "respondent": respondent,
            "filing_date": filing_date,
            "registration_date": registration_date,
            "hearing_date": hearing_date,
            "court_name": court_name,
            "status": status,
            "orders": orders,
            "raw_html": response.text,
        }

    except Exception as e:
        print(f"[EXCEPTION] Error during parsing: {e}")
        return None
