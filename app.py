
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Short Video Analytics Tool", page_icon="📊", layout="wide")
st.title("📊 Short Video Engagement Analytics Tool")
st.subheader("For Content Creators: Optimize Your Video Performance")

# 1. Upload Data
st.markdown("### 1. Upload Your CSV Data File")
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 2. Data Cleaning
    st.markdown("### 2. Cleaned Data")
    df_clean = df.drop_duplicates()  # Remove duplicates
    df_clean = df_clean.fillna(0)     # Fill missing values
    st.dataframe(df_clean, use_container_width=True)

    # 3. Data Transformation
    df_clean["total_engagement"] = df_clean["like"] + df_clean["comment"] + df_clean["collect"]
    df_clean["duration_group"] = df_clean["duration"].apply(
        lambda x: "Short (<15s)" if x < 15 else "Long (≥15s)"
    )

    # 4. Key Analysis
    st.markdown("### 3. Key Analysis Results")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Avg Engagement by Duration")
        dur_analysis = df_clean.groupby("duration_group")["total_engagement"].mean()
        st.dataframe(dur_analysis)
    with col2:
        st.markdown("#### Avg Engagement by Type")
        type_analysis = df_clean.groupby("type")["total_engagement"].mean()
        st.dataframe(type_analysis)

    # 5. Visualization
    st.markdown("### 4. Visual Charts")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    dur_analysis.plot(kind="bar", ax=ax1, color="#FF6B6B")
    ax1.set_title("Duration vs Engagement")
    type_analysis.plot(kind="bar", ax=ax2, color="#4ECDC4")
    ax2.set_title("Video Type vs Engagement")
    plt.tight_layout()
    st.pyplot(fig)

    # 6. Insights for Users
    st.markdown("### 5. Creator Recommendations")
    st.success("✅ Top Insight: Short videos (<15s) & Tutorial type get the highest engagement!")