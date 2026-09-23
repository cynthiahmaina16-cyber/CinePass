# Movie Ticket Price Calculator

An interactive, command-line Python application designed to evaluate user eligibility and dynamically calculate the final cost of a movie ticket based on age, scheduling, and seating tiers.

## Features

- **Automated Eligibility Checks**: Verifies general entry age restrictions and exclusive age requirements for evening screenings.
- **Dynamic Surcharges**: Automatically applies weekend and evening peak-hour pricing rules.
- **Tiered Service Fees**: Evaluates and modifies service charges based on seat preferences (`Premium`, `Gold`, or `Standard`).
- **Membership Incentives**: Grants special baseline price discounts for qualifying accounts.

## Dynamic Pricing Rules

| Factor | Tier / Condition | Price Impact |
| :--- | :--- | :--- |
| **Base Price** | Flat rate | \$15.00 |
| **Seat Surcharge** | Premium | +\$5.00 |
| | Gold | +\$3.00 |
| | Standard (or other) | +\$1.00 |
| **Peak Surcharge** | Weekend or Evening show | +\$2.00 |
| **Member Discount**| Active member AND age ≥ 21 | -\$3.00 |

## Requirements

- Python 3.x Installed
   ```
4. Follow the interactive prompts in the terminal window to input your ticket configuration.
