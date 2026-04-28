'''
Main Execution Entry Point for Brand Guardian AI.
This file is the "control center" that starts and manages the entire compliance audit workflow. Think of it as the master switch that:
1. Sets up the audit request
2. Runs the AI workflow
3. Displays the final compliance report
'''

import uuid
import json
import logging
from pprint import pprint
from dotenv import load_dotenv

load_dotenv(override=True)

from backend.src.graph.workflow import app

logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("brand-guardian-runner")

def run_cli_simulation():
    '''
    Simulates the video compliance audit request.
    This function orchestrates the entire audit process:
    - Creates a unique session ID
    - Prepares the video URL and metadata
    - Runs it through the AI workflow
    - Displays the compliance results
    '''
    session_id = str(uuid.uuid4())
    logger.info(f"Starting Audit Session : {session_id}")

    # Define the initial state

    initial_inputs = {
        "video_url" : "https://youtu.be/dT7S75eYhcQ",
        "video_id" : f"vid_{session_id[:8]}",
        "compliance_results" : [],
        "errors" : []
    }

    print("n-----Initializing workflow...")
    print(f"Input Payload : {json.dumps(initial_inputs, indent=2)}")
    try: # Running the entire workflow
        final_state = app.invoke(initial_inputs) # triggers the langGraph workflow
        print("\n-----Workflow execution is complete...")

        print("\n Compliance Audit Report ==")
        print(f"Video ID: {final_state.get('video_id')}")
        print(f"status : {final_state.get('final_status')}")
        print("\n [Violations Detected]")
        results = final_state.get('compliance_results', [])
        if results :
            for issue in results :
                print(f"- [{issue.get('severity')}] [{issue.get('category')}] : [{issue.get('description')}]")
        else:
            print("No violations detected.")
        print("\n[Final Summary]")
        print(final_state.get('final_report'))

    except Exception as e:
        logger.error(f"Workflow Excecution Failed : {str(e)}")
        raise e

if __name__ == '__main__':
    run_cli_simulation()