# OTP Verification via Email using Python

This Python script allows you to send a one-time password (OTP) to a specified email address for verification using the **SMTP** protocol. It utilizes **smtplib** for sending emails and **random** for OTP generation.

## Features
- Generates a random 4-digit OTP.
- Sends OTP via Gmail's SMTP server.
- Verifies the OTP entered by the user.
- Ensures secure email transmission with TLS encryption.

## Prerequisites
- Python 3 installed on your system.
- A Gmail account with **Less Secure Apps access enabled** or an **App Password** for authentication.
- Required Python libraries installed:
  ```sh
  pip install smtplib email
  ```

## How to Use
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. Open the script and replace `your-email@gmail.com` and `your-app-password` in `server.login()`.
3. Run the script:
   ```sh
   python otp_verification.py
   ```
4. Enter the recipient's email address when prompted.
5. Check the recipient's email for the OTP and enter it back into the terminal.
6. If the OTP matches, verification is successful.

## Code Explanation
- The script generates a **random 4-digit OTP**.
- It creates an **email message** using the `email.mime` module.
- It connects to **Gmail's SMTP server** using TLS encryption.
- The email with the OTP is sent to the recipient.
- The user enters the OTP received via email, and the script validates it.

## Security Considerations
- Do not hardcode your email password. Use **App Passwords** instead of your main password.
- Consider using environment variables to store sensitive information.
- Use **OAuth2 authentication** for better security instead of Less Secure Apps.

## License
This project is licensed under the MIT License.

## Disclaimer
This script is for educational purposes only. Sending automated emails must comply with **email service provider policies**.



