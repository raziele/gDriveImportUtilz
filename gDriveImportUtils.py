import io
import numpy as np
import pandas as pd
from googleapiclient.http import MediaIoBaseDownload


def get_file_list_gdrive(google_folder_name, gdrive_service):
    # get file list under a google drive folder
    # input: folder name as string and goole drive handler
    # output: a dictionary with filename as key and fileID as value

    response = gdrive_service.files().list(q="".join(
        ["name contains ","'",google_folder_name,"'"])).execute()
    
    search_found_list = response.get('files', [])
    
    if(len(search_found_list) > 1):
       print("Error: multiple folders found")
       return 1
     
    folder_id = search_found_list[0].get('id')
    
    response = gdrive_service.files().list(
        q="".join(["'",folder_id,"' in parents"])).execute()
    
    flist = {}
    for file in response.get('files', []):
      flist[file.get('name')] = file.get('id')
      
    """   
      print 'Found folder: %s (%s)' % (file.get('name'), file.get('id'))
      folder_id = file.get('id')
    """
    return flist
  
def load_file_from_gdrive(fid, gdrive_service):
    # load a file from google drive by its fileID
    # input: fid as string, google drive service handler
    # returns a handler for the requested file
    
    request = gdrive_service.files().get_media(fileId=fid)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
      status, done = downloader.next_chunk()
      
    fh.seek(0)

    return fh
