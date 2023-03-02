from flask import Flask , render_template, request, session, redirect, url_for
import numpy as np
import pickle
from sklearn.ensemble import GradientBoostingClassifier
import pandas as pd
import joblib
from flask_mail import Mail, Message

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        email = request.form['email']
        name = request.form['name']
        session['email'] = email
        session['name'] = name

        return redirect(url_for('prediction'))
    return render_template("registration_form.html")

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if not session.get("email") is None and not session.get("name") is None:    
        if request.method == "POST":
            location = int(request.form['location'])
            no_customers = int(request.form['no_customers'])
            daily_sales = int(request.form['daily_sales'])
            rent_wages = int(request.form['rent_wages'])
            competition = int(request.form['competition'])
            freq_supply_pay = int(request.form['freq_supply_pay'])
            supply = int(request.form['supply'])
            rating_reviewportal = int(request.form['rating_reviewportal'])
            nature = int(request.form['nature'])
            size_shop = int(request.form['size_shop'])
            total_assets = int(request.form['total_assets'])
            Education = int(request.form['Education'])
            Credit = int(request.form['Credit'])
            Business_type = int(request.form['Business_type'])
            cases = int(request.form['cases'])
            total_workers = int(request.form['total_workers'])
            
            if location == 0:
                Location_0 = 1
                Location_1 = 0
                Location_2 = 0
                Location_3 = 0
                Location_4 = 0
                Location_5 = 0
            elif location == 1:
                Location_0 = 0
                Location_1 = 1
                Location_2 = 0
                Location_3 = 0
                Location_4 = 0
                Location_5 = 0
            elif location == 2:
                Location_0 = 0
                Location_1 = 0
                Location_2 = 1
                Location_3 = 0
                Location_4 = 0
                Location_5 = 0
            elif location == 3:
                Location_0 = 0
                Location_1 = 0
                Location_2 = 0
                Location_3 = 1
                Location_4 = 0
                Location_5 = 0
            elif location == 4:
                Location_0 = 0
                Location_1 = 0
                Location_2 = 0
                Location_3 = 0
                Location_4 = 1
                Location_5 = 0
            elif location == 5:
                Location_0 = 0
                Location_1 = 0
                Location_2 = 0
                Location_3 = 0
                Location_4 = 0
                Location_5 = 1

            if no_customers == 0:
                No_customers_0 = 1
                No_customers_1 = 0
                No_customers_2 = 0
                No_customers_3 = 0
                No_customers_4 = 0
                No_customers_5 = 0
            elif no_customers == 1:
                No_customers_0 = 0
                No_customers_1 = 1
                No_customers_2 = 0
                No_customers_3 = 0
                No_customers_4 = 0
                No_customers_5 = 0
            elif no_customers == 2:
                No_customers_0 = 0
                No_customers_1 = 0
                No_customers_2 = 1
                No_customers_3 = 0
                No_customers_4 = 0
                No_customers_5 = 0
            elif no_customers == 3:
                No_customers_0 = 0
                No_customers_1 = 0
                No_customers_2 = 0
                No_customers_3 = 1
                No_customers_4 = 0
                No_customers_5 = 0
            elif no_customers == 4:
                No_customers_0 = 0
                No_customers_1 = 0
                No_customers_2 = 0
                No_customers_3 = 0
                No_customers_4 = 1
                No_customers_5 = 0
            elif no_customers == 5:
                No_customers_0 = 0
                No_customers_1 = 0
                No_customers_2 = 0
                No_customers_3 = 0
                No_customers_4 = 0
                No_customers_5 = 1
            
            if daily_sales == 0:
                Daily_Sales_0 = 1
                Daily_Sales_1 = 0
                Daily_Sales_2 = 0
                Daily_Sales_3 = 0
                Daily_Sales_4 = 0
                Daily_Sales_5 = 0
            elif daily_sales == 1:
                Daily_Sales_0 = 0
                Daily_Sales_1 = 1
                Daily_Sales_2 = 0
                Daily_Sales_3 = 0
                Daily_Sales_4 = 0
                Daily_Sales_5 = 0
            elif daily_sales == 2:
                Daily_Sales_0 = 0
                Daily_Sales_1 = 0
                Daily_Sales_2 = 1
                Daily_Sales_3 = 0
                Daily_Sales_4 = 0
                Daily_Sales_5 = 0
            elif daily_sales == 3:
                Daily_Sales_0 = 0
                Daily_Sales_1 = 0
                Daily_Sales_2 = 0
                Daily_Sales_3 = 1
                Daily_Sales_4 = 0
                Daily_Sales_5 = 0
            elif daily_sales == 4:
                Daily_Sales_0 = 0
                Daily_Sales_1 = 0
                Daily_Sales_2 = 0
                Daily_Sales_3 = 0
                Daily_Sales_4 = 1
                Daily_Sales_5 = 0
            elif daily_sales == 5:
                Daily_Sales_0 = 0
                Daily_Sales_1 = 0
                Daily_Sales_2 = 0
                Daily_Sales_3 = 0
                Daily_Sales_4 = 0
                Daily_Sales_5 = 1

            if rent_wages == 0:
                Rent_Wages_0 = 1
                Rent_Wages_1 = 0
                Rent_Wages_2 = 0
                Rent_Wages_3 = 0
                Rent_Wages_4 = 0
                Rent_Wages_5 = 0
            elif rent_wages == 1:
                Rent_Wages_0 = 0
                Rent_Wages_1 = 1
                Rent_Wages_2 = 0
                Rent_Wages_3 = 0
                Rent_Wages_4 = 0
                Rent_Wages_5 = 0
            elif rent_wages == 2:
                Rent_Wages_0 = 0
                Rent_Wages_1 = 0
                Rent_Wages_2 = 1
                Rent_Wages_3 = 0
                Rent_Wages_4 = 0
                Rent_Wages_5 = 0
            elif rent_wages == 3:
                Rent_Wages_0 = 0
                Rent_Wages_1 = 0
                Rent_Wages_2 = 0
                Rent_Wages_3 = 1
                Rent_Wages_4 = 0
                Rent_Wages_5 = 0
            elif rent_wages == 4:
                Rent_Wages_0 = 0
                Rent_Wages_1 = 0
                Rent_Wages_2 = 0
                Rent_Wages_3 = 0
                Rent_Wages_4 = 1
                Rent_Wages_5 = 0
            elif rent_wages == 5:
                Rent_Wages_0 = 0
                Rent_Wages_1 = 0
                Rent_Wages_2 = 0
                Rent_Wages_3 = 0
                Rent_Wages_4 = 0
                Rent_Wages_5 = 1

            if competition == 0:
                Competition_0 = 1
                Competition_1 = 0
                Competition_2 = 0
                Competition_3 = 0
                Competition_4 = 0
                Competition_5 = 0
            elif competition == 1:
                Competition_0 = 0
                Competition_1 = 1
                Competition_2 = 0
                Competition_3 = 0
                Competition_4 = 0
                Competition_5 = 0
            elif competition == 2:
                Competition_0 = 0
                Competition_1 = 0
                Competition_2 = 1
                Competition_3 = 0
                Competition_4 = 0
                Competition_5 = 0
            elif competition == 3:
                Competition_0 = 0
                Competition_1 = 0
                Competition_2 = 0
                Competition_3 = 1
                Competition_4 = 0
                Competition_5 = 0
            elif competition == 4:
                Competition_0 = 0
                Competition_1 = 0
                Competition_2 = 0
                Competition_3 = 0
                Competition_4 = 1
                Competition_5 = 0
            elif competition == 5:
                Competition_0 = 0
                Competition_1 = 0
                Competition_2 = 0
                Competition_3 = 0
                Competition_4 = 0
                Competition_5 = 1
            
            if freq_supply_pay == 0:
                Freq_Supply_pay_0 = 1
                Freq_Supply_pay_1 = 0
                Freq_Supply_pay_2 = 0
                Freq_Supply_pay_3 = 0
                Freq_Supply_pay_4 = 0
                Freq_Supply_pay_5 = 0
            elif freq_supply_pay == 1:
                Freq_Supply_pay_0 = 0
                Freq_Supply_pay_1 = 1
                Freq_Supply_pay_2 = 0
                Freq_Supply_pay_3 = 0
                Freq_Supply_pay_4 = 0
                Freq_Supply_pay_5 = 0
            elif freq_supply_pay == 2:
                Freq_Supply_pay_0 = 0
                Freq_Supply_pay_1 = 0
                Freq_Supply_pay_2 = 1
                Freq_Supply_pay_3 = 0
                Freq_Supply_pay_4 = 0
                Freq_Supply_pay_5 = 0
            elif freq_supply_pay == 3:
                Freq_Supply_pay_0 = 0
                Freq_Supply_pay_1 = 0
                Freq_Supply_pay_2 = 0
                Freq_Supply_pay_3 = 1
                Freq_Supply_pay_4 = 0
                Freq_Supply_pay_5 = 0
            elif freq_supply_pay == 4:
                Freq_Supply_pay_0 = 0
                Freq_Supply_pay_1 = 0
                Freq_Supply_pay_2 = 0
                Freq_Supply_pay_3 = 0
                Freq_Supply_pay_4 = 1
                Freq_Supply_pay_5 = 0
            elif freq_supply_pay == 5:
                Freq_Supply_pay_0 = 0
                Freq_Supply_pay_1 = 0
                Freq_Supply_pay_2 = 0
                Freq_Supply_pay_3 = 0
                Freq_Supply_pay_4 = 0
                Freq_Supply_pay_5 = 1

            if supply == 0:
                Supply_0 = 1
                Supply_1 = 0
                Supply_2 = 0
                Supply_3 = 0
                Supply_4 = 0
                Supply_5 = 0
            elif supply == 1:
                Supply_0 = 0
                Supply_1 = 1
                Supply_2 = 0
                Supply_3 = 0
                Supply_4 = 0
                Supply_5 = 0
            elif supply == 2:
                Supply_0 = 0
                Supply_1 = 0
                Supply_2 = 1
                Supply_3 = 0
                Supply_4 = 0
                Supply_5 = 0
            elif supply == 3:
                Supply_0 = 0
                Supply_1 = 0
                Supply_2 = 0
                Supply_3 = 1
                Supply_4 = 0
                Supply_5 = 0
            elif supply == 4:
                Supply_0 = 0
                Supply_1 = 0
                Supply_2 = 0
                Supply_3 = 0
                Supply_4 = 1
                Supply_5 = 0
            elif supply == 5:
                Supply_0 = 0
                Supply_1 = 0
                Supply_2 = 0
                Supply_3 = 0
                Supply_4 = 0
                Supply_5 = 1

            if rating_reviewportal == 0:
                Rating_Reviewportal_0 = 1
                Rating_Reviewportal_1 = 0
                Rating_Reviewportal_2 = 0
                Rating_Reviewportal_3 = 0
                Rating_Reviewportal_4 = 0
                Rating_Reviewportal_5 = 0
            elif rating_reviewportal == 1:
                Rating_Reviewportal_0 = 0
                Rating_Reviewportal_1 = 1
                Rating_Reviewportal_2 = 0
                Rating_Reviewportal_3 = 0
                Rating_Reviewportal_4 = 0
                Rating_Reviewportal_5 = 0
            elif rating_reviewportal == 2:
                Rating_Reviewportal_0 = 0
                Rating_Reviewportal_1 = 0
                Rating_Reviewportal_2 = 1
                Rating_Reviewportal_3 = 0
                Rating_Reviewportal_4 = 0
                Rating_Reviewportal_5 = 0
            elif rating_reviewportal == 3:
                Rating_Reviewportal_0 = 0
                Rating_Reviewportal_1 = 0
                Rating_Reviewportal_2 = 0
                Rating_Reviewportal_3 = 1
                Rating_Reviewportal_4 = 0
                Rating_Reviewportal_5 = 0
            elif rating_reviewportal == 4:
                Rating_Reviewportal_0 = 0
                Rating_Reviewportal_1 = 0
                Rating_Reviewportal_2 = 0
                Rating_Reviewportal_3 = 0
                Rating_Reviewportal_4 = 1
                Rating_Reviewportal_5 = 0
            elif rating_reviewportal == 5:
                Rating_Reviewportal_0 = 0
                Rating_Reviewportal_1 = 0
                Rating_Reviewportal_2 = 0
                Rating_Reviewportal_3 = 0
                Rating_Reviewportal_4 = 0
                Rating_Reviewportal_5 = 1

            if nature == 0:
                Nature_0 = 1
                Nature_1 = 0
                Nature_2 = 0
                Nature_3 = 0
                Nature_4 = 0
                Nature_5 = 0
            elif nature == 1:
                Nature_0 = 0
                Nature_1 = 1
                Nature_2 = 0
                Nature_3 = 0
                Nature_4 = 0
                Nature_5 = 0
            elif nature == 2:
                Nature_0 = 0
                Nature_1 = 0
                Nature_2 = 1
                Nature_3 = 0
                Nature_4 = 0
                Nature_5 = 0
            elif nature == 3:
                Nature_0 = 0
                Nature_1 = 0
                Nature_2 = 0
                Nature_3 = 1
                Nature_4 = 0
                Nature_5 = 0
            elif nature == 4:
                Nature_0 = 0
                Nature_1 = 0
                Nature_2 = 0
                Nature_3 = 0
                Nature_4 = 1
                Nature_5 = 0
            elif nature == 5:
                Nature_0 = 0
                Nature_1 = 0
                Nature_2 = 0
                Nature_3 = 0
                Nature_4 = 0
                Nature_5 = 1

            if size_shop == 0:
                Size_Shop_0 = 1
                Size_Shop_1 = 0
                Size_Shop_2 = 0
                Size_Shop_3 = 0
                Size_Shop_4 = 0
                Size_Shop_5 = 0
            elif size_shop == 1:
                Size_Shop_0 = 0
                Size_Shop_1 = 1
                Size_Shop_2 = 0
                Size_Shop_3 = 0
                Size_Shop_4 = 0
                Size_Shop_5 = 0
            elif size_shop == 2:
                Size_Shop_0 = 0
                Size_Shop_1 = 0
                Size_Shop_2 = 1
                Size_Shop_3 = 0
                Size_Shop_4 = 0
                Size_Shop_5 = 0
            elif size_shop == 3:
                Size_Shop_0 = 0
                Size_Shop_1 = 0
                Size_Shop_2 = 0
                Size_Shop_3 = 1
                Size_Shop_4 = 0
                Size_Shop_5 = 0
            elif size_shop == 4:
                Size_Shop_0 = 0
                Size_Shop_1 = 0
                Size_Shop_2 = 0
                Size_Shop_3 = 0
                Size_Shop_4 = 1
                Size_Shop_5 = 0
            elif size_shop == 5:
                Size_Shop_0 = 0
                Size_Shop_1 = 0
                Size_Shop_2 = 0
                Size_Shop_3 = 0
                Size_Shop_4 = 0
                Size_Shop_5 = 1

            if total_assets == 0:
                Total_Assets_0 = 1
                Total_Assets_1 = 0
                Total_Assets_2 = 0
                Total_Assets_3 = 0
                Total_Assets_4 = 0
                Total_Assets_5 = 0
            elif total_assets == 1:
                Total_Assets_0 = 0
                Total_Assets_1 = 1
                Total_Assets_2 = 0
                Total_Assets_3 = 0
                Total_Assets_4 = 0
                Total_Assets_5 = 0
            elif total_assets == 2:
                Total_Assets_0 = 0
                Total_Assets_1 = 0
                Total_Assets_2 = 1
                Total_Assets_3 = 0
                Total_Assets_4 = 0
                Total_Assets_5 = 0
            elif total_assets == 3:
                Total_Assets_0 = 0
                Total_Assets_1 = 0
                Total_Assets_2 = 0
                Total_Assets_3 = 1
                Total_Assets_4 = 0
                Total_Assets_5 = 0
            elif total_assets == 4:
                Total_Assets_0 = 0
                Total_Assets_1 = 0
                Total_Assets_2 = 0
                Total_Assets_3 = 0
                Total_Assets_4 = 1
                Total_Assets_5 = 0
            elif total_assets == 5:
                Total_Assets_0 = 0
                Total_Assets_1 = 0
                Total_Assets_2 = 0
                Total_Assets_3 = 0
                Total_Assets_4 = 0
                Total_Assets_5 = 1
            
            if Education == "Graduate":
                Graduate = 1
                Non_Graduate = 0
            else:
                Graduate = 0
                Non_Graduate = 1

            if Credit == "Yes":
                No = 0
                Yes = 1
            else:
                No = 1
                Yes = 0

            if Business_type == "Yes":
                No = 0
                Yes = 1
            else:
                No = 1
                Yes = 0

            if cases == 0:
                Cases_0 = 1
                Cases_1 = 0
                Cases_2 = 0
                Cases_3 = 0
                Cases_4 = 0
            elif cases == 1:
                Cases_0 = 0
                Cases_1 = 1
                Cases_2 = 0
                Cases_3 = 0
                Cases_4 = 0
            elif cases == 2:
                Cases_0 = 0
                Cases_1 = 0
                Cases_2 = 1
                Cases_3 = 0
                Cases_4 = 0
            elif cases == 3:
                Cases_0 = 0
                Cases_1 = 0
                Cases_2 = 0
                Cases_3 = 1
                Cases_4 = 0
            elif cases == 4:
                Cases_0 = 0
                Cases_1 = 0
                Cases_2 = 0
                Cases_3 = 0
                Cases_4 = 1
            
            if total_workers == 0:
                Total_Workers_0 = 1
                Total_Workers_1 = 0
                Total_Workers_2 = 0
                Total_Workers_3 = 0
                Total_Workers_4 = 0
                Total_Workers_5 = 0
                Total_Workers_6 = 0
                Total_Workers_7 = 0
            elif total_workers == 1:
                Total_Workers_0 = 0
                Total_Workers_1 = 1
                Total_Workers_2 = 0
                Total_Workers_3 = 0
                Total_Workers_4 = 0
                Total_Workers_5 = 0
                Total_Workers_6 = 0
                Total_Workers_7 = 0
            elif total_workers == 2:
                Total_Workers_0 = 0
                Total_Workers_1 = 0
                Total_Workers_2 = 1
                Total_Workers_3 = 0
                Total_Workers_4 = 0
                Total_Workers_5 = 0
                Total_Workers_6 = 0
                Total_Workers_7 = 0
            elif total_workers == 3:
                Total_Workers_0 = 0
                Total_Workers_1 = 0
                Total_Workers_2 = 0
                Total_Workers_3 = 1
                Total_Workers_4 = 0
                Total_Workers_5 = 0
                Total_Workers_6 = 0
                Total_Workers_7 = 0
            elif total_workers == 4:
                Total_Workers_0 = 0
                Total_Workers_1 = 0
                Total_Workers_2 = 0
                Total_Workers_3 = 0
                Total_Workers_4 = 1
                Total_Workers_5 = 0
                Total_Workers_6 = 0
                Total_Workers_7 = 0
            elif total_workers == 5:
                Total_Workers_0 = 0
                Total_Workers_1 = 0
                Total_Workers_2 = 0
                Total_Workers_3 = 0
                Total_Workers_4 = 0
                Total_Workers_5 = 1
                Total_Workers_6 = 0
                Total_Workers_7 = 0
            elif total_workers == 6:
                Total_Workers_0 = 0
                Total_Workers_1 = 0
                Total_Workers_2 = 0
                Total_Workers_3 = 0
                Total_Workers_4 = 0
                Total_Workers_5 = 0
                Total_Workers_6 = 1
                Total_Workers_7 = 0
            elif total_workers == 7:
                Total_Workers_0 = 0
                Total_Workers_1 = 0
                Total_Workers_2 = 0
                Total_Workers_3 = 0
                Total_Workers_4 = 0
                Total_Workers_5 = 0
                Total_Workers_6 = 0
                Total_Workers_7 = 1

            Loan_Amount = int(request.form['Loan_Amount'])

            Loan_Term =int(request.form['Loan_Term'])

            Applicant_Income = int(request.form['Applicant_Income'])

            Family_Income = int(request.form['Family_Income'])

            predInput = [[location, no_customers, daily_sales, rent_wages, competition, freq_supply_pay, supply, rating_reviewportal, nature, size_shop, total_assets, Education, Credit, Business_type, cases, total_workers, Loan_Amount, Loan_Term, Applicant_Income, Family_Income]]
            p = pd.DataFrame(predInput, columns= ['Cases', 'Education', 'Total_assets', 'Business_type', 'Credit', 'Rating_Reviewportal', 'Daily_Sales', 'Competition', 'Rent_Wages', 'Size_Shop', 'Location', 'Supply', 'Total_Workers', 'No_customers', 'Freq_Supply_pay', 'Nature', 'Applicant_Income_Log', 'Loan_Amount_Log', 'Loan_Amount_Term_Log', 'Total_Income_Log'])
            o = model.predict(p)
           
            # if o <= 0.5:
            #     output = "You are not qualify for loan"
            #     color = "red"
            #     return render_template( 'Thankyou.html', output=output,color=color)
            # elif o >= 0.5:
            #     output = "Congratulations!! You qualify for the loan"
            #     color = "green"
            msg = Message('Credit Scorer', sender = 'prithviraj.mutalik2019@gmail.com', recipients = [str(session['email'])])
            if o[0] >= 0.5 or o[0] <= -0.5:
                msg.body = "Hello "+session['name']+",\n"+"You are qualify for the loan and your score is "+str(o[0])
            else:
                msg.body = "Hello "+session['name']+",\n"+"Sorry!! Your are not qualify for loan "
            mail.send(msg)
            session.pop('email')
            session.pop('name')
            return render_template( 'Thankyou.html')
    else:
       return redirect(url_for('home')) 
    return render_template("TVS Form.html")

if __name__ == '__main__':
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'xxxxxxxxxxxxxxxxxxxx'
    app.config['MAIL_PASSWORD'] = 'xxxxxxxxxx'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.secret_key = "super secret key"
    mail = Mail(app)
    app.run(debug=True)