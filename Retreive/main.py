import json
from pickletools import pydict 
from fastapi import FastAPI, Path , HTTPException, Query
from fastapi import HTTPException as he
app = FastAPI()

#load data
def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

#basic endpoints 
@app.get('/')
def hello():
    return {'message':'Hello this is my first APi endpoint '}

@app.get('/about')
def about():
    return {'about':'this is patients api '}

#view data

@app.get('/view_data')
def view_data():
    data = load_data()
    return data


#paths and params

@app.get('/patient/{patient_id}')
def view_patients(patient_id: str = Path(..., description='Id of patient in the DB', example = 'P001')):
#first load all data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise he(status_code = 404 , detail='patient not found')
    
    

# query parameter 

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Can sort by Weight, height and bmi"), order: str = Query('asc' , description = "Sort in asc or desc order")):

    valid_fields = ['height', 'weight' , 'bmi']
    if sort_by not in valid_fields:
        raise he(status_code = 400 , detail=f'Invalid feild select from {valid_fields}')


    if order not in ['dsc','asc']:
        raise he(status_code = 400 , detail=f'Invalid feild select between asc or dsc')

    data = load_data()
    sort_order = True if order == 'dsc' else False

    sorted_data = sorted(data.values(), key= lambda x: x.get(sort_by , 0 ),reverse = sort_order
                         )
    return sorted_data








