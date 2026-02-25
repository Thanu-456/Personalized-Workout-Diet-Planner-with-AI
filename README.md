Personalized Workout & Diet Planner with AI
##  Project Overview

Personalized workout and diet planner ai is a Streamlit-based web application that generates personalized diet plans and predicts weight progression using machine learning.

Unlike generic fitness apps, this system considers user-specific health data, dietary preferences, and lifestyle factors to provide tailored recommendations and actionable health insights.

## Features

* Personalized health profile input
* AI-based weekly meal plan generation
* Weight prediction using Machine Learning
* 12-week weight forecasting visualization
* Food image upload with calorie & protein estimation
* Interactive dashboard with real-time updates

## System Approach

User Input → AI-Based Data Processing → ML Weight Prediction → AI Meal Optimization → Intelligent Visualization

The system:

* Collects personalized health information
* Preprocesses data using StandardScaler
* Uses Random Forest Regressor for prediction
* Generates goal-based weekly meal plans
* Visualizes 12-week weight trends using Plotly

##  Tech Stack

Frontend & Framework:

* Streamlit

Backend & ML:

* Python
* Scikit-learn (Random Forest Regressor)
* Pandas
* NumPy

Visualization:

* Plotly

## Machine Learning Model

Algorithm Used: Random Forest Regressor

Input Features:

* Daily calorie intake
* Activity level
* Protein intake
* Sleep hours
* Current weight

Output:

* Next week weight prediction
* 12-week weight forecast

Model performance evaluated using R² score.
Conclusion:
The system successfully delivers personalized workout and diet recommendations using machine learning predictions and AI-based content generation. An interactive Streamlit web interface enables users to input data and receive real-time insights with visual analytics. The project achieves an efficient, user-friendly, and scalable solution for fitness planning through a lightweight web development.

