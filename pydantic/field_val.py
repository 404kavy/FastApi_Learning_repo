from dataclasses import Field
from typing import Dict, List
from pydantic import BaseModel, EmailStr, Field , AnyUrl
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


    @field_validator('email')
    @classmethod
    def email_val(cls, value):
        valid_domains = ['hdfc.com', 'gmail.com', 'yahoo.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Invalid email domain. Allowed domains are: {valid_domains}")
        return value


    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.title()  # Capitalize the first letter of each word in the name

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
        "contact_details": {'phone': ' 999999999'}
    }
