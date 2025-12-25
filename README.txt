SNMP Bandwidth Monitor
======================

A real-time SNMP bandwidth monitoring tool written in Python using asyncio and Rich.

This script was developed to meet CUSTOMER-SPECIFIC SECURITY REQUIREMENTS,
including a hardened default SNMP community configuration.

--------------------------------------------------

FEATURES
--------
- Async SNMP polling (pysnmp asyncio)
- Automatic interface discovery
- Interactive interface selection
- RX / TX throughput in Mbps
- Interface utilization percentage
- Live terminal UI (Rich)

--------------------------------------------------

SECURITY & CUSTOMER REQUIREMENTS
--------------------------------
- By default, the script uses a PREDEFINED HARDENED SNMP COMMUNITY
  as required by the customer environment.
- A special trigger input allows overriding the SNMP community
  ONLY WHEN EXPLICITLY REQUESTED by the customer.
- This behavior is intentional and documented to comply with
  customer security policies.

--------------------------------------------------

REQUIREMENTS
------------
- Python 3.9 or higher
- SNMP v2c enabled on target device
- Network access to UDP port 161

--------------------------------------------------

INSTALLATION
------------
pip install -r requirements.txt

--------------------------------------------------

USAGE
-----
python scripts/snmp_bandwidth_monitor.py

Runtime inputs:
- Target IP address or hostname
- Interface selection
- Optional SNMP community override (customer-defined trigger)

--------------------------------------------------

TECHNICAL NOTES
---------------
- Uses 32-bit SNMP counters
- Handles 32-bit counter overflow
- Designed for continuous CLI monitoring
- Tested on Windows using Git Bash

--------------------------------------------------

LICENSE
-------
MIT
