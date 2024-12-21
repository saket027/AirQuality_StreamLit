import json
import streamlit as st
import requests


user_options = {}

st.title('AirQuality Prediction')

streamlit_options = json.load(open("streamlit_options.json"))
for field_name, range in streamlit_options["slider_fields"].items():
    min_val, max_val = range
    current_value = round((min_val + max_val)/2)
    user_options[field_name] = st.sidebar.slider(field_name, min_val, max_val, value=current_value)

for field_name, values in streamlit_options["single_select_fields"].items():
    user_options[field_name] = st.sidebar.selectbox(field_name, values)


user_options


if st.button('Predict'):
    data = json.dumps(user_options, indent=2)
    r = requests.post('http://127.0.0.1:8000/predict', data=data)
    st.write(r.json())
















# import json
# import streamlit as st
# import requests

# # Set your deployed model endpoint here
# # API_URL = "http://localhost:8501"  # Replace with your actual endpoint

# st.set_page_config(page_title="Air Quality Prediction", page_icon="🌱")

# st.title("Air Quality Prediction")
# st.write("Use the sidebar to input environmental conditions and get a predicted air quality level.")

# # Load configuration from JSON
# try:
#     streamlit_options = json.load(open("streamlit_options.json"))
# except FileNotFoundError:
#     st.error("streamlit_options.json not found. Please ensure it is in the same directory.")
#     st.stop()

# user_options = {}

# # Sidebar Inputs
# st.sidebar.title("Input Features")

# # Slider fields
# if "slider_fields" in streamlit_options:
#     for field_name, value_range in streamlit_options["slider_fields"].items():
#         if len(value_range) == 2:
#             min_val, max_val = value_range
#             current_value = round((min_val + max_val) / 2)
#             user_options[field_name] = st.sidebar.slider(
#                 label=field_name,
#                 min_value=min_val,
#                 max_value=max_val,
#                 value=current_value
#             )

# # Single-select fields
# if "single_select_fields" in streamlit_options:
#     for field_name, values in streamlit_options["single_select_fields"].items():
#         if isinstance(values, list) and values:
#             user_options[field_name] = st.sidebar.selectbox(field_name, values)
#         else:
#             st.warning(f"No values found for single-select field: {field_name}")

# # Predict Button
# if st.button("Predict"):
#     data = json.dumps(user_options)
#     with st.spinner("Predicting..."):
#         try:
#             response = requests.post(API_URL, data=data, headers={"Content-Type": "application/json"})
#             if response.status_code == 200:
#                 result = response.json()
#                 prediction = result.get("Prediction", "No prediction returned")
#                 st.success(f"Predicted Air Quality: {prediction}")
#             else:
#                 st.error(f"Error {response.status_code}: {response.text}")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")

# # Additional Notes or Instructions
# st.write("---")
# st.write("**Note**: Adjust the fields and endpoint as needed.")
