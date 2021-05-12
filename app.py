from flask import Flask, request, render_template
from cowin_api import CoWinAPI

app = Flask(__name__)
cowin = CoWinAPI()


@app.route('/', methods=['GET', 'POST'])
def index():
    date = "2021-05-06"
    new_date = ""
    age = int(18)
    pincode = '400051'
    if request.method == 'POST':
        pincode = request.form.get('pincode')
        date = request.form.get('date')
        age = request.form.get('select_age')
        new_date = date[8:10]+'-'+date[5:7]+'-'+date[0:4]
        date = new_date
        if(age == "-1"):
            hw = cowin.get_availability_by_pincode(pincode, date)
        else:
            hw = cowin.get_availability_by_pincode(pincode, date, (int)(age))
        if(len(hw['centers']) >= 1):
            return render_template("index.html", hw=hw.values(), date=date, pincode=pincode, age=age)
        else:
            return render_template("else.html", date=date, pincode=pincode, age=age)
    return render_template("home.html")


if __name__ == "__main__":
    app.run()
