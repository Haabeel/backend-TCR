# Savoury Search Backend Documentation

This documentation provides an overview of the backend of the TCR final project, Savoury Search.

## Project Overview

Savoury Search is a project developed using Django and Django Rest Framework (DRF) to create an API that communicates with the frontend. This API serves files and data, and it includes authentication using Django Rest Auth. The project primarily utilizes class-based views and proper permission classes for robust and secure functionality.

## Project Dependencies

To set up the backend of the Savoury Search project, you can download the required dependencies listed in the `requirements.txt` file. This file includes all the dependencies used in the backend part of the project.

### How to Install Dependencies

To install the project dependencies, follow these steps:

1. Clone the repository:

   ```shell
   git clone <repository_url>
   cd backend-TCR
   ```

2. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. Install the project dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

4. You're all set to run the backend of the Savoury Search project!

## Project Components

The backend of the Savoury Search project consists of the following key components:

1. **Django Rest Framework (DRF):** The primary framework used for creating the API, handling data, and serving files.

2. **Django Rest Auth:** Used for authentication to secure the API.

3. **Class-Based Views:** Class-based views are employed for various endpoints, enhancing code organization and reusability.

4. **Permission Classes:** Proper permission classes are used to control access and authorization within the API.
