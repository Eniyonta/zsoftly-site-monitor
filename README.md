# ZSoftly Website Health Monitor

A simple command-line tool that checks whether a list of websites are reachable and healthy.

## Requirements

- Python 3.8+
- `requests` library

## Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/Eniyonta/zsoftly-site-monitor.git
cd zsoftly-site-monitor

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate      
venv\Scripts\activate         

# 3. Install dependencies
pip install requests
```

## How to Run

```bash
python monitor.py
```

## Example Output
```txt
=== WEBSITE HEALTH REPORT ===

Name: client-a-site
URL: https://example.com
Status: HEALTHY
HTTP Status / Error: 200
Response Time: 102.12 ms
--------------------------------------------------
```

---
