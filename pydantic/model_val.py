from dataclasses import Field
from typing import Dict, List
from pydantic import BaseModel, EmailStr, Field , AnyUrl, model_validator
from typing import List,Dict,Optional, Annotated
import narwhals
from pydantic import BaseModel, EmailStr, StrictInt, field_validator

class Patient(BaseModel):
    name: str
    age:  int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    @model_validator(mode='after')
    def validate_emergency_contact(self):
    
        if self.age > 60 and 'emergency_contact' not in self.contact_details:
            raise ValueError("Emergency contact is required for patients above 60 years of age.")
        return self

    def insert_patient_data(self):
        print(self.age)
        print(self.name)
        print(self.weight)
        print(self.married)
        print(self.allergies)
        print(self.contact_details) 
        print("updated")


patient_info={
        "name": "kavya",
        "age": 19,
        "email": '404.kavya@gmail.com',
        "married": False,
        "weight": 50.55,
        "allergies": ['pollen', 'dust'],
        "contact_details": {
    "phone": "999999999",
    "emergency_contact": "8888888888"
}
    }

updated_patient = Patient(**patient_info)
updated_patient.insert_patient_data()