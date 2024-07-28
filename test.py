import requests 
import pandas as pd

api_url = "https://jsonplaceholder.typicode.com/todos/1" 



response = requests.get(api_url)

test =response.json()


print(response.status_code)
print (test)
df= pd.DataFrame([test], columns=['userId','id','title','completed'])
print(df)
df.to_csv('data.csv')