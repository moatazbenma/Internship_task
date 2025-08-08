import requests
from bs4 import BeautifulSoup

BASE_URL = "https://districts.ecourtsindia.com/CNR/"

def scrape_case_details(cnr_number):
    url = f"{BASE_URL}{cnr_number}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data for {cnr_number}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        card_body = soup.select_one('.info-card .card-body')
        columns = card_body.select('.col-md-6')

        left = columns[0].find_all('p')
        right = columns[1].find_all('p')

        cnr = left[0].text.split(":")[-1].strip()
        case_number = left[1].text.split(":")[-1].strip()
        parties = left[2].text.split(":")[-1].strip()
        filing_date = left[3].text.split(":")[-1].strip()
        registration_date = left[4].text.split(":")[-1].strip()
        
        court_name = right[0].text.split(":")[-1].strip()
        hearing_date = right[1].text.split(":")[-1].strip()
        status = right[2].text.split(":")[-1].strip()

        petitioner, respondent = parties.split("versus")

        # Orders
        orders = []
        timeline_items = soup.select('.timeline-item')

        for item in timeline_items:
            if 'marker-order' in item.select_one('.timeline-marker')['class']:
                order_date = item.select_one('.event-date').text.strip()
                summary = item.select_one('h6').text.strip()
                pdf_link_tag = item.select_one('a.btn-view-order')
                pdf_url = "https://districts.ecourtsindia.com" + pdf_link_tag['href']

                orders.append({
                    "date": order_date,
                    "summary": summary,
                    "pdf_url": pdf_url
                })

        return {
            "cnr": cnr,
            "case_number": case_number,
            "petitioner": petitioner.strip(),
            "respondent": respondent.strip(),
            "filing_date": filing_date,
            "registration_date": registration_date,
            "hearing_date": hearing_date,
            "court_name": court_name,
            "status": status,
            "orders": orders,
            "raw_html": response.text,
        }

    except Exception as e:
        print(f"Error during parsing: {e}")
        return None
