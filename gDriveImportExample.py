from googleapiclient.discovery import build
from google.colab import auth
import pandas as pd

folder_name = "YOUR GOOGLE DRIVE FOLDER NAME HERE"

# initialize drive service. May require authentication
auth.authenticate_user() # this will open an authentication request. 
                         # Once approve, the user gets a token to be provided in the box displayed

service = build('drive', 'v3')

list_of_files = get_file_list_gdrive(folder_name, service)

file = load_file_from_gdrive(list_of_files["NAME OF REQUESTED FILE"], service)

df = pd.read_table(file, sep = ";", header = None, index_col = 0) #exact arguments depend on you file's structure!
df.head()
