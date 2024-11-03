from fastapi import FastAPI
from server.routers import experiments, runs, reporting, visualization, export

app = FastAPI(
    title="OptunaGui API",
    description="API for managing experiments, runs, reports, and visualizations for hyperparameter tuning.",
    version="1.0.0",
)

app.include_router(experiments.router, prefix="/experiments", tags=["Experiments"])
app.include_router(runs.router, prefix="/runs", tags=["Runs"])
app.include_router(reporting.router, prefix="/reporting", tags=["Reporting"])
app.include_router(visualization.router, prefix="/visualization", tags=["Visualization"])
app.include_router(export.router, prefix="/export", tags=["Export"])
