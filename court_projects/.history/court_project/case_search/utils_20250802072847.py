from .models import QueryLog, CaseData, Order
from django.utils import timezone

def save_scraped_data(data):
    # Create a query log
    query_log = QueryLog.objects.create(
        cnr_number=data.get("cnr", "Unknown"),
        searched_at=timezone.now()
    )

    # Create the main case data
    case = CaseData.objects.create(
        cnr=data.get("cnr", ""),
        case_number=data.get("case_number", ""),
        petitioner=data.get("petitioner", ""),
        respondent=data.get("respondent", ""),
        filing_date=data.get("filing_date", ""),
        registration_date=data.get("registration_date", ""),
        hearing_date=data.get("hearing_date", ""),
        court_name=data.get("court_name", ""),
        status=data.get("status", "")
    )

    # Create related order entries (if any)
    for order in data.get("orders", []):
        Order.objects.create(
            case=case,
            date=order.get("date", ""),
            summary=order.get("summary", ""),
            pdf_url=order.get("pdf_url", "")
        )

    return case
