"""
Jules API Automation Script
Steps Covered:
1. List sources
2. Create session
3. List sessions
4. Approve plan
5. Send message and list activities
"""

import requests, json, time

# 🧠 STEP 1: Fill your own API key and source here
API_KEY = "YOUR_API_KEY"  # ← Replace this with your Jules API key
SOURCE_NAME = "sources/github/yourusername/yourrepo"  # ← Replace this

BASE_URL = "https://jules.googleapis.com/v1alpha"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": API_KEY
}


# 🪄 Step 1: List your sources
def list_sources():
    print("\n🔹 Listing your connected sources...")
    url = f"{BASE_URL}/sources"
    res = requests.get(url, headers=headers)
    print(json.dumps(res.json(), indent=2))
    return res.json()


# 🪄 Step 2: Create a new session
def create_session():
    print("\n🔹 Creating a new session...")
    url = f"{BASE_URL}/sessions"
    data = {
        "prompt": "Create a sample Flask app that shows Hello Jules!",
        "sourceContext": {
            "source": SOURCE_NAME,
            "githubRepoContext": {"startingBranch": "main"}
        },
        "title": "Flask App Demo"
    }
    res = requests.post(url, headers=headers, data=json.dumps(data))
    print(json.dumps(res.json(), indent=2))
    return res.json().get("id")


# 🪄 Step 3: List all sessions
def list_sessions():
    print("\n🔹 Listing all sessions...")
    url = f"{BASE_URL}/sessions?pageSize=5"
    res = requests.get(url, headers=headers)
    print(json.dumps(res.json(), indent=2))
    return res.json()


# 🪄 Step 4: Approve a plan (if required)
def approve_plan(session_id):
    print(f"\n🔹 Approving plan for session {session_id}...")
    url = f"{BASE_URL}/sessions/{session_id}:approvePlan"
    res = requests.post(url, headers=headers)
    print("Status Code:", res.status_code)
    if res.status_code == 200:
        print("✅ Plan approved successfully!")
    else:
        print("⚠️ Plan may not require approval or an error occurred.")


# 🪄 Step 5: Send a message to the agent
def send_message(session_id):
    print(f"\n🔹 Sending message to session {session_id}...")
    url = f"{BASE_URL}/sessions/{session_id}:sendMessage"
    data = {"prompt": "Can you modify it to use HTML templates?"}
    res = requests.post(url, headers=headers, data=json.dumps(data))
    print("Message sent. Status Code:", res.status_code)


# 🪄 Step 6: List all activities to see agent’s response
def list_activities(session_id):
    print(f"\n🔹 Listing activities for session {session_id}...")
    url = f"{BASE_URL}/sessions/{session_id}/activities?pageSize=30"
    res = requests.get(url, headers=headers)
    print(json.dumps(res.json(), indent=2))


# 🚀 Run all steps in sequence
if __name__ == "__main__":
    list_sources()
    session_id = create_session()
    if session_id:
        list_sessions()
        time.sleep(2)
        approve_plan(session_id)
        time.sleep(2)
        send_message(session_id)
        time.sleep(3)
        list_activities(session_id)
    else:
        print("❌ Could not create session. Check your API key or source name.")
