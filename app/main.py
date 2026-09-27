from fastapi import Depends, FastAPI, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Expense
from app.db.session import get_db
from app.schemas import ExpenseCreate, ExpenseResponse


app = FastAPI(title="Personal Finance Tracker")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/expenses",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)) -> Expense:
    new_expense = Expense(**expense.model_dump())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@app.get("/expenses", response_model=list[ExpenseResponse])
def list_expenses(db: Session = Depends(get_db)) -> list[Expense]:
    statement = select(Expense).order_by(
        Expense.occurred_at.desc(), Expense.id.desc()
    )
    return list(db.scalars(statement).all())
