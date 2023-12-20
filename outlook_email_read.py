import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")

# Access the default inbox folder
inbox = namespace.GetDefaultFolder(6)  # 6 corresponds to the inbox folder
latest_email = None
latest_received_time = None

# Iterate through emails in the inbox and find the latest received email
for email in inbox.Items:
    received_time = email.ReceivedTime
    if latest_received_time is None or received_time > latest_received_time:
        latest_received_time = received_time
        latest_email = email

# Display information about the latest email
if latest_email:
    print("Subject:", latest_email.Subject)
    print("Received Date:", latest_email.ReceivedTime)
    print("Sender:", latest_email.SenderName)
    print("Body:", latest_email.Body)
else:
    print("No emails found in the inbox.")

# target_subject = "Build success in Jenkins: sv-securityhub365-ng-ui - #286"
#
# # Iterate through emails in the inbox and find the email with the specified subject
# target_email = None
#
# for email in inbox.Items:
#     if email.Subject == target_subject:
#         target_email = email
#         break  # Exit the loop once the target email is found
#
# # Display information about the target email
# if target_email:
#     print("Subject:", target_email.Subject)
#     print("Received Date:", target_email.ReceivedTime)
#     print("Sender:", target_email.SenderName)
#     print("Body:", target_email.Body)
# else:
#     print(f"No email with subject '{target_subject}' found in the inbox.")



# Iterate through emails in the inbox
# for email in inbox.Items:
#     print("Subject:", email.Subject)
#     print("Received Date:", email.ReceivedTime)
#     print("Sender:", email.SenderName)
#     print("Body:", email.Body)
#     print("\n---\n")