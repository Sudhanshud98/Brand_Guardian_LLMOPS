import operator
from typing import Annotated, List, Dict, Optional, Any, TypedDict

# Defining schema for single compliance result
class ComplianceIssue(TypedDict):
    category : str
    description : str
    severity : str
    timestamp : Optional[str]

class VideoAuditState(TypedDict):
    '''
    Define the data schema for langgraph execution content
    '''

    video_url : str
    video_id : str
    local_file_path : Optional[str]
    video_metadata : Dict[str, Any]
    transcript : Optional[str]
    ocr_text : List[str]

    compliance_result : Annotated[List[ComplianceIssue], operator.add]

    # Final deliverabls
    fianl_status : str
    final_report : str

    # System observability
    errore : Annotated[List[str], operator.add]