
import streamlit as st
from mysql_userinfo import get_connection
from mysql.connector.errors import Error

def run_update_app() :
    st.subheader('나이를 업데이트')
    id = st.number_input('아이디 입력', min_value=1)
    age = st.number_input('업데이트할 나이 입력', min_value=1)

    if st.button('저장') :
        try :
            connection = get_connection()
            query = '''update test_user set age = %s where id = %s;'''
            record = (id, age)
            cursor = connection.cursor()
            cursor.execute(query, record)
            connection.commit()
        except Error as e :
            print('Error', e)
        finally :
            cursor.close()
            if connection.is_connected() :
                connection.close()
                print('MYSQL connection is closed')
                st.write('변경이 완료되었습니다.')

