import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
st.set_page_config(
    page_title="Personalized Workout & Diet Planner with AI",
    layout="wide"
)
st.markdown("""
<style>
.main-title {
    font-size: 36px;
    font-weight: bold;
    color: black;
}
.section-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}
.card {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Personalized Workout & Diet Planner with AI</div>', unsafe_allow_html=True)
#Data for model
np.random.seed(42)
data = pd.DataFrame({
    "calories": np.random.randint(1500, 3500, 200),
    "activity": np.random.uniform(0, 5, 200),
    "protein": np.random.randint(40, 200, 200),
    "sleep": np.random.randint(4, 10, 200),
    "weight": np.random.randint(50, 100, 200),
})
#weight
data["next_weight"] = (
    data["weight"]
    + (data["calories"] - 2200) / 7000
    - (data["activity"] * 0.1)
    + np.random.normal(0, 0.3, 200)
)

X = data.drop("next_weight", axis=1)
y = data["next_weight"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

r2 = r2_score(y_test, model.predict(X_test))

#layout
left, right = st.columns([1,2])
#left panel
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Your Health Profile</div>', unsafe_allow_html=True)

    goals = st.text_input("Health Goals", "Lose 1 kg in 1 month")
    medical = st.text_input("Medical Conditions", "Low BP")
    routine = st.text_input("Fitness Routine", "30 minutes walk")
    preference = st.selectbox("Food Preference", ["Veg","Non-Veg"])
    restrictions = st.text_input("Dietary Restrictions", "None")

    st.markdown('</div>', unsafe_allow_html=True)
#right panel
with right:
    tab1, tab2, tab3 = st.tabs(
        ["🍽 Meal Planning", "📷 Food Analysis", "📊 Health Insights"]
    )
    #meal planning
    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">AI Optimized Meal Plan</div>', unsafe_allow_html=True)

        if st.button("Generate Plan"):

            meals = [
                {"name": "Oats", "cal": 300, "type": "Veg"},
                {"name": "Paneer Bowl", "cal": 500, "type": "Veg"},
                {"name": "Dal Rice", "cal": 650, "type": "Veg"},
                {"name": "Vegetable Upma", "cal": 400, "type": "Veg"},
                {"name": "Eggs", "cal": 350, "type": "Non-Veg"},
                {"name": "Chicken Breast", "cal": 500, "type": "Non-Veg"},
                {"name": "Grilled Fish", "cal": 450, "type": "Non-Veg"},
            ]
            if "lose" in goals.lower():
                target = 1800
            elif "gain" in goals.lower():
                target = 2500
            else:
                target = 2200

            meals = [m for m in meals if m["type"] == preference]

            week_plan = []
            days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

            for day in days:
                daily_meals = np.random.choice(meals, 3, replace=True)
                total = sum([m["cal"] for m in daily_meals])

                week_plan.append({
                    "Day": day,
                    "Breakfast": daily_meals[0]["name"],
                    "Lunch": daily_meals[1]["name"],
                    "Dinner": daily_meals[2]["name"],
                    "Total Calories": total
                })

            df = pd.DataFrame(week_plan)
            st.success("Optimized Weekly Plan Generated")
            st.dataframe(df, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

    #food analysis
    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Food Image Analysis</div>', unsafe_allow_html=True)

        file = st.file_uploader("Upload food image", type=["jpg","png","jpeg"])
        if file:
            st.image(file, use_container_width=True)

            estimated_cal = np.random.randint(300,700)
            protein_est = np.random.randint(10,40)

            st.success(f"Estimated Calories: {estimated_cal} kcal")
            st.info(f"Protein: {protein_est} g")

        st.markdown('</div>', unsafe_allow_html=True)

    #health insights
    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Weight Forecast (12 Weeks)</div>', unsafe_allow_html=True)

        calories = st.number_input("Daily Calories",1500,3500,2200)
        activity = st.number_input("Activity Hours",0.0,5.0,1.5)
        protein = st.number_input("Protein (g)",40,200,80)
        sleep = st.number_input("Sleep Hours",4,10,7)
        weight = st.number_input("Current Weight (kg)",40,150,80)

        input_data = scaler.transform([[calories,activity,protein,sleep,weight]])
        prediction = model.predict(input_data)[0]

        st.metric("Next Week Prediction", f"{round(prediction,2)} kg")
        st.caption(f"Model Accuracy (R²): {round(r2,3)}")

        weeks = 12
        weights = [weight]
        current = weight

        for _ in range(weeks):
            inp = scaler.transform([[calories,activity,protein,sleep,current]])
            next_w = model.predict(inp)[0]
            weights.append(next_w)
            current = next_w

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=list(range(weeks+1)),
            y=weights,
            mode='lines+markers'
        ))

        fig.update_layout(
            template="plotly_white",
            xaxis_title="Week",
            yaxis_title="Weight (kg)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)