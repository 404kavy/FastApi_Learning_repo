from pydantic import BaseModel, EmailStr
from typing import List


class ContactDetails(BaseModel):
    phone: str
    emergency_contact: str


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: ContactDetails


patient_info = {
    "name": "Kavya",
    "age": 19,
    "email": "404.kavya@gmail.com",
    "weight": 50.5,
    "married": False,
    "allergies": ["dust", "pollen"],
    "contact_details": {
        "phone": "9999999999",
        "emergency_contact": "8888888888"
    }
}

patient = Patient(**patient_info)

print(patient)
print(patient.contact_details.phone)
print(patient.contact_details.emergency_contact)