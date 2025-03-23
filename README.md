# image generation using API
author - atharva salunke

This project involves building a web application where users can enter a text prompt, and the application generates multiple AI-generated images using Google Cloud's Vertex AI Imagen API. The generated images are displayed in a visually appealing format. The project leverages Flask for the backend, Vertex AI for image generation, and HTML/CSS for the frontend.

📝 Steps to Perform the Project
⚙️ Step 1: Set Up Your Environment
Install required packages:

bash
Copy
Edit
pip install flask google-cloud-aiplatform pillow
Enable Vertex AI API in Google Cloud Console.

Set up a Google Cloud service account and authenticate:

bash
Copy
Edit
gcloud auth application-default login
🏗️ Step 2: Initialize Vertex AI and Flask
Create a new Flask project:

bash
Copy
Edit
mkdir ai-image-generator
cd ai-image-generator
Add the required files:

bash
Copy
Edit
/ai-image-generator
├── /templates
│   └── index.html
├── app.py
└── requirements.txt
