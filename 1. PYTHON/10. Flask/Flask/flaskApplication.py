from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('getresult.html')

@app.route("/getresult", methods=['POST', 'GET'])
def getresult():
    if request.method == 'POST':
        try:
            # Get marks from form
            maths = float(request.form.get('maths', 0))
            data_science = float(request.form.get('data_science', 0))
            coa = float(request.form.get('coa', 0))
            microprocessors = float(request.form.get('microprocessors', 0))
            ml = float(request.form.get('ml', 0))
            
            # Calculate average
            total = maths + data_science + coa + microprocessors + ml
            average = total / 5
            
            # Store individual marks in a dictionary
            subject_marks = {
                'maths': maths,
                'data_science': data_science,
                'coa': coa,
                'microprocessors': microprocessors,
                'ml': ml,
                'total': total,
                'average': average
            }
            
            # Route to success or fail based on average
            if average >= 40:
                return render_template('success.html', results=average, subjects=subject_marks)
            else:
                return render_template('fail.html', results=average, subjects=subject_marks)
                
        except Exception as e:
            return f"Error: {str(e)}", 400
    
    return redirect(url_for('index'))

@app.route("/Success/<int:score>")
def Success(score):
    return render_template('success.html', results=score)

@app.route("/Fail/<int:score>")
def Fail(score):
    return render_template('fail.html', results=score)

if __name__ == '__main__':
    app.run(debug=True)