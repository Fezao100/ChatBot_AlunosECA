#import os
#from oauth2client.service_account import ServiceAccountCredentials
#from googleapiclient.discovery import build

#SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#SAMPLE_SPREADSHEET_ID = '<1YXMD7Y5XaYgf-eBB7RegW3pubH1mZGUr8VuHB7-_kOA>'
#SAMPLE_RANGE_NAME = 'A1:B9'

#key_file_location = <C:\Users\Usuario\Desktop\meu bot\json>
#api_key = <AIzaSyCI8cDDlD6mqS1d0J77GJHweHhZkQiib2w>
#creds = ServiceAccountCredentials.from_json_keyfile_name(key_file_location, SCOPES)
#service = build('sheets', 'v4', credentials=creds, developerKey=api_key)

#sheet = service.spreadsheets()
#result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
#values = result.get('values', [])