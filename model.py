from roboflow import Roboflow
import streamlit as st

st.title('ASL detection')

rf = Roboflow(api_key="07xd4Fb9Jmy0RHi57x5x")
project = rf.workspace().project("american-sign-language-letters")
model = project.version(6).model

# infer on a local image
def predict():
    print(model.predict("k1.jpg", confidence=40, overlap=30).json())

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

st.button("evaluate image", type="primary", on_click=predict())