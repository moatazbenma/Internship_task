
from .models import CaseData, Order, QueryLog
from django.utils import timezone

def save_scraped_data(data):
    if not data:
        return None

    query_log = QueryLog.objects.create(
        cnr_number=data.get("cnr", "Unknown"),
        searched_at=timezone.now(),
    )

    case, created = CaseData.objects.get_or_create(
        cnr=data["cnr"],
        defaults={
            "case_number": data["case_number"],
            "petitioner": data["petitioner"],
            "respondent": data["respondent"],
            "filing_date": data["filing_date"],
            "registration_date": data["registration_date"],
            "hearing_date": data["hearing_date"],
            "court_name": data["court_name"],
            "status": data["status"],
        },
    )

    for order_data in data.get("orders", []):
        Order.objects.get_or_create(
            case=case,
            date=order_data["date"],
            summary=order_data["summary"],
            pdf_url=order_data["pdf_url"]
        )

    return case
