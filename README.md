# Bitrix Form Automation with Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-brightgreen?logo=pandas)
![Status](https://img.shields.io/badge/status-active-success)

## Overview

This project automates the insertion of insurance claims data into the **Bitrix24 CRM system** using a simple, yet powerful Python script. Instead of manually filling out the same web form dozens of times, the script reads an Excel spreadsheet and automatically populates the required fields, saving hours of repetitive work and eliminating human error.

This script was built to solve a real business problem I faced as an insurance administrative assistant, where daily claim registrations were time-consuming and prone to mistakes.

## Key Features

- **Bulk Form Filling**: Reads a list of claims (sinistros) from an Excel file (`tabela.xlsx`) and inserts them one by one into Bitrix24.
- **Efficiency Gain**: Reduces a 2+ hour manual task to a 10‑second automated execution.
- **Error Reduction**: Avoids typos and inconsistent data entry that often occur with manual input.
- **Reusable & Configurable**: The script can be easily adapted to other forms or datasets by modifying column mappings.

## Tech Stack

| **Technology** | **Purpose** |
|----------------|-------------|
| 🐍 **Python 3** | Core programming language |
| 🐼 **Pandas** | Reading, cleaning, and transforming data from Excel |
| 🌐 **Selenium / Requests** *(if applicable)* | Automating browser interaction with the CRM |
| 📊 **Excel** | Source data (`.xlsx`) |

## How It Works

1. **Read Data**: The `sinistro.py` script reads `tabela.xlsx` using Pandas.
2. **Prepare Data**: `auxiliar.py` handles helper functions (cleaning, formatting, or mapping columns).
3. **Automate Input**: The main execution opens the Bitrix24 web form and iterates through each row, filling in the appropriate fields and submitting.
4. **Confirmation**: The script logs successful insertions and reports any failures for review.

## Project Structure
