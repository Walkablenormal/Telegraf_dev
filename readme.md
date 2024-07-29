# Cisco Catalyst Center Telegraf Integration

This project provides Telegraf configuration and scripts to fetch data from Cisco Catalyst Center API endpoints. It allows you to collect metrics and insights from your Cisco Catalyst Center environment and integrate them with your monitoring and analytics tools.

Currently, this project is WIP 🚧

## Table of Contents

- [Cisco Catalyst Center Telegraf Integration](#cisco-catalyst-center-telegraf-integration)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Supported routes](#routes)
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

1. Open the `config.py` file and update the following parameters:

- `BASE_URL`: URL of your Cisco Catalyst Center instance (string)
- `USERNAME`: Your Catalyst Center API username (string)
- `PASSWORD`: Your Catalyst Center API password (string)
- `SSL_VERIFY`: True if the certificate your Catalyst Center deployent uses is singed by a trusted CA. (bool)

Currently, this file contains the credentials of the Cisco DevNet Always-On Catalyst Center Sandbox.

## Usage

1. Start Telegraf with the new configuration:

```systemctl restart telegraf```

2. Verify that data is being collected by checking your configured output destination (e.g., InfluxDB, Prometheus, etc.).

## Routes

| Route       | Python file     | Telegraf config |
| ----- | ----------- | --------------- |
|[/dna/intent/api/v1/network-device/](https://developer.cisco.com/docs/dna-center/get-device-list/)|catalyst_center_network_device.py|catalyst_center_network_device.conf|
|[/dna/intent/api/v1/client-health](https://developer.cisco.com/docs/dna-center/get-overall-client-health/)|catalyst_center_overall_client_health.py|catalyst_center_overall_client_health.conf|
|[/dna/intent/api/v1/network-health](https://developer.cisco.com/docs/dna-center/get-overall-network-health/)|catalyst_center_overall_network_health.py|catalyst_center_overall_network_health.conf|
|[/dna/intent/api/v1/site-health](https://developer.cisco.com/docs/dna-center/get-site-health/)|catalyst_center_site_health.py|catalyst_center_site_health.conf|


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the LGPL License.
