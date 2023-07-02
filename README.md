# LifeSync

LifeSync is a desktop application designed to simplify health management for users. The purpose of this project is to improve my programming skills.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Keys](#api-keys)
- [Features](#features)
- [Email Configuration](#email-configuration)
- [License](#license)
- [Contact](#contact)

## Installation

1. Clone the repository: `git clone <repository-url>`
2. Install the dependencies: `pip install -r requirements.txt`
3. Set up the necessary API keys (see [API Keys](#api-keys) section).
4. Run the project: `python main.py`

## Usage

Provide instructions on how to use the project, including any command-line arguments or user interface details. For example:

1. Launch the application by running `python main.py`.
2. Sign up or log in using the provided forms.
3. Explore the different functionalities of the application, such as reminders, nearest health center finder, and chatbot.

## API Keys

To use certain features of the project, you need to set up the required API keys. Follow these steps:

1. Obtain an API key from OpenAI and assign it to the `API_KEY1` variable in `config.py`.
2. Obtain an API key from Google Maps API and assign it to the `API_KEY2` variable in `config.py`.

## Features

1. User authentication: Users can sign up and log in to access the application's features.
2. Reminders: Users can manage their reminders, including adding, updating, listing, and deleting reminders.
3. Nearest Health Center Finder: Users can find the nearest hospital and pharmacy based on their location.
4. Chatbot: Users can interact with a chatbot that provides health-related information and assistance.

## Email Configuration

To configure the email functionality in the application, follow these steps:

1. Open the `reminders_main.py` file in the `home_pg` folder.
2. Locate the `send_reminder_email` function.
3. In the function, find the email configuration section.
4. Set the `sender_email` variable to your email address.
5. Set the `sender_password` variable to your email password.
6. Update the SMTP server and port if necessary.

```python
# Email configuration
sender_email = 'your-email@example.com'  # Replace with your email
sender_password = 'your-password'  # Replace with your email password
smtp_server = 'smtp.gmail.com'
smtp_port = 587
```

## License

LifeSync is licensed under the MIT License. See the LICENSE file for more information.

## Contact

For any inquiries or support, please email us at lifesync@example.com.
