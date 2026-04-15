# hornets-live-score-app
A live sports web app running on AWS serverless architecture
# Hornets Live Score App

A real-time sports dashboard built with AWS serverless architecture.

## Live Demo
Frontend hosted on AWS S3:
http://hornets-score-app-041426.s3-website-us-east-1.amazonaws.com/

## What it does
- Tracks live NBA game data
- Displays real-time score updates
- Updates automatically every 30 seconds
- Focused on the Charlotte Hornets

## Architecture

- AWS Lambda (Python backend)
- API Gateway (REST API)
- S3 Static Website Hosting (frontend)
- External NBA live data source

## Example API Response
```json
{
  "home": 102,
  "away": 98,
  "status": "3rd Quarter"
}

Tech Stack
Python
JavaScript
AWS Lambda
API Gateway
S3
HTML/CSS
 Team Focus

Built around the Charlotte Hornets live game data feed.
