# This file works with the azure application insights

import os
import logging
from azure.monitor.opentelemetry import configure_azure_monitor

#create a dedicated logger
logger = logging.getLogger("brand-guardian.-telemetry")

def setup_telemetry():
    '''
    Initializes Azure Monitor OpenTelemetry
    Tracks: HTTP requests, database queries, errors, performance metrics
    Sends this data to azure monitor

    It auto captures every API request
    No need to manually log each endpoint
    '''

    # Retrieve connection string
    connection_string = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")

    if not connection_string:
        logger.warning("No instrumentation key found. Telemetry is DISABLED.")
        return
    
    # Configure azure monitor

    try:
        configure_azure_monitor(
            connection_string = connection_string,
            logger_name = "brand_guardian_tracer"
        )
        logger.info("Azure monitor tracking Enabled and Connected.")
    except Exception as e:
        logger.error(f"Failed to initialize Azure Monitor : {e}")
        