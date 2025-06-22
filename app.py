import gradio as gr
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb


with open("models/energy_consumption.pkl", "rb") as f:
    model = pickle.load(f)


def predict_energy(
    Per_Capita_Energy_Use, Renewable_Energy_Share, Fossil_Fuel_Dependency,
    Industrial_Energy_Use, Household_Energy_Use, Carbon_Emissions, Energy_Price_Index,
    country
):
    
    country_list = ["Australia", "Brazil", "Canada", "China", "Germany", 
                    "India", "Japan", "Russia", "UK", "USA"]
    country_encoded = [1.0 if c == country else 0.0 for c in country_list]

    
    data = {
        "Per_Capita_Energy_Use": Per_Capita_Energy_Use,
        "Renewable_Energy_Share": Renewable_Energy_Share,
        "Fossil_Fuel_Dependency": Fossil_Fuel_Dependency,
        "Industrial_Energy_Use": Industrial_Energy_Use,
        "Household_Energy_Use": Household_Energy_Use,
        "Carbon_Emissions": Carbon_Emissions,
        "Energy_Price_Index": Energy_Price_Index,
    }
    
    for i, c in enumerate(country_list):
        data[f"Country_{c}"] = country_encoded[i]

    df = pd.DataFrame([data])
    dmatrix = xgb.DMatrix(df, feature_names=df.columns.tolist())

    prediction = float(model.predict(dmatrix)[0])
    return round(prediction, 3)


demo = gr.Interface(
    fn=predict_energy,
    inputs=[
        gr.Slider(0, 1, label="Per Capita Energy Use"),
        gr.Slider(0, 1, label="Renewable Energy Share"),
        gr.Slider(0, 1, label="Fossil Fuel Dependency"),
        gr.Slider(0, 1, label="Industrial Energy Use"),
        gr.Slider(0, 1, label="Household Energy Use"),
        gr.Slider(0, 1, label="Carbon Emissions"),
        gr.Slider(0, 1, label="Energy Price Index"),
        gr.Dropdown(["Australia", "Brazil", "Canada", "China", "Germany", 
                     "India", "Japan", "Russia", "UK", "USA"], label="Country")
    ],
    outputs="number",
    title="Energy Consumption Predictor",
    description="Predict energy consumption score based on fuel and economic parameters."
)


demo.launch()