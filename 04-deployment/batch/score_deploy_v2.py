"""
score_deploy_v2.py

Deployment script for Prefect 2.14+ where the `Deployment` class is deprecated.
Uses the recommended `from_source(...).deploy()` approach for creating deployments.
"""

import os
from score import ride_duration_prediction
from prefect import flow

# Path to the directory containing your flow script
remote_source = "~/mlops-zoomcamp/04-deployment/batch"

# Entry point in the format "filename.py:function_name"
entrypoint = "score.py:ride_duration_prediction"

# Create and deploy the flow using the from_source method
ride_duration_prediction.from_source(
    source=remote_source,
    entrypoint=entrypoint
).deploy(
    name="ride_duration_prediction",  #  Name for the deployment
    parameters={
        "taxi_type": "green",
        "run_id": "e1efc53e9bd149078b0c12aeaa6365df",
    },
    cron="0 3 2 * *",  # Schedule to run at 3 AM on the 2nd of every month
    description="Process-based deployment for applying ML models to taxi data",
    tags=["ml", "taxi", "batch-processing", "process-pool"],
    version="1.0.0",
    # work_queue_name="ml",       # Uncomment if you have a specific work queue
    # work_pool_name="my-process-pool",  # Uncomment if using a custom work pool
)
