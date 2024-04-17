import streamlit as st
import pandas as pd

def main():
    # Set page layout to wide (full screen)
    st.set_page_config(layout="wide")

    file_path = r"C:\Users\lenovo\Downloads\FEES\B.Tech\3rd Year\Section - E.xlsx"
    df = load_data(file_path)
    if df is not None:
        # Filter dataframe to include only Section E
        df_section_e = df[df['Section'] == 'E']
        if not df_section_e.empty:
            # Convert dataframe to HTML table and render it using markdown
            st.markdown(get_table_html(df_section_e), unsafe_allow_html=True)
        else:
            st.write("No data available for Section E.")
    else:
        st.write("No data to display.")

def get_table_html(df):
    # Convert DataFrame to HTML table string
    table_html = df.to_html(index=False, escape=False, classes=["dataframe"])

    # Modify HTML string to set table width to 100% and center align text
    table_html = table_html.replace('<table', '<table style="width:100%; text-align:center;"')

    return table_html

def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        st.error(f"An error occurred while loading the data: {e}")
        return None

if __name__ == "__main__":
    main()
