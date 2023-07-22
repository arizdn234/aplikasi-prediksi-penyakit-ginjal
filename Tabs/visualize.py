import warnings
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree
import streamlit as st
from config import train_model

def app(df, x, y):
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Visualization of Kidney Disease Prediction Model")

    if st.checkbox("Plot Confusion Matrix"):
        model, score = train_model(x,y)
        plt.figure(figsize=(10,6))
        # ConfusionMatrixDisplay(model, x, y)
        y_pred = model.predict(x)
        cm = confusion_matrix(y, y_pred)
        cm_display = ConfusionMatrixDisplay(cm).plot()
        st.pyplot()

    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x,y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=4, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['nockd', 'ckd']
        )
        st.graphviz_chart(dot_data)

    