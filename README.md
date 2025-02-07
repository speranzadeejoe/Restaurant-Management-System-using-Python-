# Restaurant-Management-System-using-Python-
# Restaurant Payment System

## Overview
The Restaurant Payment System is a GUI-based Python application built using Tkinter. It allows users to input the quantity of food items, calculates the total bill including tax and service charges, and displays the final amount payable. The system also generates a random order number for each transaction.

## Features
- User-friendly GUI with a clean layout
- Automatic order number generation
- Tax and service charge calculation
- Total bill computation
- Reset and exit functionality
- Integrated calculator using `calc_function`

## Requirements
Ensure you have the following dependencies installed before running the application:

- Python 3.x
- Tkinter (comes pre-installed with Python)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/restaurant-payment-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd restaurant-payment-system
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
1. Enter the quantity of each food item.
2. Click the **TOTAL** button to calculate the bill.
3. View the order number, itemized cost, tax, service charge, and total amount payable.
4. Use the **RESET** button to clear inputs.
5. Use the **EXIT** button to close the application.

## File Structure
```
restaurant-payment-system/
│── main.py            # Main application script
│── calc_function.py   # Calculator functionality (needs implementation)
│── README.md          # Project documentation
```

## Known Issues
- Some variable names are misspelled, such as `larggefries` instead of `largefries`.
- The `txtburger`, `txtcheeseburger`, and other text fields have incorrect `textvariable` assignments.

## Contribution
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

---

Feel free to modify the README as needed. Happy coding! 🚀

