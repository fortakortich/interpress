import pandas as pd

df = pd.read_csv("universities_extended_final_ru.csv")

def recommend_universities(inputs):
    filtered = df[
        (df["Минимальный GPA"] <= inputs["gpa"]) &
        (df["Минимальный IELTS"] <= inputs["ielts"]) &
        (df["Минимальный SAT"] <= inputs["sat"]) &
        (df["Минимальный AP"] <= inputs["ap"]) &
        (df["Минимальный бюджет ($)"] <= inputs["budget"]) &
        (df["Направление"] == inputs["major"]) &
        (df["Климат"] == inputs["climate"]) &
        (df["Уровень проектов"] <= inputs["project_level"])
    ]

    if filtered.empty:
        return []

    return filtered.sample(n=min(10, len(filtered)))[[
        "Название университета", "Страна", "Город", "Гранты", "Стоимость проживания", "Краткое описание"
    ]].to_dict(orient="records")
