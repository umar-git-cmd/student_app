import streamlit as st
import requests
api_url = 'http://127.0.0.1:8000/predict'

st.title('Прогноз writing score')

gender = st.selectbox('Пол', ['male', 'female'])
race = st.selectbox('Группа', ['group A', 'group B', 'group C', 'group D', 'group E '])
parental = st.selectbox('Образование родителей', ["bachelor's degree", 'high school', "master's degree", 'some collage', 'some high school', "associate's degree"])
lunch = st.selectbox('Обед', ['standard', 'free/reduced'])
test = st.selectbox('Тест', ['completed', 'none'])
math_score = st.number_input('Балы по математике:', min_value=0, max_value=100, value=0)
reading_score = st.number_input('Балы по чтению:', min_value=0, max_value=100, value=0)

student_data = {
    "gender": gender,
    "race_ethnicity": race,
    "parental": parental,
    "lunch": lunch,
    "test": test,
    "math_score": math_score,
    "reading_score": reading_score
}

if st.button('Проверка'):

    try:
        answer = requests.post(api_url, json=student_data, timeout=10)
        if answer.status_code == 200:
            result = answer.json()
            st.success(f"Результат: {result.get('Writing_score')}")
            #st.json(result)
        else:
            st.error(f'Oшибка: {answer.status_code}')
    except requests.exceptions.RequestException:
        st.error(f'Не удалось подключиться к API')