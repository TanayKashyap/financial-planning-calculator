import streamlit as st
import plotly.graph_objects as go
import numpy as np
from dataframe import inflation, countries, growth, industries


st.set_page_config(
    page_title="Financial Planning Calculator")

st.title("Financial Planning Calculator")

# Income Section
st.header("**Monthly Income**")
st.subheader("Salary")
colAnnualSal, colTax = st.columns(2)

with colAnnualSal:
    salary = st.number_input(
        "Enter your Annual Salary($): ", min_value=0.0, format='%f')
with colTax:
    tax_rate = st.number_input(
        "Enter your tax rate(&): ", min_value=0.0, format='%f')

tax_rate = tax_rate/100
salary_after_taxes = salary * (1-tax_rate)
monthly_takehome_salary = round(salary_after_taxes / 12.0, 2)

# Expenses
st.header("**Monthly Expenses**")
colExpenses1, colExpenses2 = st.columns(2)

with colExpenses1:
    st.subheader("Monthly Rental")
    monthly_rental = st.number_input(
        "Enter your monthly rental($): ", min_value=0.0, format='%f')

    st.subheader("Monthly Food Budget")
    monthly_food = st.number_input(
        "Enter your monthly food budget($): ", min_value=0.0, format='%f')

    st.subheader("Miscellaneous Expenses")
    miscellaneous = st.number_input(
        "Enter your monthly miscellaneous expenses($): ", min_value=0.0, format='%f')

with colExpenses2:
    st.subheader("Monthly Transport")
    monthly_transport = st.number_input(
        "Enter your monthly transport fee($): ", min_value=0.0, format='%f')

    st.subheader("Monthly Utility Fees")
    monthly_utility = st.number_input(
        "Enter your monthly utility fees($): ", min_value=0.0, format='%f')

    st.subheader("Monthly Entertainment")
    monthly_entertainment = st.number_input(
        "Enter your monthly entertainment expenses($): ", min_value=0.0, format='%f')

monthly_expenses = monthly_rental + monthly_food + miscellaneous + \
    monthly_transport + monthly_utility + monthly_entertainment
monthly_savings = monthly_takehome_salary - monthly_expenses

# Savings
st.header("**Savings**")
st.subheader("Monthly Take Home Salary: $" +
             str(round(monthly_takehome_salary, 2)))
st.subheader("Monthly Expenses: $"+str(round(monthly_expenses, 2)))
st.subheader("Monthly Savings: $"+str(round(monthly_savings, 2)))

# Inflation and salary growth
st.markdown("---")

st.header("**Forecast Savings**")
colForecast1, colForecast2 = st.columns(2)
with colForecast1:
    st.subheader("Forecast Year")
    forecast_year = st.number_input(
        "Enter your desired year (min 1 year): ", min_value=0, format="%d")
    forecast_months = 12 * forecast_year

    # import inflation data for canada and calculate avergae annual rate (for later)
    st.subheader("Average Annual Inflation Rate (1960-2021)")
    country_work = st.selectbox('Please pick your country of work', countries)
    st.write("You selected", country_work)
    index = countries.index[countries['Country Name'] == country_work]
    annual_inflation = round(
        float(inflation.iloc[index]['average inflation']), 2)
    st.write("The inflation rate of", country_work,
             "is", annual_inflation, "%.")
    monthly_inflation = (1 + annual_inflation) ** (1/12) - 1
    cumulative_inflation_forecast = np.cumprod(
        np.repeat(1+monthly_inflation, forecast_months))
    forecast_expenses = monthly_expenses * cumulative_inflation_forecast

with colForecast2:
    st.subheader("Annual Salary Growth")
    your_industry = st.selectbox("Please pick your industry", industries)
    st.write("You selected", your_industry)
    index_industry = industries.index[industries['industries']
                                      == your_industry]
    annual_growth = round(float(growth.iloc[index_industry]['wage growth']), 2)
    st.write("the average wage growth for your industry is", annual_growth, "%.")
    monthly_growth = (1 + annual_growth) ** (1/12) - 1
    cumulative_salary_growth = np.cumprod(
        np.repeat(1+monthly_growth, forecast_months))
    forecast_salary = monthly_takehome_salary * cumulative_salary_growth

forecast_savings = forecast_salary - forecast_expenses
cumulative_savings = np.cumsum(forecast_savings)

# Create a plot to visualize salary,expenses & savings
x_values = np.arange(forecast_year+1)

fig = go.Figure()

# forecasted salary
fig.add_trace(
    go.Scatter(
        x=x_values,
        y=forecast_salary,
        name="Forecast Salary"
    )
)

# forecasted expenses
fig.add_trace(
    go.Scatter(
        x=x_values,
        y=forecast_expenses,
        name="Forecast Expenses"
    )
)

# Forecast Savings
fig.add_trace(
    go.Scatter(
        x=x_values,
        y=cumulative_savings,
        name="Forecast Savings"
    )
)

fig.update_layout(title="Forecast Salary, Expenses & Savings Over the Years",
                  xaxis_title='Year',
                  yaxis_title="Amount($)")

st.plotly_chart(fig, user_container_width=True)
