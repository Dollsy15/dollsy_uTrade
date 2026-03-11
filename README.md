# In-Memory Order Book Engine

## Overview

This project implements an in-memory limit order book for a single instrument.  
The engine processes buy and sell orders and matches them in real-time using price-time priority.

The system supports:

- LIMIT orders
- MARKET orders
- Order cancellation

Unmatched orders remain in the book until filled or cancelled.

This project was developed as part of the uTrade Solutions Campus Hiring 2026 Mini Project Assignment.

---

## Features

- Supports BUY and SELL limit orders
- Supports MARKET orders (price = 0)
- Matches orders using price-time priority
- Handles partial order fills
- Supports order cancellation
- Prevents self-trading
- Prints the final order book state (top 5 bid and ask levels)

---

## Input Format

Orders are read from standard input.

Order format:

ORDER_ID SIDE PRICE QUANTITY

Example:

O1 BUY 100.50 10

Where:

ORDER_ID → unique identifier  
SIDE → BUY or SELL  
PRICE → order price (0 means MARKET order)  
QUANTITY → number of shares

Cancel order format:

CANCEL ORDER_ID

Example:

CANCEL O2

---

## Output Format

Each executed trade is printed as:

TRADE BUY_ORDER SELL_ORDER PRICE QUANTITY

Example:

TRADE O1 O3 100.50 8

After processing all orders, the final order book is printed.

Example:

--- Book ---
ASK: 99.00 x 18
BID: (empty)

---

## Sample Input

O1 BUY 100.50 10  
O2 BUY 100.50 5  
O3 SELL 100.50 8  
O4 SELL 99.00 20  
CANCEL O2

---

## Sample Output

TRADE O1 O3 100.50 8  
TRADE O1 O4 99.00 2

--- Book ---
ASK: 99.00 x 18  
BID: (empty)

---

## Design Decisions

The order book maintains two sides:

Bids (Buy Orders)

- Stored by price
- Sorted in descending order
- FIFO queue at each price level for time priority

Asks (Sell Orders)

- Stored by price
- Sorted in ascending order
- FIFO queue at each price level

This ensures correct price-time priority matching.

---

## Matching Logic

When a new order arrives:

1. Check the opposite side of the book
2. If prices cross, start matching
3. Execute trades based on price-time priority
4. If quantity remains, add the order to the book
5. Market orders match until filled or no liquidity exists

---

## Edge Cases Handled

- Partial fills
- Market orders with no liquidity
- Order cancellation
- Empty order book

---

## Project Structure

dollsy_uTrade  
│  
├── src  
│ └── main.py  
│  
├── README.md  
├── requirements.txt  
└── .gitignore

---

## Limitations

- Supports only a single instrument
- Data is stored in memory only
- No advanced order types like IOC or FOK

---

## Author

Dollsy Rani
Submitted for uTrade Solutions Campus Hiring 2026 Mini Project Assignment
