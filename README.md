# Storefront

A Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)
- virtualenv

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/patug/storefront.git
   cd storefront
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install dependencies:
`pip install -r requirements.txt`
`python manage.py migrate`


Run the development server:
`python manage.py runserver`


Open your web browser and navigate to  `http://127.0.0.1:8000/`.
