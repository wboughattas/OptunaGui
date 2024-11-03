from pydantic import BaseModel


class ReportGenerateResponse(BaseModel):
    """
    Model for the response containing the download link for a generated report.

    - **report_url**: URL for downloading the report as a PDF or similar format.

    Example:
    ```json
    {
      "report_url": "/reports/run_7890.pdf"
    }
    ```
    """
    report_url: str


class ExperimentNotesRequest(BaseModel):
    """
    Model for adding custom notes to an experiment for documentation purposes.

    - **notes**: Text notes describing insights, assumptions, or observations about the experiment.

    Example:
    ```json
    {
      "notes": "Tested new feature engineering techniques, saw improvement in model performance."
    }
    ```
    """
    notes: str


class ExperimentNotesResponse(BaseModel):
    """
    Model for confirming that notes have been added to an experiment.

    - **status**: Status message indicating the notes were added successfully.

    Example:
    ```json
    {
      "status": "note_added"
    }
    ```
    """
    status: str
