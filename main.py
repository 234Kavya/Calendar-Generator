from flask import Flask,render_template , request
import calendar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendar',methods=['POST'])
def generate_calendar():
    month  = int(request.form['month'])
    year = int(request.form['year'])

    cal = calendar.HTMLCalendar()
    html_calendar = cal.formatmonth(year,month)

    return render_template('calendar.html' , calendar=html_calendar)


if __name__ == '__main__':
    app.run(debug=True)