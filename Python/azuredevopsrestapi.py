import requests
import time
import os
from requests.auth import HTTPBasicAuth

# ==========================
# CONFIG
# ==========================
ORG = "manaswinichenna31"
PROJECT = "AzureDecopsManaswini"
PAT = os.getenv("Azure_Pat")

POLL_INTERVAL = 10  # how often your program checks the pipeline status, it checks every 10 seconds

BASE_URL = f"https://dev.azure.com/{ORG}/{PROJECT}"
AUTH = HTTPBasicAuth("", PAT)

HEADERS = {
    "Content-Type": "application/json"
}

# ==========================
# LIST PIPELINES
# ==========================
def list_pipelines():
    url = f"{BASE_URL}/_apis/pipelines?api-version=7.1-preview.1"
    resp = requests.get(url, auth=AUTH)
    resp.raise_for_status()

    # Gives the list of pipeline objects, pipelines == [{"id": 12, "name": "CI"}, {"id": 34, "name": "Release"}]
    pipelines = resp.json()["value"] # resp is the HTTP response from Azure DevOps and returns JSON, where "value" is actual list of pipelines.
    print("\nAvailable Pipelines:")
    for p in pipelines:
        print(f"  ID: {p['id']} | Name: {p['name']}")

    return pipelines


# ==========================
# TRIGGER PIPELINE
# ==========================
def trigger_pipeline(pipeline_id, branch="refs/heads/main", variables=None):
    url = f"{BASE_URL}/_apis/pipelines/{pipeline_id}/runs?api-version=7.1-preview.1" # Create a new run for this pipeline ID

# "resources": { ... } - external inputs (Repositories, Pipelines, Containers) this pipeline run will use
# "repositories": { ... } - source code repositories needed for this run, "self": { ... }: The repository where this pipeline YAML lives
# "refName": "refs/heads/main" - Use this Git reference (branch or tag)
    payload = {
        "resources": {
            "repositories": {
                "self": {
                    "refName": branch
                }
            }
        }
    }

    if variables:
        payload["variables"] = {
            k: {"value": v} for k, v in variables.items()
        }
    # if variables={"ENV": "prod", "DEBUG": "false"}, output is "variables": { "ENV": { "value": "prod" }, "DEBUG": { "value": "false" }} These become pipeline variables, usable in YAML.

    resp = requests.post(url, json=payload, auth=AUTH, headers=HEADERS) # pipeline starts running, output : in Json format {"id": 456,  "state": "inProgress"}

    resp.raise_for_status()

    run = resp.json()
    print(f"\nPipeline triggered. Run ID: {run['id']}")
    return run["id"]


# ==========================
# CHECK PIPELINE STATUS
# ==========================
def get_pipeline_run(pipeline_id, run_id):
    url = f"{BASE_URL}/_apis/pipelines/{pipeline_id}/runs/{run_id}?api-version=7.1-preview.1"
    resp = requests.get(url, auth=AUTH)
    resp.raise_for_status()
    return resp.json()


def wait_for_completion(pipeline_id, run_id):
    print("\nWaiting for pipeline to complete...")

    while True:
        run = get_pipeline_run(pipeline_id, run_id) # example output would be: run = {"id": 456, "state": "inProgress", "result": None, "createdDate": "2024-01-10T12:00:00Z"}


        state = run["state"] # state: inProgress, completed, cancelling
        result = run.get("result") # result: succeeded, failed, canceled

        print(f"  State: {state} | Result: {result}")

        if state == "completed":
            return result

        time.sleep(POLL_INTERVAL) # checks for pipeline status every 10 seconds, until finishied


# ==========================
# MAIN
# ==========================
def main():
    pipelines = list_pipelines()

    pipeline_id = int(input("\nEnter pipeline ID to trigger: ").strip())

    run_id = trigger_pipeline(
        pipeline_id=pipeline_id,
        branch="refs/heads/main",
        variables=None
    )

    final_result = wait_for_completion(pipeline_id, run_id)

    print("\nPipeline finished!")
    print("Final result:", final_result)


if __name__ == "__main__":
    main()

# output
# Available Pipelines:
#   ID: 2 | Name: AzureDecopsManaswini
#   ID: 3 | Name: AzureDevopsBuildDocker
#   ID: 1 | Name: manaswini3103.MavenHelloWorld
# 
# Enter pipeline ID to trigger: 2
# 
# Pipeline triggered. Run ID: 17
# 
# Waiting for pipeline to complete...
#   State: inProgress | Result: None
#   State: inProgress | Result: None
#   State: inProgress | Result: None
#   State: completed | Result: succeeded
# 
# Pipeline finished!
# Final result: succeeded
# PS C:\Users\chennasa\OneDrive - CDK Global LLC\Documents\GIT> 
