import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# PAGE CONFIG
st.set_page_config(
    page_title="Supply Chain AI",
    page_icon="📦",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.stApp {
    background-color: #0B1120;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="metric-container"] {
    background: linear-gradient(135deg, #1E293B, #0F172A);
    border: 1px solid #334155;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

h1, h2, h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.title("📌 Navigation")

# FILTERS
st.sidebar.markdown("---")

st.sidebar.subheader("⚙️ Dashboard Filters")

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All", "Electronics", "Clothing", "Food", "Furniture"]
)

selected_days = st.sidebar.slider(
    "Select Forecast Days",
    7,
    30,
    10
)

live_data = st.sidebar.checkbox(
    "Enable Live Data Simulation"
)

# PAGE NAVIGATION
page = st.sidebar.radio(
    "Go To",
    ["Dashboard", "Forecasting", "Inventory", "Analytics"]
)

# TITLE
st.title("📦 AI Supply Chain Dashboard")

st.markdown("### Smart Demand Forecasting & Inventory Analytics")

st.markdown("---")

# DASHBOARD PAGE
if page == "Dashboard":

    st.subheader("📊 Dashboard Overview")

    # DYNAMIC KPI SECTION
    total_sales = np.random.randint(50000, 150000)

    total_orders = np.random.randint(1000, 5000)

    forecast_accuracy = np.random.randint(85, 99)

    inventory_stock = np.random.randint(500, 2000)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Revenue",
        f"${total_sales}",
        "+12%"
    )

    col2.metric(
        "📦 Orders",
        total_orders,
        "+5%"
    )

    col3.metric(
        "🎯 Accuracy",
        f"{forecast_accuracy}%",
        "+2%"
    )

    col4.metric(
        "🏭 Inventory",
        inventory_stock,
        "-3%"
    )

    st.markdown("---")

    # SALES TREND CHART
    st.subheader("📈 Sales Trend Analysis")

    dates = pd.date_range(
        start="2024-01-01",
        periods=30
    )

    # LIVE DATA SIMULATION
    if live_data:

        sales = np.random.randint(100, 700, 30)

    else:

        sales = np.random.randint(100, 500, 30)

    chart_data = pd.DataFrame({
        "Date": dates,
        "Sales": sales
    })

    line_fig = px.line(
        chart_data,
        x="Date",
        y="Sales",
        markers=True,
        template="plotly_dark",
        title="Sales Performance"
    )

    st.plotly_chart(
        line_fig,
        use_container_width=True
    )

# FORECASTING PAGE
elif page == "Forecasting":

    st.subheader("🤖 AI Demand Forecasting")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"],
        key="forecast_upload"
    )

    if uploaded_file is not None:

        # READ CSV
        data = pd.read_csv(uploaded_file)

        st.success("✅ File Uploaded Successfully!")

        st.write("### Dataset Preview")

        st.dataframe(data.head())

        # AI MODEL
        data["Date"] = pd.to_datetime(data["Date"])

        data["Day"] = np.arange(len(data))

        X = data[["Day"]]
        y = data["Sales"]

        from sklearn.linear_model import LinearRegression

        model = LinearRegression()

        model.fit(X, y)

        # FUTURE DAYS
        future_days = np.arange(
            len(data),
            len(data) + selected_days
        ).reshape(-1, 1)

        predictions = model.predict(future_days)

        # FUTURE DATES
        future_dates = pd.date_range(
            start=data["Date"].max(),
            periods=selected_days
        )

        # FORECAST DATAFRAME
        forecast_df = pd.DataFrame({
            "Date": future_dates,
            "Predicted Sales": predictions
        })

        st.write("### 📈 Future Sales Predictions")

        st.dataframe(forecast_df)

        # FORECAST GRAPH
        forecast_fig = px.line(
            forecast_df,
            x="Date",
            y="Predicted Sales",
            markers=True,
            title="AI Demand Forecast",
            template="plotly_dark"
        )

        st.plotly_chart(
            forecast_fig,
            use_container_width=True
        )

        # AI INSIGHTS
        st.markdown("---")

        st.subheader("🧠 AI Business Insights")

        average_sales = data["Sales"].mean()

        max_sales = data["Sales"].max()

        min_sales = data["Sales"].min()

        latest_prediction = predictions[-1]

        # INSIGHT LOGIC
        if latest_prediction > average_sales:

            st.success(
                "📈 AI Insight: Future demand is expected to increase."
            )

        else:

            st.warning(
                "📉 AI Insight: Sales growth may slow down."
            )

        # INVENTORY ALERT
        if max_sales > 300:

            st.info(
                "📦 Inventory Alert: High-demand products may require restocking."
            )

        # SALES SUMMARY
        st.write(f"✅ Average Sales: {average_sales:.2f}")

        st.write(f"🚀 Highest Sales: {max_sales}")

        st.write(f"📉 Lowest Sales: {min_sales}")

# INVENTORY PAGE
elif page == "Inventory":

    st.subheader("📦 Inventory Management")

    inventory_data = pd.DataFrame({
        "Category": [
            "Electronics",
            "Clothing",
            "Food",
            "Furniture"
        ],
        "Stock": [120, 80, 150, 60]
    })

    # CATEGORY FILTER
    if selected_category != "All":

        inventory_data = inventory_data[
            inventory_data["Category"] == selected_category
        ]

    pie_fig = px.pie(
        inventory_data,
        names="Category",
        values="Stock",
        template="plotly_dark",
        title="Inventory Distribution"
    )

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )

# ANALYTICS PAGE
elif page == "Analytics":

    st.subheader("📈 Business Analytics")

    bar_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr"],
        "Orders": [320, 450, 390, 500]
    })

    bar_fig = px.bar(
        bar_data,
        x="Month",
        y="Orders",
        template="plotly_dark",
        title="Monthly Orders"
    )

    st.plotly_chart(
        bar_fig,
        use_container_width=True
    )

    # ANALYTICS METRICS
    st.markdown("---")

    col1, col2 = st.columns(2)

    col1.metric(
        "📊 Growth Rate",
        "18%",
        "+4%"
    )

    col2.metric(
        "🚚 Delivery Efficiency",
        "92%",
        "+3%"
    )

# FOOTER
st.markdown("---")

st.write("🚀 AI Powered Supply Chain Forecasting System")