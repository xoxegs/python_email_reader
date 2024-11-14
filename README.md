# Python reader

Application to read emails from an Office 365 account

To use this application, it is necessary to register the application in Azure AD (now Microsoft Entra).

To register the application, follow these steps:

- Go to https://portal.azure.com
- Click on "Azure Active Directory" in the left menu
- Click on "App registrations"
- Configure the application name and select the type of account you want to allow.
- Once the application is created, note the Application (client) ID and the Directory (tenant) ID.
- Go to "Certificates & secrets" and generate a new Client Secret. Save this value in a safe place.
- In "API permissions", add the Mail.Read permissions in "Microsoft Graph API" and grant admin consent.
- Once the permission is added, select "Grant admin consent for [Your organization]" so that the organization grants consent for that permission.
- Wait a few minutes for it to propagate.
- Configure the variables client_id, client_secret, tenant_id, user_email.

Install the dependencies with pip install -r requirements.txt.

