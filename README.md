# Flight Deals Tracker

This Python project is designed to track flight deals. It uses various APIs to retrieve flight information, updates destinations with IATA codes, checks for the cheapest available flights, and sends notifications for price drops.

## Features

- Retrieves and updates destination data with IATA codes.
- Finds the cheapest flights for specified destinations.
- Notifies users about flight deals.

## Getting Started

### Dependencies

- Python 3.x
- Requests library
- Twilio API for notifications
- dotenv for environment variable management
- Access to APIs

### Setting up the environment

- Clone the repository.
- Install required Python packages:

  ```bash
  pip install requests python-dotenv

### Executing the Program

Run `main.py` to start the flight deals tracking:

```bash
python main.py
```

The program will automatically update destination data, search for flight deals, and send notifications if cheaper flights are found.

### Modules

- `data_manager.py`: Manages data storage and retrieval.
- `flight_data.py`: Handles flight-related information retrieval.
- `notification_manager.py`: Responsible for sending out notifications.
- `flight_search.py`: Searches for flight data using external APIs.

### Authors

Momin Alvi

### Acknowledgments

Thanks to the creators of the APIs used in this project.  
