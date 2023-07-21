import os
import io
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
from PIL import Image
import pandas as pd
import time

#スクレイピングlist
d_price = ["21万円","25万円"]
arr1 = np.array([["渋谷アインス 4階/410","Court Hills 広尾南 2階"], ["21万円","25万円"]])
temp_output = pd.DataFrame(data=arr1)

#家賃
min_prrice = 21
max_prrice = 25

st.session_state.flag = "a"
# st.session_state.name = "b"

##本文
st.write("Leader’s saloon")  
clm1, clm2 = st.columns([1, 2.2])


###############################################################
with clm1:
    st.title("賃料予測システム")

         
###############################################################
with clm2:
    if st.session_state.flag != 0:
        st.session_state.flag = 0
        st.markdown("## Input")
        input_option_locate = st.selectbox("希望の場所（東京都内）",
                            (" ","渋谷区","台東区"))
        input_option_size = st.text_input('部屋の広さ(mm^2)', '')
        input_option_station = st.text_input('最寄り駅', '')

        if input_option_locate and input_option_size and input_option_station and st.session_state.flag == 0:
            st.session_state.flag += 1
            input_do = st.button('実行')

            if input_do and st.session_state.flag == 1:
                st.session_state.flag += 1
                st.markdown("## Output")
                st.write(f'**条件表示**： {input_option_locate} & {input_option_size}mm^2 & {input_option_station}')
                st.write(f'**予想賃料**： ***{min_prrice}***万円 〜 ***{max_prrice}***万円')
                st.dataframe(temp_output)

                st.session_state.name = st.text_input('保存名', '')
                input_hozn_bottom = st.button('保存')
                # if input_option_hozn and st.session_state.flag == 2:
                #      = input_option_hozn

                # else:
                #     st.write("保存名を入力してください")



