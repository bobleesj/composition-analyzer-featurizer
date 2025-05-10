import pandas as pd


def get_processed_oliynyk_df():
    # Creates an dataframe NewElem that contains the values from Oliynyk_Element_Properties_Dataset
    oliynyk_df = pd.read_excel(
        "data/element_properties_for_ML.xlsx"
    )  # , engine='openpyxl')
    oliynyk_df = oliynyk_df.reset_index()  # Reset the indexes
    oliynyk_df.columns = oliynyk_df.columns.str.replace("[\n]", "")
    oliynyk_df.index = oliynyk_df.index + 1
    oliynyk_df = oliynyk_df.fillna(0)
    return oliynyk_df
