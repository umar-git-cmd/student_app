from fastapi import FastAPI
import uvicorn
import joblib
from pydantic import BaseModel


student_app = FastAPI()


class StudentSchema(BaseModel):
    gender: str
    race_ethnicity: str
    parental: str
    lunch: str
    test: str
    math_score: int
    reading_score: int


@student_app.post('/predict')
async def student_predict(student: StudentSchema):
    student_dict = student.dict()

    gender = student_dict.pop('gender')
    gender1_0 = [
        1 if gender == 'male' else 0
    ]

    race = student_dict.pop('race_ethnicity')
    race1_0 = [
        1 if race == 'group B' else 0,
        1 if race == 'group C' else 0,
        1 if race == 'group D' else 0,
        1 if race == 'group E' else 0,
    ]
    parental = student_dict.pop('parental')
    parental1_0 = [
        1 if parental == "bachelor's degree" else 0,
        1 if parental == "high school" else 0,
        1 if parental == "master' degree" else 0,
        1 if parental == "some college" else 0,
        1 if parental == "some high school" else 0,
    ]
    lunch = student_dict.pop('lunch')
    lunch1_0 = [
        1 if lunch == 'standard' else 0
    ]
    test = student_dict.pop('test')
    test1_0 = [
        1 if test == 'none' else 0
    ]

    data = list(student_dict.values()) + gender1_0 + race1_0 + parental1_0 + lunch1_0 + test1_0
    scaler_data = scaler.transform([data])
    pred = model.predict(scaler_data)[0]
    return {'Writing_score': round(pred, 2)}

model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')


if __name__ == '__main__':
    uvicorn.run(student_app, host='127.0.0.1', port=8000)