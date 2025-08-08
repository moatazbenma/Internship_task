from .models import QueryLog, CaseData, Order
from django.utils import timezone

def save_scraped_data(data):
    query_log = QueryLog.objects.create(
        timestamp=timezone.now(),
        case_type=data.get("case_number", "").split("/")[0],
        case_number=data.get("case_number", "").split("/")[1],
        year=int(data.get("case_number", "").split("/")[-1]),
        success=True,
        raw_html=data.get("raw_html", ""),
        cnr_number=data.get("cnr", "Unknown")
    )

    # Save case data
    case = CaseData.objects.create(
        query=query_log,
        court_name=data.get("court_name", "Unknown"),
        registration_date=data.get("registration_date"),
        petitioner=data.get("petitioner", "Unknown"),
        respondent=data.get("respondent", "Unknown"),
        filing_date=data.get("filing_date"),
        hearing_date=data.get("hearing_date"),
        status=data.get("status", "Unknown"),
        order_link=None,
        case_number=data.get("case_number", "Unknown")
    )

    # Save orders
    for order in data.get("orders", []):
        Order.objects.create(
            case=case,
            date=order.get("date"),
            pdf_url=order.get("pdf_url"),
            summary=order.get("summary", "Not available")
        )

    return case
