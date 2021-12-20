
import streamlit as st
from mysql_userinfo import get_connection
from mysql.connector.errors import Error

def run_delete_app() :
    st.subheader('데이터 삭제')
    id = st.number_input('삭제할 아이디 입력', min_value=1)
    if st.button('삭제') :
        try :
            connection = get_connection()
            query = '''delete from test_user where id = %s;'''
            record = (id, )
            cursor = connection.cursor()
            cursor.execute(query, id)
            connection.commit()
        except Error as e :
            print('Error', e)
        finally :
            cursor.close()
            if connection.is_connected() :
                connection.close()
                print('MYSQL connection is closed')
                st.write('삭제가 완료되었습니다.')

