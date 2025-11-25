from flask import Flask,render_template,request

app=Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        weight = request.form.get("weight")
        height = request.form.get("height")
    
        weight = float(weight)
        height = float(height)

        #converting cm into m
        height = height/100

        # calculation body mass 
        BMI = weight/(height*height)

        #upto 2 decimals rounded off
        BMI = round(BMI,2)

        if BMI > 0:
            if BMI <= 16:
                return render_template('result.html', pred = f"Your Body Mass Index is {BMI}.You are severly under weight",BMI=BMI)
            elif BMI <= 18.5:
                return render_template('result.html', pred = f"Your Body Mass Index is {BMI}.You are under weight",BMI=BMI)
            elif BMI <= 25:
                return render_template('result.html', pred = f"Your Body Mass Index is {BMI}.You are Healthy",BMI=BMI)
            elif BMI <= 30:
                return render_template('result.html', pred = f"Your Body Mass Index is {BMI}.You are over weight",BMI=BMI)
            else:
                return render_template('result.html', pred = f"Your Body Mass Index is {BMI}.You are severly over weight",BMI=BMI)
            
        else:
            return render_template('result.html', pred="Please Enter Correct Detailes")
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)