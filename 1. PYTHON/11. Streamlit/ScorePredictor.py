import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# -----------------------------
# Load Data
# -----------------------------
data = pd.read_csv("student_data.csv")

X = data[["study_hours", "sleep_hours", "attendance"]]
y = data["score"]

# -----------------------------
# Train Model
# -----------------------------
model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎓 Student Score Predictor")

st.write("Predict exam scores using simple ML!")

# User Inputs
study_hours = st.slider("Study Hours", 0, 12, 6)
sleep_hours = st.slider("Sleep Hours", 0, 12, 7)
attendance = st.slider("Attendance (%)", 0, 100, 75)

# Prediction
prediction = model.predict(
    [[study_hours, sleep_hours, attendance]]
)

st.subheader("Predicted Score")

st.success(f"📚 Expected Score: {prediction[0]:.2f}")

# -----------------------------
# Visualization
# -----------------------------
st.subheader("Dataset Preview")
st.dataframe(data)

fig, ax = plt.subplots()

ax.scatter(data["study_hours"], data["score"])

ax.set_xlabel("Study Hours")
ax.set_ylabel("Score")
ax.set_title("Study Hours vs Score")

st.pyplot(fig)

 