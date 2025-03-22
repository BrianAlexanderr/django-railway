# MedicAI Backend
This repository is the backend for the app https://github.com/BrianAlexanderr/MedicAI_mini-project <br>
<br><br>

## Notes
Because this is my first time creating such backend for my projec, i know that there is alot of improvement to make on the logic, or API efficiency on taking the request. <br>
So feel free to contact me and tells me! :D

## Features

- Save the new user credential

- User authentication (Firebase Authentication)

- Retrieve Symptoms and display on the apps

- API for diagnosing diseases based on symptoms

- Save diagnose history

- Database integration with Supabase

- CORS enabled for frontend interaction

<br>

Tech Stack

- Backend: Django, Django REST Framework

- Database: Supabase

- Deployment: Railway

<br>

## Installation

- ### Prerequisites

Make sure you have Python installed. You can check by running:

`python --version`

- ### Clone the Repository

`git clone https://github.com/yourusername/medicai-backend.git`
`cd medicai-backend`

- ### Create a Virtual Environment

`python -m venv venv`
`source venv/bin/activate`  # On Windows: venv\Scripts\activate

- ### Install Dependencies

`pip install -r requirements.txt`

- ### Set Up Environment Variables

Create a .env file in the root directory and add the following:
```
SECRET_KEY=your_secret_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```
- ### Apply Migrations

`python manage.py migrate`

- ### Run the Server

`python manage.py runserver`

Then the url serve as the endpoint communication between the frontend and the backend. 
<br><br>

## API Endpoints
-----------------------------------------------------------------------------------------------------
| Method     | Endpoint                                           | Description                     |
|------------|----------------------------------------------------|---------------------------------|
| POST       | /api/predict_disease/                              | Predict disease                 |
| GET        | /api/symptoms/                                     | Retrieve symptoms               |
| POST       | /api/register_user/                                | Register User                   |
| GET        | /api/facilities/                                   | Retrieve Hospital               |
| GET        | /api/facilities/photo/(id facility)/               | Retrieve Hospital based on ID   |
| POST       | /api/get_symptom_names/                            | Retrieve symptom names          |
| GET        | api/doctors/(disease id)/                          | Recommend doctor based on ID    |
| POST       | /api/get_precautions/                              | Retrieve precautions            |
| POST       | /api/save_diagnosis/                               | Save diagnose                   |
| GET        | api/medical_history/(user id)/                     | Retrieve history based on ID    |
-----------------------------------------------------------------------------------------------------

<br><br>

## Deployment

This project is deployed on Railway.<br>
To deploy:<br>
Push changes to the repository.<br>
Railway will automatically detect and deploy changes.
<br><br><br>

## Contributing

Feel free to submit issues or pull requests to improve the project!

## Contact
LinkedIn -> https://www.linkedin.com/in/brian-alexander-490ab0319/

## License

This project is licensed under the MIT License.
