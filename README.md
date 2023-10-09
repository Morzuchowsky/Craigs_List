
# Craigs_List Mini Project

This project is a simple web application developed with Django. It is designed to allow users to list and view items for sale, inspired by platforms like Craigslist.

## Features

- **Home Page**: Showcases a welcoming message and a link to view all items.
- **Item List**: Displays all items available for sale.
- **Item Details**: Detailed information about a specific item can be viewed.
- **Add Item**: Functionality to add a new item to the list.
- **Edit Item**: Allows item details modification.
- **Delete Item**: Provides the option to remove an item from the list.
- **User Registration**: Page for new user sign-ups.

## Requirements

- **Django**: This project is built on the Django framework.
- **CrispyForms**: Used for enhancing form styling.
- **Pillow**: Implemented for image handling.
- **Mailjet Library**: Necessary for sending emails.
  - **Note**: An API key and Secret key for Mailjet are essential.

## Setup

1. Clone the repository.
2. Install the required packages using pip:
    ```
    pip install django crispy-forms pillow mailjet
    ```
3. Configure your Mailjet API and Secret keys.
4. Run migrations:
    ```
    python manage.py migrate
    ```
5. Start the Django development server:
    ```
    python manage.py runserver
    ```

Feedback and suggestions are always appreciated.

