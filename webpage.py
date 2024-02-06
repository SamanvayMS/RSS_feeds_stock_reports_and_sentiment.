from flask import Flask, render_template, request

app = Flask(__name__)

# Example dictionary of stocks
stocks = {
    "Apple Inc.": "AAPL",
    "Alphabet Inc.": "GOOGL",
    "Microsoft Corporation": "MSFT",
    # Add more stocks as needed
}

# Function to generate a stock report (placeholder)
def generate_stock_report(ticker):
    # Placeholder for your logic to generate a report based on the ticker
    return f"Report for {ticker}: This is a placeholder for the actual stock report."

@app.route('/', methods=['GET', 'POST'])
def index():
    report = ""
    if request.method == 'POST':
        ticker = request.form['stock']
        report = generate_stock_report(ticker)
    return render_template('index.html', stocks=stocks, report=report)

if __name__ == '__main__':
    app.run(debug=True)