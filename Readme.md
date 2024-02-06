
## Overlay Settings API

### Base URL: http://127.0.0.1:5000/api/overlay

### Endpoints:

---

### GET /api/overlay

Description:
Get overlay settings.

Request:
- Method: GET
- URL: http://127.0.0.1:5000/api/overlay

Response:
- Status Code: 200 OK
- Content-Type: application/json

Sample Response:
<!-- json -->
{
  "_id": "ObjectId",
  "property1": "value1",
  "property2": "value2",
  // ... (other properties)
}
<!--  -->

---

### POST /api/overlay

Description:
Update or create overlay settings.

Request:
- Method: POST
- URL: http://127.0.0.1:5000/api/overlay
- Content-Type: application/json
- Body: JSON object containing overlay settings

Sample Request Body:
<!-- json -->
{
  "property1": "new_value1",
  "property2": "new_value2",
  // ... (other properties)
}
<!--  -->

Response:
- Status Code: 200 OK
- Content-Type: application/json

Sample Response:
<!-- json -->
{
  "message": "Overlay settings updated successfully"
}
<!--  -->

---

### DELETE /api/overlay

Description:
Delete overlay settings.

Request:
- Method: DELETE
- URL: http://127.0.0.1:5000/api/overlay

Response:
- Status Code: 200 OK
- Content-Type: application/json

Sample Response:
<!-- json -->
{
  "message": "Overlay settings deleted successfully"
}
<!--  -->

---

### GET /api/overlay/{overlay_id}

Description:
Get specific overlay settings by ID.

Request:
- Method: GET
- URL: http://127.0.0.1:5000/api/overlay/{overlay_id}

Response:
- Status Code: 200 OK
- Content-Type: application/json

Sample Response:
<!-- json -->
{
  "_id": "ObjectId",
  "property1": "value1",
  "property2": "value2",
  // ... (other properties)
}
<!--  -->

---

### PUT /api/overlay/{overlay_id}

Description:
Update specific overlay settings by ID.

Request:
- Method: PUT
- URL: http://127.0.0.1:5000/api/overlay/{overlay_id}
- Content-Type: application/json
- Body: JSON object containing updated overlay settings

Sample Request Body:
<!-- json -->
{
  "property1": "new_value1",
  "property2": "new_value2",
  // ... (other properties)
}
<!--  -->

Response:
- Status Code: 200 OK
- Content-Type: application/json

Sample Response:
<!-- json -->
{
  "message": "Overlay settings updated successfully"
}
<!--  -->

---

### DELETE /api/overlay/{overlay_id}

Description:
Delete specific overlay settings by ID.

Request:
- Method: DELETE
- URL: http://127.0.0.1:5000/api/overlay/{overlay_id}

Response:
- Status Code: 200 OK
- Content-Type: application/json

Sample Response:
<!-- json -->
{
  "message": "Overlay deleted successfully"
}
<!--  -->

---





<!-- SETUP DOCUMENTATION FOR USERS -->

# RTSP Video Streaming App User Documentation

## Introduction

Welcome to the RTSP Video Streaming App! This application allows you to stream and control RTSP video feeds. You can also manage video overlays to display additional information on the video stream.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Accessing the App](#accessing-the-app)
2. [Streaming Video](#streaming-video)
   - [Inputting RTSP URL](#inputting-rtsp-url)
   - [Controlling Video Playback](#controlling-video-playback)
3. [Managing Overlays](#managing-overlays)
   - [Creating an Overlay](#creating-an-overlay)
   - [Updating an Overlay](#updating-an-overlay)
   - [Deleting an Overlay](#deleting-an-overlay)
4. [Troubleshooting](#troubleshooting)

## Getting Started

### Installation

Make sure you have the following installed:

- [Python](https://www.python.org/) (version 3.6 or higher)
- [Node.js](https://nodejs.org/) (for the React app)
- [MongoDB](https://www.mongodb.com/try/download/community) (as the database)

Clone the repository and install dependencies:

```bash
git clone https://github.com/your/repo.git
cd your-repo
pip install -r requirements.txt
npm install
```

### Accessing the App

Run the Flask application:

```bash
python app.py

Access the app in your web browser at [http://localhost:5000](http://localhost:5000).

## Streaming Video

### Inputting RTSP URL

On the app's homepage, you'll find an input field labeled "RTSP URL." Enter the RTSP URL of the video stream you want to view.

### Controlling Video Playback

- **Play/Pause:** Click the "Play" or "Pause" button to control video playback.
- **Volume:** Adjust the volume using the volume slider.

## Managing Overlays

### Creating an Overlay

1. In the "Video Overlay" section, enter the text you want to display as an overlay.
2. Click the "Create Overlay" button.

### Updating an Overlay

1. Modify the overlay text in the "Video Overlay" section.
2. Click the "Update Overlay" button.

### Deleting an Overlay

Click the "Delete Overlay" button to remove the current overlay.

## Troubleshooting

- **CORS Error:** If you encounter a CORS error, ensure that the Flask app allows requests from your React app's origin. Update the CORS configuration in `app.py`.

- **No Compatible Source:** If you see a "No compatible source" error, check that the RTSP URL is correct, and the video stream is accessible.

For additional assistance, please refer to the application's documentation or contact the support team.

---