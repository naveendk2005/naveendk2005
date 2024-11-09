from flask import Flask,request, render_template
import pickle

app = Flask(__name__)

#with open('Maternal Health Risk Data Set.pkl', 'rb') as model_file:
model = pickle.load(open("Health Risk Data Set.pkl","rb"))

@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def predict():
    age = float(request.form['age'])
    SystolicBP = float(request.form['SystolicBP'])
    DiastolicBP = float(request.form['DiastolicBP'])
    BS = float(request.form['BS'])
    BodyTemp = float(request.form['BodyTemp'])
    HeartRate = float(request.form['HeartRate'])
    input_data = [[age,SystolicBP,DiastolicBP,BS,BodyTemp,HeartRate]]
    print(input_data)
    predict=model.predict(input_data)
    prediction=f"The predicted Risk is: {predict[0]:,.2f}"    
    return render_template('index.html', prediction_text='Predicted High Risk: {}'.format( prediction))
if __name__ == '__main__':  
    app.run(debug=True)  