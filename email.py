"""
See README.md
"""

import msal
import requests

# Azure AD and Microsoft Graph API config
client_id = ''  # application ID 
client_secret = ''  # application Secret
tenant_id = ''  # directory ID (tenant)
user_email = ""  # Change email for corresponding user

authority = f"https://login.microsoftonline.com/{tenant_id}"
scopes = ["https://graph.microsoft.com/.default"]
graph_endpoint = f'https://graph.microsoft.com/v1.0/users/{user_email}/messages'

# Autenticación con MSAL
def get_token():
    app = msal.ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret
    )
    result = app.acquire_token_silent(scopes, account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=scopes)
    
    if "access_token" in result:
        return result["access_token"]
    else:
        print("Error obtaining token:", result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))  # Esto ayuda a la depuración
        return None

# Leer correos electrónicos
def read_email():
    token = get_token()
    if not token:
        return
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(graph_endpoint, headers=headers)
    if response.status_code == 200:
        emails = response.json().get('value', [])
        for email in emails:
            print("Subject:", email.get("subject"))
            print("From:", email.get("from", {}).get("emailAddress", {}).get("address"))
            # print("Body:", email.get("bodyPreview"))
            print("="*50)
    else:
        print("Error reading emails:", response.status_code, response.text)

if __name__ == "__main__":
    read_email()
    