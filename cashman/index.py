from flask import Flask, jsonify, request, render_template
from model.expense import Expense, ExpenseSchema
from model.income import Income, IncomeSchema
from model.transaction_type import TransactionType
import datetime, os
app = Flask(__name__)

transactions = [
	Income('Salary', 5000),
	Income('Dividends', 200),
	Expense('pizza', 50),
	Expense('Rock Concert', 100)
]

date = datetime.datetime.today().strftime('%A, %B %-d')

@app.route('/')
def index():
	return render_template('index.html', Today = date, Balance = get_incomes().json)

@app.route('/incomes')
def get_incomes():
	schema = IncomeSchema(many=True)
	incomes = schema.dump(
		#Filters all transactions for only INCOME types
		filter(lambda t: t.type == TransactionType.INCOME, transactions)
	)
	return jsonify(incomes.data)


@app.route('/incomes/<int:income_idx>')
def get_income(income_idx):
	"""Gets a specific income by index."""
	schema = IncomeSchema(many=True)
	incomes = schema.dump(
		#Filters all transactions for only INCOME types
		filter(lambda t: t.type == TransactionType.INCOME, transactions)
	)
	return jsonify(incomes.data[income_idx])


@app.route('/incomes', methods=['POST'])
def add_income():
	income = IncomeSchema().load(request.get_json())
	transactions.append(income.data)
	return "", 204


	
@app.route('/expenses')
def get_expenses():
	schema = ExpenseSchema(many=True)
	expenses = schema.dump(
		#Filters all transactions for only EXPENSE types
		filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
	)
	return jsonify(expenses.data)


	
@app.route('/expenses', methods=['POST'])
def add_expense():
	expense = ExpenseSchema().load(request.get_json())
	transactions.append(expense.data)
	return "", 204


	
if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)