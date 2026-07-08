from pydantic import BaseModel, EmailStr
from typing import List


# Nested Model
class ContactDetails(BaseModel):
    phone: str
    emergency_contact: str


# Main Model
class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: ContactDetails


# -------------------------------
# Deserialization (Dict -> Model)
# -------------------------------

patient_data = {
    "name": "Kavya",
    "age": 19,
    "email": "404.kavya@gmail.com",
    "weight": 50.5,
    "married": False,
    "allergies": ["Dust", "Pollen"],
    "contact_details": {
        "phone": "9999999999",
        "emergency_contact": "8888888888"
    }
}

patient = Patient(**patient_data)

print("===== Patient Object =====")
print(patient)


# -------------------------------
# Access Nested Model
# -------------------------------

print("\n===== Nested Data =====")
print("Phone:", patient.contact_details.phone)
print("Emergency Contact:", patient.contact_details.emergency_contact)


# -------------------------------
# Serialization to Dictionary
# -------------------------------

patient_dict = patient.model_dump()

print("\n===== Serialized Dictionary =====")
print(patient_dict)


# -------------------------------
# Serialization to JSON
# -------------------------------

patient_json = patient.model_dump_json(indent=4)

print("\n===== Serialized JSON =====")
print(patient_json)


# -------------------------------
# Include Specific Fields
# -------------------------------

print("\n===== Include Only Name & Age =====")
print(patient.model_dump(include={"name", "age"}))


# -------------------------------
# Exclude Fields
# -------------------------------

print("\n===== Exclude Email =====")
print(patient.model_dump(exclude={"email"}))


# -------------------------------
# Nested Model Serialization
# -------------------------------

print("\n===== Contact Details Only =====")
print(patient.contact_details.model_dump())