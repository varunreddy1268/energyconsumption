
# Energy Consumption Forecasting

Energy Consumption Forecasting is a powerful time series forecasting tool designed to predict household electric power consumption every minute. This project employs advanced machine learning models and a user-friendly Flask web application for visualization and interaction.

## Features

- Time series forecasting with high-frequency data (every 1 minute).
- Flask web application for easy interaction and visualization.
- Custom model building and preprocessing modules for data handling and prediction.
- Utilizes PyTorch and TensorFlow for deep learning models.

## Installation

Before you can run the project, you'll need to have Python installed on your system. This project was built using Python 3.8, but it should be compatible with other versions. To install the required libraries, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Install the required packages using pip:

```bash
pip install -r requirements.txt

Usage
To start the Flask application, run the following command from the root directory of the project:

python app.py

Navigate to http://localhost:3001 in your web browser. You'll be presented with a user interface where you can upload your data and see the energy consumption forecasting in action.

Uploading Data
The Flask app allows you to upload a CSV file with your energy consumption data. Ensure your data is in the correct format as expected by the application (refer to the pre_processing module for guidance).
