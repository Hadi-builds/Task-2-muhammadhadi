# Real-Time CLI Expense Tracker

A state-preserving Python backend script designed to continuously record, validate, and accumulate expenses via a terminal interface.

---

## 📌 Project Overview
Developed as part of the **DecodeLabs Industrial Training Program (Project 2: The Architecture of Financial Truth)**. The project implements the **IPO (Input-Process-Output)** model to handle real-time streaming data with proper state persistence and input error-proofing.

---

## ⚙️ Core Architecture & Features

* **Continuous Audit Loop:** Runs a continuous `while True` loop to accept consecutive financial entries until manually stopped.
* **State Preservation (Accumulator Pattern):** Initializes the accumulator variable (`total_spent = 0.0`) outside the loop to retain memory across every transaction cycle[cite: 1].
* **Defensive Input Safety (Poka-Yoke):** Wraps data conversion in a `try...except ValueError` block to catch invalid text entries (e.g., typing `"ten"`) without crashing the application[cite: 1].
* **Graceful Sentinel Shutdown:** Intercepts the `'quit'` command to safely break the execution loop and present the final ledger balance[cite: 1].

---

## 🚀 How to Run

### Prerequisites
* Python 3.8 or higher installed on your machine.
