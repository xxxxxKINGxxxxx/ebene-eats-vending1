# CampusVend

A Django-powered campus vending machine system, built for Polytechnics Ebene Campus. It simulates the full snack-machine experience — browsing products, inserting money, and completing a purchase — through an interactive Bootstrap 5 interface backed by a Django project structure.

## Overview

CampusVend renders a vending machine UI with three product categories (savory snacks, sweet treats, and drinks), each item tagged with a code, price, and live stock count. Users select an item by clicking its card or typing its code, insert money in fixed denominations or a custom amount, and confirm the purchase once their balance covers the price. The interface tracks balance, stock levels, and low-stock/out-of-stock states in real time.

The project currently runs on client-side JavaScript for the purchase flow, with the Django backend providing the app scaffolding (`EbeneEats` and `vending` apps) that the persistence layer will build on next.

## Features

- Categorized product grid (snacks, sweet treats, drinks) with images, prices, and stock indicators
- Item selection by click or product code
- Denomination-based and custom money insertion
- Purchase validation (sufficient balance, in-stock check) with change calculation
- Low-stock and out-of-stock visual states
- Responsive Bootstrap 5 layout with a retro vending-machine console look

## Tech Stack

- **Backend:** Django 5.2 (Python)
- **Database:** SQLite (development)
- **Frontend:** Bootstrap 5, vanilla JavaScript, Font Awesome
- **Apps:** `EbeneEats` (main view/routing), `vending` (planned models for products, stock, and transactions)

## Project Structure

```
project1/
├── EbeneEats/          # Main app — serves the vending machine page
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── vending/             # Scaffolded app for product/inventory models (in progress)
│   ├── models.py
│   ├── views.py
│   └── templates/vending/firstproject.html   # Vending machine UI
├── project1/            # Project settings and root URL config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── manage.py
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/<your-username>/campusvend.git
cd campusvend/project1
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run the development server

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the vending machine.

## Roadmap

- [ ] Define `Product`, `Category`, and `Transaction` models in the `vending` app
- [ ] Move product data from the template into the database
- [ ] Wire purchase logic to Django views/APIs instead of client-side-only state
- [ ] Add Django admin support for managing inventory
- [ ] Add persistent transaction history
- [ ] Write tests for stock and balance logic

## License

Not yet specified. Add a `LICENSE` file (MIT recommended for open-source use) before publishing.

## Author

Built for Polytechnics Ebene Campus.
