from flask import Flask,render_template,request
import requests
import json

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather=dict({
                'city':'',
                'icon':'N/A',
                'temp':'N/A',
                'temp_min':'N/A',
                'temp_max':'N/A',
                'descrip':'',
                'message':''
                })
    con=True
    if request.method=="POST":
        city=request.form['city']

        try:
            weather_url=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=018e4898874da81767023d19f4851ffd&units=metric')
            weather_data=weather_url.json()
            if(len(weather_data)<3):
                weather={
                    'city':city,
                    'message':weather_data['message']
                    }
            else:
                weather={
                    'city':city,
                    'country':weather_data['sys']['country'],
                    'icon':"http://openweathermap.org/img/wn/"+weather_data['weather'][0]['icon']+".png",
                    'temp':weather_data['main']['temp'],
                    'pressure':weather_data['main']['pressure'],
                    'humidity':weather_data['main']['humidity'],
                    'wind_speed':weather_data['wind']['speed'],
                    'descrip':weather_data['weather'][0]['description']
                }
        except:
            con=False
    if(con):        
        return render_template('index.html',weather=weather)
    else:
        return render_template('error.html')

if __name__=='__main__':
    app.run()