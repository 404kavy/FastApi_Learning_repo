# 🏥 Patient Management System API

Welcome to the **Patient Management System API**! This repository is a comprehensive, beginner-to-intermediate guide to building RESTful APIs using **FastAPI** and **Pydantic**. 

Whether you are writing your first line of backend code or looking to solidify your understanding of data validation and serialization, this project is designed to teach you everything from scratch.

---

## 1. Project Overview

### What does this project do?
This project is a fully functional REST API that manages patient medical records. It allows users to create, read, update, and delete (CRUD) patient data. It also automatically calculates Body Mass Index (BMI) and provides a health verdict based on the patient's height and weight.

### What problem does it solve?
Managing patient records manually (e.g., in spreadsheets) is error-prone, lacks data validation (e.g., negative weights, invalid emails), and is hard to integrate with other systems. This API solves that by providing a structured, validated, and automated digital system.

### Why was this project built?
To serve as an educational blueprint. It bridges the gap between basic Python scripting and production-ready backend development, showcasing advanced Pydantic validation, data serialization, and FastAPI routing.

### Technologies Used
- **Python 3.10+**: The core programming language.
- **FastAPI**: A modern, high-performance web framework for building APIs.
- **Pydantic**: Data validation using Python type annotations.
- **JSON**: The lightweight data-interchange format used for storage.
- **Uvicorn**: An ASGI web server implementation for Python.

---

## 2. Folder Structure
FASTAPI/
├── pycache/ # Compiled Python bytecode (auto-generated)
├── .vscode/ # VS Code editor settings
── Create/ # Module for creating and managing patients
│ ├── pycache/
│ ├── main2.py # FastAPI app for Create/Update operations
│ └── patients.json # Database file for the Create module
├── pydantic/ # Module dedicated to Pydantic concepts
│ ├── field_val.py # Demonstrates @field_validator
│ ├── model_val.py # Demonstrates @model_validator
│ ├── nested_model.py # Demonstrates nested Pydantic models
│ ├── pydantic_why.py # Demonstrates Field, Annotated, Literal
│ └── serialization.py # Demonstrates model_dump and JSON serialization
├── Retrieve/ # Module for retrieving and sorting patients
│ ├── data.py # Script to generate 500 dummy patient records
│ ├── main.py # FastAPI app for Retrieve/Sort/Delete operations
│ ── patient.json # Database file for the Retrieve module
└── README.md # This file



### Purpose of Every File
- **`main.py` / `main2.py`**: The entry points for the FastAPI applications. They define the routes (endpoints) and business logic.
- **`patients.json` / `patient.json`**: Acts as our "database". Stores patient records in JSON format.
- **`data.py`**: A utility script that uses Python's `random` module to generate 500 realistic dummy records so we have data to test with.
- **`field_val.py` & `model_val.py`**: Standalone scripts teaching how to validate individual fields (like emails) and whole models (like checking if an elderly patient has an emergency contact).
- **`nested_model.py`**: Teaches how to structure complex data (e.g., a Patient having a nested ContactDetails object).
- **`pydantic_why.py`**: Explains the "why" behind Pydantic features like `Literal` and `EmailStr`.
- **`serialization.py`**: Teaches how to convert Pydantic objects into dictionaries or JSON strings for API responses.

---

## 3. Concepts Used (The Glossary)

*Before we look at code, let's understand the vocabulary.*

| Concept | What it is | Why we use it |
| :--- | :--- | :--- |
| **FastAPI** | A Python web framework for building APIs. | It's incredibly fast, easy to code, and auto-generates documentation. |
| **ASGI** | Asynchronous Server Gateway Interface. | Allows FastAPI to handle multiple requests concurrently (async). |
| **Uvicorn** | An ASGI web server. | FastAPI is just code; Uvicorn is the server that actually runs it on the internet. |
| **Pydantic** | A data validation library. | Ensures incoming data is the correct type (e.g., age is an int, not a string). |
| **BaseModel** | The parent class for all Pydantic models. | Gives your Python classes superpowers like automatic validation and serialization. |
| **JSON** | JavaScript Object Notation. | A text format for storing and transmitting data. Easy for humans and machines to read. |
| **REST API** | Representational State Transfer. | A standard architecture for web services (using HTTP methods like GET, POST). |
| **CRUD** | Create, Read, Update, Delete. | The four basic operations of persistent storage. |
| **Endpoint** | A specific URL where an API can be accessed. | e.g., `/patients` is an endpoint. |
| **Request Body** | Data sent by the client to the server. | Used in POST/PUT requests to send the new patient's details. |
| **Path Parameter** | A variable part of the URL. | e.g., `/patient/{patient_id}` where `P001` is the path parameter. |
| **HTTPException** | A FastAPI exception for errors. | Stops execution and sends a specific error code (like 404 Not Found) to the client. |
| **Decorator** | A function that modifies another function. | In FastAPI, `@app.get("/")` tells FastAPI to link the URL `/` to the function below it. |
| **Type Hints** | Annotations like `name: str`. | Tells Pydantic and developers what data type a variable should hold. |

---

## 4. Line-by-Line Code Explanation

*Note: To keep this readable, we will focus on the core application `Retrieve/main.py` and `Create/main2.py`. The concepts apply universally.*

### `Retrieve/main.py` (Core FastAPI App)

```python
# 1. IMPORTS
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
import json

# Why? We import FastAPI to create the app, Path/Query for URL parameters, 
# HTTPException for errors, and json to read/write our file.



# 2. APP INITIALIZATION
app = FastAPI()

# Why? Creates an instance of the FastAPI application. This is the core object.



# 3. PYDANTIC MODELS
class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender')]
    height: Annotated[float, Field(..., gt=0, description='Height in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight in kgs')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5: return 'Underweight'
        elif self.bmi < 25: return 'Normal'
        elif self.bmi < 30: return 'Overweight'
        else: return 'Obese'

# Why? Defines the exact structure of a Patient. 
# 'Annotated' and 'Field' add metadata and validation (gt=0 means greater than 0).
# 'computed_field' and '@property' automatically calculate BMI and Verdict without storing them.



# 4. UPDATE MODEL
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    # ... other fields are Optional

# Why? When updating, we don't want to send ALL fields. Optional allows partial updates.


# 5. HELPER FUNCTIONS
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

# Why? Encapsulates file I/O so we don't repeat open/read/write code in every endpoint.


# 6. ENDPOINTS
@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}

# Why? A simple root endpoint to verify the server is running.

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description='ID of the patient', example='P001')):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    return data[patient_id]

# Why? Fetches a single patient. Path(...) extracts 'P001' from the URL. 
# If not found, HTTPException stops execution and returns a 404 JSON error.


[Client / Swagger UI]
       │
       │ 1. Sends HTTP Request (e.g., GET /patient/P001)
       ▼
[Uvicorn Server]
       │
       │ 2. Receives request, passes to FastAPI
       ▼
[FastAPI Router]
       │
       │ 3. Matches URL to @app.get("/patient/{patient_id}")
       ▼
[Path Parameter Extraction]
       │
       │ 4. Extracts "P001" and validates it's a string
       ▼
[Function Execution]
       │
       │ 5. Calls load_data() -> reads patients.json
       ▼
[Business Logic]
       │
       │ 6. Checks if "P001" exists in dictionary
       ▼
[Response Generation]
       │
       │ 7. Returns dictionary -> FastAPI converts to JSON
       ▼
[Client]
       │
       │ 8. Receives 200 OK with Patient Data



Swagger UI 
   ↓ (Sends JSON Body)
FastAPI 
   ↓ (Parses Body)
Pydantic Model (Patient) 
   ↓ (Validates types, calculates BMI/Verdict)
model_dump(exclude={'id'}) 
   ↓ (Converts to Dict, removes ID to prevent spoofing)
Dictionary 
   ↓ (Adds ID: data[patient_id] = dict)
patients.json (via save_data)



Swagger UI 
   ↓ (Sends Query Params: ?sort_by=bmi&order=desc)
FastAPI 
   ↓ (Extracts Query params)
load_data() 
   ↓ (Reads JSON to Dict)
sorted() function 
   ↓ (Sorts dict values using lambda: x.get('bmi'))
JSONResponse 
   ↓ (Returns sorted list)
Client




Swagger UI 
   ↓ (Sends Query Params: ?sort_by=bmi&order=desc)
FastAPI 
   ↓ (Extracts Query params)
load_data() 
   ↓ (Reads JSON to Dict)
sorted() function 
   ↓ (Sorts dict values using lambda: x.get('bmi'))
JSONResponse 
   ↓ (Returns sorted list)
Client




Why use BaseModel? It enforces data integrity at the boundary of your application.
Key Pydantic Features Used
Annotated & Field: Allows adding metadata (descriptions, examples) and constraints (gt=0) without cluttering the type hint.
Literal: Restricts a string to a specific set of values (e.g., 'male', 'female'). Acts like an Enum.
Optional: Means the field can be None. Crucial for Update models.
@computed_field & @property: Calculates values on the fly. BMI is never stored in the JSON; it's always calculated from the latest height/weight.
model_dump(): Converts the Pydantic object into a standard Python dictionary.
exclude={'id'}: Prevents the client from overwriting the primary key.
exclude_unset=True: Only includes fields that were explicitly provided (vital for PATCH/PUT updates).


8. FastAPI Deep Dive
Why is FastAPI so fast?
Starlette: It's built on Starlette for the asynchronous web handling.
Pydantic: Uses Rust-based Pydantic core for lightning-fast data validation.
Type Hints: Leverages Python's native type hints, avoiding runtime reflection overhead.
HTTP Methods Explained
@app.get: Retrieve data. Safe, idempotent.
@app.post: Create new data. Not idempotent (calling twice creates two records).
@app.put: Replace existing data entirely.
@app.delete: Remove data.
JSONResponse vs Dict
FastAPI automatically converts returned Python dictionaries into JSON. However, if we need to set a custom status code (like 201 Created), we must explicitly return a JSONResponse.
python
return JSONResponse(status_code=201, content={'message': 'created'})



9. Every Parameter Explanation
Parameter
Used In
Purpose
Example
... (Ellipsis)
Field(...)
Marks a field as required.
Field(..., description="Name")
default=None
Field()
Makes a field optional.
Field(default=None)
gt / lt
Field()
Greater than / Less than validation.
Field(..., gt=0)
description
Field() / Path()
Adds text to Swagger UI docs.
description="Patient ID"
example
Field() / Path()
Shows a sample value in Swagger.
example="P001"
exclude
model_dump()
Omits keys from the output dict.
exclude={'id'}
exclude_unset
model_dump()
Only includes fields explicitly set.
exclude_unset=True
status_code
HTTPException
The HTTP error code to return.
status_code=404
detail
HTTPException
The error message body.
detail="Not found"
indent
json.dump()
Pretty-prints JSON with spaces.
indent=4
10. Functions Used
json.load(f): Reads a JSON file and converts it into a Python dictionary.
json.dump(data, f): Converts a Python dictionary into JSON and writes it to a file.
open('file.json', 'r'): Opens a file in read mode. Using with ensures it closes automatically.
round(number, 2): Rounds a float to 2 decimal places (used for BMI).
@property: A Python decorator that turns a method into a "getter" for an attribute.
.items(): Returns key-value pairs from a dictionary, used when iterating over update data.
sorted(): Python's built-in sorting function. We use a lambda to tell it which dictionary key to sort by.
11. Why Things Are Done (The "Why")
Why model_dump(exclude={'id'})?
Security. If we allow the client to send an id in the POST body, they could spoof another patient's ID. We generate/assign the ID on the server side.
Why computed_field for BMI?
Data Integrity. If we store BMI, what happens if the user updates their weight? The stored BMI becomes outdated. Calculating it on the fly ensures it's always accurate.
Why JSON instead of a Database?
Simplicity. For learning FastAPI, setting up PostgreSQL adds too much friction. JSON allows us to focus purely on API logic and Pydantic validation.
Why PatientUpdate class?
Flexibility. A full Patient model requires all fields. An update should only require the fields you want to change. Optional fields make this possible.
12. Best Practices
Naming Conventions
Use snake_case for Python functions and variables (load_data, patient_id).
Use PascalCase for Classes (Patient, PatientUpdate).
Code Improvements
Error Handling: Always catch FileNotFoundError when reading JSON files in case the file is deleted.
Async: Use async def for endpoints to allow concurrent request handling.
Security & Production
Never trust client input. Pydantic handles this, but always validate business logic (e.g., checking if a patient already exists before creating).
Environment Variables: Never hardcode file paths. Use os.getenv() or pydantic-settings.
13. API Documentation
Method
Endpoint
Purpose
Request Body / Params
Response
GET
/
Health check
None
{"message": "..."}
GET
/patient/{id}
Get one patient
Path: id
Patient Object
GET
/sort
Sort all patients
Query: sort_by, order
List of Patients
POST
/create
Create patient
Body: Patient
201 Created
PUT
/edit/{id}
Update patient
Path: id, Body: PatientUpdate
200 OK
DELETE
/delete/{id}
Delete patient
Path: id
200 OK
