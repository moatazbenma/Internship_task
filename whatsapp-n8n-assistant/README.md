# WhatsApp-Driven Google Drive Assistant (Internship Task 2)

This project is an **n8n workflow** that connects WhatsApp (via Twilio Sandbox) with Google Drive to perform file management tasks and generate summaries using AI.  
It was built using **n8n (Docker)**, **Twilio**, **Google Drive API**, and **ngrok** for webhook tunneling.

---

## 📌 Features
- **LIST** files in a Google Drive folder  
- **MOVE** a file to another folder  
- **DELETE** a file  
- **SUMMARY** of a document using AI (GPT-4o / Claude)  
- Maintains an action log in Google Sheets  

---

## 📂 Files to Submit
- `workflow.json` — Exported n8n workflow
- `README.md` — This setup guide

---


## 🎥 Demo Video

[Click to watch demo](https://www.youtube.com/watch?v=1FdKiSsphhc)



## 🚀 Setup Instructions

### 1️⃣ Clone / Download the Project
Place your `workflow.json` file in the project directory.

---

### 2️⃣ Create `docker-compose.yml`
```yaml

version: '3.1'

services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=admin
      - N8N_BASIC_AUTH_PASSWORD=password
    volumes:
      - ./.n8n:/home/node/.n8n
    
    
```

### 3️⃣ Start n8n in Docker
```bash
docker-compose up -d
```
n8n will now run locally on http://localhost:5678 with basic authentication.

### 4️⃣ Set Up ngrok for Webhooks
Install and run ngrok to expose n8n to the internet:
```bash
ngrok http 5678
```
Copy the Forwarding URL (e.g., https://xxxx.ngrok-free.app) for later use in Twilio.

### 5️⃣ Connect Twilio Sandbox for WhatsApp

Go to Twilio Console.
Activate Twilio Sandbox for WhatsApp.
Set the webhook URL to:
```bash
https://<your-ngrok-url>/webhook-test
```

### 6️⃣ Connect Google Drive to n8n
In n8n, add Google Drive credentials.
Use OAuth2 and grant permission to your Drive account.
Save the credentials.


### 7️⃣ Import the Workflow
In n8n, click Import Workflow.
Select your workflow.json.
Save the workflow.

### 📱 Usage

LIST /ProjectX

DELETE /ProjectX/report.pdf

MOVE /ProjectX/report.pdf /Archive

SUMMARY /ProjectX
