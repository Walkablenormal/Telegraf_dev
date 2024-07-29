# Cisco Catalyst Center Telegraf Integration

This project provides Telegraf configuration and scripts to fetch data from Cisco Catalyst Center API endpoints. It allows you to collect metrics and insights from your Cisco Catalyst Center environment and integrate them with your monitoring and analytics tools.

## Table of Contents

- [Cisco Catalyst Center Telegraf Integration](#cisco-catalyst-center-telegraf-integration)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Available Scripts](#available-scripts)
  - [Contributing](#contributing)
  - [License](#license)

## Prerequisites

- Telegraf 1.31.2 or higher
- Python 3.12.3 or higher
- Access to Cisco Catalyst Center API endpoints

## Installation

1. Clone this repository:
    ```git clone https://github.com/Walkablenormal/cisco-catalyst-center-telegraf.git```
    ```cd cisco-catalyst-center-telegraf```
2. Install required Python packages:
   ```pip install -r requirements.txt```
3. Copy the Telegraf configuration file to your Telegraf config directory:
   ```cp * /etc/telegraf/telegraf.d/```

## Configuration

1. Open the `config.json` file and update the following parameters:

- `catalyst_center_url`: URL of your Cisco Catalyst Center instance
- `username`: Your Catalyst Center API username
- `password`: Your Catalyst Center API password

## Usage

1. Start Telegraf with the new configuration:
```systemctl restart telegraf```
2. Verify that data is being collected by checking your configured output destination (e.g., InfluxDB, Prometheus, etc.).

## Available Scripts

currently, the project includes the following scripts to fetch data from various Cisco Catalyst Center API endpoints:


To run a script manually:

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the LGPL License.
