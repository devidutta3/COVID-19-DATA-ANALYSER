import requests as r

def fetch_requets(url):
    response=r.get(url)


    if response.status_code==200:
        data=response.json()
        return data
    else:
        return "Data Not found"
    
url="https://disease.sh/v3/covid-19/countries"

result=fetch_requets(url)
print(result)