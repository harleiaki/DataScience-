
import timeit
import pandas            as pd
import streamlit         as st
import seaborn           as sns
import matplotlib.pyplot as plt
from PIL                 import Image
from io                  import BytesIO



# Função para ler os dados
@st.cache(show_spinner= True, allow_output_mutation=True)
def load_data(file_data):
    try:
        return pd.read_csv(file_data, sep=';')
    except:
        return pd.read_excel(file_data)

@st.cache(allow_output_mutation=True)
def multiselect_filter(relatorio, col, selecionados):
    if 'all' in selecionados:
        return relatorio
    else:
        return relatorio[relatorio[col].isin(selecionados)].reset_index(drop=True)


@st.cache
def df_toString(df):
    return df.to_csv(index=False)
    # return df.to_csv(index=False).encode('utf-8')

@st.cache
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def main():
    st.set_page_config(page_title = 'Telemarketing analisys', \
        page_icon = '../img/telmarketing_icon.png',
        layout="wide",
        initial_sidebar_state='expanded'
    )
    st.write('# Telemarketing analisys')
    st.markdown("---")
    
    image = Image.open("../img/Bank-Branding.jpg")
    st.sidebar.image(image)
    
    
    start = timeit.default_timer()

    bank_raw = load_data('../data/input/bank-additional-full.csv')

    csv = df_toString(bank_raw)
    st.write(type(csv))
    st.write(csv[:100])

    st.write('### Download CSV')
    
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='df_csv.csv',
        mime='text/csv',
    )

    
    df_xlsx = to_excel(bank_raw)
    st.write(type(df_xlsx))
    st.write(df_xlsx[:100])

    
    st.write('### Download Excel')
    st.download_button(label='📥 Download data as EXCEL',
                        data=df_xlsx ,
                        file_name= 'df_excel.xlsx')



    st.write('Time: ', timeit.default_timer() - start)  

if __name__ == '__main__':
	main()
    









