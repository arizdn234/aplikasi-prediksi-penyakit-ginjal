import streamlit as st
from config import predict

def app(df, x, y):

    st.title("Prediction Page")

    col1, col2, col3 = st.columns(3)
    
    # INPUT FIELD
    with col1:
        bp = st.text_input('Input blood pressure value')
    with col1:
        sg = st.text_input('Input specific gravity value')
    with col1:
        al = st.text_input('Input albumin value')
    with col1:
        su = st.text_input('Input sugar value')
    with col1:
        rbc = st.text_input('Input red blood cells value')
    with col1:
        pc = st.text_input('Input push cell value')
    with col1:
        pcc = st.text_input('Input push cell clumps value')
    with col1:
        ba = st.text_input('Input bacteria value')
    with col2:
        bgr = st.text_input('Input blood glucose random value')
    with col2:
        bu = st.text_input('Input blood urea value')
    with col2:
        sc = st.text_input('Input serum creatinine value')
    with col2:
        sod = st.text_input('Input sodium value')
    with col2:
        pot = st.text_input('Input pottasium value')
    with col2:
        hemo = st.text_input('Input haemoglobin value')
    with col2:
        pcv = st.text_input('Input packed cell volume value')
    with col2:
        wc = st.text_input('Input white blood cell count value')
    with col3:
        rc = st.text_input('Input red blood cell count value')
    with col3:
        htn = st.text_input('Input hypertension value')
    with col3:
        dm = st.text_input('Input diabetes mellitus value')
    with col3:
        cad = st.text_input('Input coronary artery disease value')
    with col3:
        appet = st.text_input('Input appetite value')
    with col3:
        pe = st.text_input('Input peda edema value')
    with col3:
        ane = st.text_input('Input aanemia value')

    # FEATURES INIT
    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]

    # PREDICT BUTTON
    if st.button("Predict Now!"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Prediction Success...")

        if (prediction == 1):
            st.warning("Data shows that this person is prone to kidney disease")
        else:
            st.success("The data shows that these people are relatively safe from kidney disease")

        st.write(f"This model has accuracy {score*100}%")
