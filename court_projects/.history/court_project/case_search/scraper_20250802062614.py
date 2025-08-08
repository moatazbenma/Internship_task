import requests
from bs4 import BeautifulSoup


def scrape_case_details(case_type, case_number, year):
    url = "https://services.ecourts.gov.in/ecourtindia_v6/"

    search_url = url + "casestatus/case_number.php"

    payload = {
        'state_cd': 'HR',            # Example: Haryana (Faridabad)
        'dist_cd': '4',              # District code (adjust as needed)
        'court_code': '',            # If required
        'case_type': case_type,
        'case_no': case_number,
        'case_year': year,
        'submit': 'Submit',
    }

    try:
        response = requests.post(search_url, data=payload)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        # TEMP: Save for manual inspection
        with open("debug_response.html", "wb") as f:
            f.write(response.content)

        # Placeholder parsing
        case_data = {
            'petitioner': 'TO_BE_PARSED',
            'respondent': 'TO_BE_PARSED',
            'court_name': 'TO_BE_PARSED',
            'filing_date': None,
            'hearing_date': None,
            'status': 'TO_BE_PARSED',
            'order_link': None,
            'raw_html': response.text
        }

        return True, case_data

    except Exception as e:
        print(f"[Scraper Error] {e}")
        return False, {'error': str(e)}
