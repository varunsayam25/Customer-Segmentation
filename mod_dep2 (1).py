#!/usr/bin/env python
# coding: utf-8

# In[15]:


import json
import math
import pandas as pd
import pickle

import requests
import streamlit as st


# In[16]:


model = pickle.load(open('AC.pkl','rb'))


# In[28]:


st.title('Customer Segmentation Web App')


# In[29]:


st.sidebar.subheader('User Input')


# In[43]:


def User_Input():
    Income = st.number_input("Income",min_value=0,step=500,value=58138,help="Customer's yearly household income")
    #Recency = st.number_input("Complain",min_value=0,value=58,help="Number of days since customer's last purchase")
    NumWebVisitsMonth = st.number_input("Num of visits",min_value=0, value=7,help="Number of visits to company’s website in the last month")
    #Complain = st.number_input("Recency",min_value=0,value=7,help="1 if the customer complained in the last 2 years, 0 otherwise")
    customer_age = st.number_input("customer_age",min_value=0,value=64,help="Customer's age")
    total_purchases = st.number_input("total_purchases",min_value=0,value=25,help="Total number of purchases through website, catalogue, or store")
    #enrollment_years = st.number_input("enrollment_years", min_value=0 ,value=10,help="Number of years a client has enrolled with a company")
    family_size = st.number_input("family_size",min_value=0,value=1,help="Total number of members in a customer's family")
    data = {'Income':Income,'NumWebVisitsMonth':NumWebVisitsMonth,'customer_age':customer_age,
            'total_purchases':total_purchases,'family_size':family_size}
    features=pd.DataFrame(data,index=[0])
    return features
df= User_Input()

st.subheader('User_Input')
st.write(df)

predict = model.predict(df)

st.button("Get the cluster of this customer")
st.write(f"This customer belongs to the cluster {predict}")


# In[26]:





# In[ ]:





# In[ ]:




