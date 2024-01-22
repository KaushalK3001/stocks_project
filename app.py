from flask import Flask, render_template
from TAscore import calculate_TAscore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/technical_analysis_score/<stock>')
def technical_analysis_score(stock):
    # Call the function to calculate technical analysis score
    ta_score = calculate_TAscore(stock)
    
    # Pass the score to the template
    return render_template('technical_analysis_score.html', stock_name=stock, ta_score=ta_score)

if __name__ == '__main__':
    app.run(debug=True)
