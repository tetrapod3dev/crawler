import pandas as pd


def export_product_excel(products, filename, index=None, columns=None):
    df = pd.DataFrame(data=products, index=index, columns=columns)
    df.to_excel(filename)

