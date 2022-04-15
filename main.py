import pandas as pd
import streamlit as st


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True


if check_password():
    @st.cache
    def load_df_1():
        url = 'https://atelier-bi.s3.fr-par.scw.cloud/data17.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=SCWY39734VMW2CNBCY66%2F20220412%2Ffr-par%2Fs3%2Faws4_request&X-Amz-Date=20220412T155300Z&X-Amz-Expires=284869&X-Amz-Signature=c76d87ebcd3391c647b0c3d150d5016015fa867d4598541d6f82dd028ebee3f7&X-Amz-SignedHeaders=host'
        data = pd.read_csv(url, delimiter=';')
        return data

    @st.cache
    def load_df_2():
        url = 'https://atelier-bi.s3.fr-par.scw.cloud/data17b.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=SCWP7GYN9AJAV91N9YEF%2F20220412%2Ffr-par%2Fs3%2Faws4_request&X-Amz-Date=20220412T155349Z&X-Amz-Expires=284813&X-Amz-Signature=7905abcd1e31c788bfc38efe824835a52ceaa60a0ca82276148b1364ff37c177&X-Amz-SignedHeaders=host'
        data = pd.read_csv(url, delimiter=';')
        return data

    df1 = load_df_1()
    df2 = load_df_2()

    st.write("""
    # Atelier visualisation des données
    """)

    st.write("""
    ## Affichage des headers des dataframes
    """)

    st.write("""
    ### DF1
    """)
    st.dataframe(df1)
    input1 = st.multiselect('Select a column in df1', df1.columns)

    st.write("""
    ### DF2
    """)
    st.dataframe(df2)
    input2 = st.multiselect('Select a column in df2', df2.columns)
