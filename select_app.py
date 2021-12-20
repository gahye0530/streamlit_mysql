

import streamlit as st
from mysql.connector import errors
from mysql_userinfo import get_connection

def run_select_app() :
    st.subheader('데이터 조회')
   
    try :
         # 1. 전체 데이터 조회
        connection = get_connection()
        query = '''select * from test_user;'''
        cursor = connection.cursor(dictionary = True)
        cursor.execute(query)
        record_list = cursor.fetchall() 
        st.dataframe(record_list)
        # 2. 아이디를 입력하면 해당 아이디의 데이터만 조회
        st.subheader('아이디로 조회')
        id = st.number_input('아이디를 입력하세요.', min_value = 1)
        query = '''select id, email, age, address from test_user where id = %s'''
        record = (id, )
        cursor.execute(query, record)
        record_list = cursor.fetchall() 
        st.dataframe(record_list)
        # 3. 이메일 항목에서 검색하는 기능
        st.subheader('이메일 검색')
        search_word="%" + st.text_input('검색어입력') + "%"
        if st.button('검색하기!') :
            query = '''select id, email, age, address
                       from test_user
                       where email like %s'''
            record = (search_word, )
            cursor.execute(query, record)
            record_list = cursor.fetchall()
            st.dataframe(record_list)
    except errors as e :
        print('Error', e)
    finally :
        cursor.close()
        if connection.is_connected() :
            connection.close()
            print('MySQL connection is closed')
