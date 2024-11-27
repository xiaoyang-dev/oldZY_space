#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import time


# In[ ]:


#自定义CSS样式
st.markdown(
    """
    <style>
    .css-1l02zqu{
    margin:auto;
    width:50%
    }
    <style>
    """,unsafe_allow_html=True
)


# In[ ]:


def show_title():
    st.title("老张老杨的困间")


# In[ ]:


placeholder = st.empty()
password=placeholder.text_input("请输入密码",type="password")
if password!="":
    if password=="258069":
        placeholder.success("密码正确！")
        for seconds in range(5):
            placeholder.write(f"⏳ {5-seconds} s后将进入困间")
            time.sleep(1)
        placeholder.empty()
        show_title()
    else:
        placeholder.error("密码错误！")
        show=0;


# In[ ]:




