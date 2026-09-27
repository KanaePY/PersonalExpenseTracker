# Personal Expense Dashboard

A self-hosted expense tracker and analytics dashboard for logging personal spending, scheduling recurring expenses, and visualizing spending patterns with GitHub-style heatmaps.

## Overview

This project lets you manually log expenses across categories (travel, food, misc, clothes, etc.), schedule recurring expenses like daily commute fares, and view spending trends through stats and calendar heatmaps. It's built as a learning project and standalone app, with a longer-term plan to integrate it into a personal portfolio site alongside other personal web apps.

## Features

- **Manual expense logging** — record amount, category, date, time, and an optional note
- **Categories** — travel, food, misc, clothes, and other user-defined categories
- **Recurring/scheduled expenses** — set up templates (e.g. daily bus fare, Uber to university) that generate upcoming expense entries
  - Upcoming entries wait in a pending queue for confirmation or rejection
  - If left untouched past a configurable time window, they auto-confirm into real expenses
- **Stats dashboard** — totals and trends by category, week, and month
- **Heatmaps**
  - Transaction-count heatmap (GitHub-contributions style): how many transactions occurred per day
  - Spend-amount heatmap: which days had the highest total spend

## Tech Stack

| Layer     | Technology                     |
|-----------|---------------------------------|
| Frontend  | React                           |
| Backend   | FastAPI (Python)                |
| Database  | PostgreSQL                      |
| ORM       | SQLAlchemy                      |
| Migrations| Alembic                         |

## Data Model (planned)

- **`categories`** — `id`, `name`, `color`
- **`expenses`** — `id`, `amount`, `category_id`, `occurred_at`, `note`, `source` (`manual` / `recurring`)
- **`recurring_templates`** — `id`, `amount`, `category_id`, `label`, `schedule` (days of week + time), `confirmation_window_hours`, `active`
- **`pending_expenses`** — `id`, `recurring_template_id`, `scheduled_for`, `status` (`pending` / `confirmed` / `rejected`), `created_at`

## Project Status

🚧 **In active development.** Currently building out the FastAPI + PostgreSQL backend skeleton with core CRUD for categories and expenses.

### Roadmap

- [ ] FastAPI + PostgreSQL + Alembic project skeleton
- [ ] CRUD endpoints for categories and expenses
- [ ] Basic React frontend for manual expense logging
- [ ] Aggregation/stats endpoints (totals by category, week, month)
- [ ] Heatmap data endpoints (transaction count, spend amount)
- [ ] Heatmap frontend components
- [ ] Recurring expense templates
- [ ] Pending expense queue with confirm/reject + auto-confirm logic
- [ ] Integration into personal portfolio site (future)

## Scope

This is currently a **local-only, single-user application** — no authentication layer for now. Authentication will eventually be handled at the portfolio-website level, since this app (along with other personal projects) will only ever be accessed by its owner.

Bank/wallet integration (UBL, NayaPay, Google Wallet) is intentionally out of scope — expenses are entered manually with a date and time.

## Getting Started

_Setup instructions will be added once the backend skeleton is in place._

## License

Personal project — license TBD.