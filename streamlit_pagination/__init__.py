import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _pagination_component = components.declare_component(
        "pagination_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _pagination_component = components.declare_component("pagination_component", path=build_dir)

def pagination_component(dataLength, layout, key=None):
    
    component_value = _pagination_component(dataLength=dataLength, layout=layout, key=key, default=0)

    return component_value


# if not _RELEASE:
#     import streamlit as st
#     import pandas as pd
#     import numpy as np
#     from streamlit_pagination import pagination_component

#     st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

#     if 'foo' not in st.session_state:
#         st.session_state['foo'] = 0 

#     data = pd.DataFrame(np.random.randint(0,100,size=(1000, 4)), columns=list('ABCD')) 
    
#     n = 100  
#     list_df = [data[i:i+n] for i in range(0,data.shape[0],n)] 

#     data_l = list_df[st.session_state['foo']] 

#     st.dataframe(data_l, width=300, height=700)

#     layout = {  'color':"primary", 
#                 'style':{'margin-top':'10px'}}
#     test = pagination_component(len(list_df), layout=layout, key="foo")
