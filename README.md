# Product Analytics Case

A portfolio project demonstrating product analytics using SQL, Python, and synthetic user activity data.

## Overview

This project analyzes user behavior and payment activity to evaluate product engagement, conversion, payment dynamics, and channel performance.

The analysis focuses on:

- Active Users
- Daily Active Users (DAU)
- Payment Users
- Conversion Rate
- Payment Volume
- Average Payment Amount
- Channel Performance
- Top Users
- User Activity Frequency
- Product Funnel

## Dataset

The project uses a synthetic dataset:

`user_activity.csv`

Main fields:

- `user_id`
- `date`
- `event_type`
- `channel`
- `amount`

Event types include:

- `login`
- `payment`

Channels include:

- `app`
- `web`

All data is synthetic and created specifically for portfolio demonstration purposes.

## SQL Analysis

The file `analysis.sql` contains SQL queries for:

- Total unique users
- Active users
- Daily Active Users (DAU)
- Payment users
- Conversion rate
- Total payment volume
- Average payment amount
- Activity by channel
- Payment volume by channel
- Top users by payment volume
- User activity frequency
- Daily payment dynamics

## Python Analysis

The file `product_analysis.py` performs the analysis programmatically using Pandas.

It calculates:

- Main KPIs
- DAU
- Daily payment dynamics
- Channel analytics
- Top users
- User activity frequency
- Product funnel

The script automatically exports the results to:

`product_analysis_results.xlsx`

## Key Findings

Based on the synthetic dataset:

- 9 users were active during the analyzed period.
- 7 users completed at least one payment.
- Conversion from active user to payment user was approximately 77.8%.
- 2 active users did not complete a payment.
- App users generated the majority of payment activity.
- Web users showed lower payment activity compared with app users.
- A relatively small group of users generated a large share of total payment volume.

These findings suggest opportunities to improve conversion among active non-paying users and further analyze differences between app and web behavior.

## Business Recommendations

Potential product actions based on the analysis:

- Investigate why active users do not complete payments.
- Analyze the payment funnel by channel.
- Improve payment conversion for web users.
- Identify high-value user segments.
- Monitor DAU and payment conversion over time.
- Add retention and cohort analysis for deeper product insights.

## Output

The generated Excel report includes:

- KPIs
- DAU
- Daily Payments
- Channel Activity
- Channel Payments
- Top Users
- User Activity
- Funnel

## Tech Stack

- SQL
- Python
- Pandas
- Excel
- OpenPyXL
- Product Analytics
- Payment Analytics

## Project Structure

- `user_activity.csv` — synthetic user activity dataset
- `analysis.sql` — SQL product analytics queries
- `product_analysis.py` — Python analytics pipeline
- `product_analysis_results.xlsx` — generated analysis results
- `requirements.txt` — Python dependencies
- `README.md` — project documentation

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python product_analysis.py
```

The script will generate:

```text
product_analysis_results.xlsx
```

## Skills Demonstrated

- Product analytics
- SQL analysis
- Python data analysis
- KPI calculation
- Conversion analysis
- User behavior analysis
- Funnel analysis
- Channel analysis
- Data aggregation
- Automated Excel reporting

## Data Privacy

All data in this repository is synthetic.

The project does not contain confidential, production, customer, or employer data.

## Future Improvements

- Retention analysis
- Cohort analysis
- WAU / MAU metrics
- DAU / MAU stickiness
- Funnel analysis with more product events
- User segmentation
- Churn analysis
- A/B test analysis
- Power BI dashboard
