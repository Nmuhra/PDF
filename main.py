import os 
import requests

urls = str(input("pdf URL: "))
output = ".\Outputs"

for url in urls:
  response = requests.get(url)
  if response.status_code == 200:
    file_path = os.path.join(output, os.path.name(url))
    with open(file_path, "wb") as A:
      A.write(response.content)
