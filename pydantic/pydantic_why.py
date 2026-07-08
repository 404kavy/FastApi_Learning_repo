from pydantic import BaseModel, EmailStr, Field , AnyUrl
from typing import List,Dict,Optional, Annotated

class ContactDetails(BaseModel):
    phone: str


class Patient(BaseModel):
    name:Annotated[str, Field(min_length=3, max_length=50, title='Patient Name', description="Name of the patient", example="John Doe")]
    email: EmailStr
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0, strict = True)
    married:Annotated[bool , Field(default=None)] = None
    allergies: Annotated[list[str] | None, Field(default=None)] = None
    contact_details: ContactDetails | None = None
    url :AnyUrl | None = None
    def insert_patient_data(self):
        print(self.age)
        print(self.name)
        print(self.weight)
        print(self.married)
        print(self.allergies)
        print(self.contact_details)
        print(self.email)
        print(self.url)
        print("Inserted into database")


patient_info = {
    "name": "kavya",
    "email": "abc@gmail.com",
    "age": 19,
    "weight": 50.55,
    "married": True,
    "allergies": ['pollen', 'dust'],
    "contact_details": {'phone': ' 999999999'},
    "url": "https://example.com"
}

patient1 = Patient(**patient_info)
patient1.insert_patient_data()