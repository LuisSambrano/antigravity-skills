import os
import requests
import json
import sys

# Configuration
N8N_BASE_URL = "http://localhost:5678/api/v1"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1ZGZhNTAxNS0yOTA3LTQwMjUtYWNhNS1hOTc1ZDY1NGQ4ODciLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzY5OTA3NDM2fQ.DSxE5w47NpsqLIFqSp91JjNUDqiS6pVW01mCGiPMKWk" # In prod, use env var

HEADERS = {
    "X-N8N-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

def list_workflows():
    try:
        response = requests.get(f"{N8N_BASE_URL}/workflows", headers=HEADERS)
        response.raise_for_status()
        workflows = response.json().get('data', [])
        print(f"✅ Connection Successful. Found {len(workflows)} workflows.")
        for w in workflows:
            print(f"- {w['name']} (ID: {w['id']}) - Active: {w['active']}")
        return workflows
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting to n8n: {e}")
        if hasattr(e, 'response') and e.response is not None:
             print(f"Response: {e.response.text}")
        sys.exit(1)

def create_workflow(name, nodes, connections):
    payload = {
        "name": name,
        "nodes": nodes,
        "connections": connections,
        "settings": {},
    }
    try:
        response = requests.post(f"{N8N_BASE_URL}/workflows", headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
        print(f"✅ Workflow '{name}' created successfully! ID: {data['id']}")
        return data
    except requests.exceptions.HTTPError as e:
         print(f"❌ Error creating workflow: {e}")
         print(f"Response Body: {e.response.text}")
         sys.exit(1)
    except Exception as e:
         print(f"❌ Error creating workflow: {e}")
         sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python n8n_manager.py [list|create] [args]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        list_workflows()
    elif command == "create":
        # Expecting a JSON file path for workflow definition
        if len(sys.argv) < 4:
            print("Usage: python n8n_manager.py create <WorkflowName> <PathToJSON>")
            sys.exit(1)
        
        name = sys.argv[2]
        json_path = sys.argv[3]
        
        with open(json_path, 'r') as f:
            wf_data = json.load(f)
            
        # Handle full workflow export format vs simple nodes/connections
        nodes = wf_data.get('nodes', [])
        connections = wf_data.get('connections', {})
        
        create_workflow(name, nodes, connections)
