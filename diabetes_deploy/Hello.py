import streamlit as st

st.set_page_config(
    page_title="Hello",
)

st.markdown("# Welcome to My Portofolio 👋")

st.markdown(
    """
    I would like to share my final project about **Diabetes Prediction**

    You can find my notebook [here](https://github.com/nurullkhasanah/diabetes_prediction)

    ### **What is Diabetes?**

    Diabetes is a chronic disease that increases risk for stroke, kidney failure, renal complications, peripheral vascular disease, heart disease, and death (Xie, 2019)

    The International Diabetes Federation(IDF) estimates that at the current growth, 693 million people will have diabetes worldwide by 2045.

    The Centers for Disease Control and Prevention(CDC) recorded that in 2012, 29.1 million people in the United State were diagnosed diabetes. This condition put high financial burden for government because of medical cost and decreased productivity.

    According to IDF data, in 2021, Indonesia is in the fifth position with 19.5 million diabetes cases and estimated will increase to 28.6 million in 2045. 
    
    Based on above condition, it is very important to develop predictive model which could help to facilitate early diagnosis of diagnosis 
  

    ### Dataset Source
    The dataset that I use is data from a survey that was conducted by CDC through the Behavioral Risk Factor Surveillance System (BRFSS).
    It's a random-digit–dialed telephone survey of noninstitutionalized US adults aged 18 years or older.
    
    Check out the dataset in [Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data)

      👈 Select **Exploratory Data Analysis** from the sidebar to see the visualization of dataset.
    
    ### Predictive Modelling
    Here is a comparison of the 3 models
"""
)
image_path = "diabetes_deploy/f1_score.png"
st.image(image_path, caption="Model Evaluation")
st.markdown(
    """
    XGBoost Classifier model is the best model with f1 score 76.4%.

    👈 Select **Prediction** from the sidebar to predict your diabetes status!

    **Please note that you should be 18 years old or older!**
    """
)

