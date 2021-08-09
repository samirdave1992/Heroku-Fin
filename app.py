import streamlit as st
import numpy as np
from plotly import graph_objs as go
import pandas as pd


st.set_page_config(layout="wide")

st.title("Financial Calculator")

st.subheader("Salary")
#with st.form(key="Form1"):
Annual_Sal, Tax= st.beta_columns(2)
with Annual_Sal:
    salary=st.number_input("Enter your annual salary($)", min_value=0.0, format='%f')

with Tax:
    tax_pct=st.number_input("Enter the tax rate(%)",min_value=0.0,format='%f')

tax_pct=tax_pct/100.0
salary_post_tax=salary * (1-tax_pct)
monthly_takehome=salary_post_tax/12.0


st.subheader("Expenses")
Rental, Food, miscellaneous, utilities, Car=st.beta_columns(5)


with Rental:
    Living_expenses=st.number_input("monthly rental/mortgage", min_value=0.0,format='%f')

with Food:
    Food_expenses=st.number_input("Enter monthly Food/Groceries", min_value=0.0,format='%f')

with Car:
    Car_expenses=st.number_input("Enter monthly Car/Transport expenses", min_value=0.0,format='%f')

with utilities:
    Utility_expenses=st.number_input("Enter monthly Utilities", min_value=0.0,format='%f')

with miscellaneous:
    miscellaneous_expenses=st.number_input("Enter monthly miscellaneousexpenses", min_value=0.0,format='%f')

Monthly_expense= Living_expenses + Food_expenses + Car_expenses + Utility_expenses + miscellaneous_expenses

Monthly_savings= monthly_takehome - Monthly_expense




  #  submit=st.form_submit_button(label="Submit")

   # if submit:
st.subheader("Monthly salary after Tax: $" + str(round(monthly_takehome,2)))
st.subheader("Monthly expenses: $" + str(round(Monthly_expense,2)))
st.subheader("Monthly savings: $" + str(round(Monthly_savings,2)))

st.markdown('***')
st.header('Lets begin forecasting your savings')

forecast1,forecast2,forecast3=st.beta_columns(3)

with forecast1:
    st.subheader("Enter # of years you want to forecast")
    forecasted_years=st.number_input("enter min 1 year:",min_value=1, format='%d')
    forecast_months= 12*forecasted_years

with forecast2:
    st.subheader("Annual salary growth rate in %")
    annual_growth=st.number_input("Approx(5-10%)",min_value=0.0,format='%f')
    monthly_growth=(1+ annual_growth) ** (1/12)-1
    cumulative_salary_growth=np.cumprod(np.repeat(1+monthly_growth, forecast_months))
    forecast_salary=monthly_takehome * cumulative_salary_growth

with forecast3:
    st.subheader("Enter annual inflation rate(%)")
    Annual_inflation=st.number_input("Approx(2-2.5%)",min_value=0.0,format='%f')
    monthly_inflation=(1+Annual_inflation)**(1/12)-1
    cumulative_inflation_forecast=np.cumprod(np.repeat(1+ monthly_inflation, forecast_months))
    forecast_expenses=Monthly_expense*cumulative_inflation_forecast


forecast_savings=forecast_salary-forecast_expenses
cumulative_savings=np.cumsum(forecast_savings)

x_values=np.arange(forecasted_years+1)


st.write(type(x_values))
st.write(type(forecast_salary))
st.write(type(forecast_expenses))
