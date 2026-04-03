# Finance Dashboard Backend

## Overview

This project implements a backend system for managing financial records with role-based access control and dashboard-level analytics.

The system supports user roles, financial record management, and aggregated insights such as totals and trends.

---

## How to Run the Application

1. Navigate to the project directory:

```
cd finance_dashboard
```

2. Run the application:

```
python main.py
```

3. The server will start at:

```
http://127.0.0.1:5000/
```

Opening this URL in a browser will confirm that the API is running.

---

## API Testing

Since the APIs require role-based headers, they should be tested using tools like PowerShell, Postman, or Thunder Client.

---

## Step 1: Create a Financial Record

Run the following command in PowerShell:

```
Invoke-RestMethod -Uri "http://127.0.0.1:5000/records" `
-Method POST `
-Headers @{role="admin"; "Content-Type"="application/json"} `
-Body '{"amount":5000,"type":"income","category":"salary"}'
```

Expected response:

```
Record created
```

---

## Step 2: Fetch Dashboard Summary

Run the following command:

```
Invoke-RestMethod -Uri "http://127.0.0.1:5000/summary" `
-Headers @{role="admin"} `
-Method GET
```

Example output:

```
total_income       : 5000.0
total_expense      : 0
net_balance        : 5000.0
category_breakdown : salary → 5000
recent_activity    : includes latest records
monthly_trends     : aggregated monthly data
weekly_trends      : aggregated weekly data
```

---

## Features

* Role-based access control (Admin, Analyst, Viewer)
* CRUD operations for financial records
* Filtering support for records
* Dashboard summary API with:

  * Total income and expenses
  * Net balance calculation
  * Category-wise aggregation
  * Recent transactions
  * Monthly and weekly trends

---

## Tech Stack

* Python
* Flask
* SQLite

---

## Notes

* SQLite is used for simplicity and can be replaced with a scalable database such as PostgreSQL.
* Role-based access is enforced using request headers.
* The summary endpoint demonstrates aggregation logic using SQL queries.
