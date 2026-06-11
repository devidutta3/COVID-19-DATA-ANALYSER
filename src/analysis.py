from fetch_response import fetch_requets as fr
import pandas as pd

data=fr(url="https://disease.sh/v3/covid-19/countries")
print("-----"*40)
def create_csv():
    df=pd.DataFrame({
        "Country":[Country["country"]for Country in data],
        "Cases":[Cases["cases"]for Cases in data],
        "Deaths":[Deaths["deaths"]for Deaths in data],
        "ReCovered":[Recovered["recovered"]for Recovered in data]
    })
    print(df)
    df.to_csv(r"Data/covid_data.csv", index=False)
    print("✅ Csv Created At The Respective File Location")
create_csv()   
