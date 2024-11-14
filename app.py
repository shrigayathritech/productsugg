from flask import Flask, render_template, request
from suggestion import filter_data, load_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    suggestions = []
    if request.method == 'POST':
        age = request.form.get('age')
        income = request.form.get('income')
        student = request.form.get('student')
        credit_rating = request.form.get('credit_rating')
        
        user_attributes = {
            'Age': age,
            'Income': income,
            'Student': student,
            'Credit_Rating': credit_rating
        }
        
        try:
            data = load_data('purchase_history.csv')
            print("Loaded Data:\n", data)  # Debugging line
            suggestions = filter_data(data, user_attributes)
            print("Filtered Suggestions:\n", suggestions)  # Debugging line
        except Exception as e:
            suggestions = [str(e)]
    
    return render_template('index.html', suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)
