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
