from flask import Flask, render_template

import pandas as pd

import plotly.express as px

 

app = Flask(__name__)

# ['🇮🇷', '🇱🇾', '🇻🇪', '🇦🇴', '🇪🇬','']

# Example dataset with oil prices and country flags

data_frame = {

    'Country': ['Iran', 'Libya', 'Venezuela', 'Angola', 'Egypt','Romania'],

    'Oil Price (per liter)': [0.029, 0.030, 0.035, 0.328, 0.336,0.151],

    'Flag Emoji':['IR','LY','VE','AO','EG','RO']

}

 

df = pd.DataFrame(data_frame)

 

@app.route('/')

def index():

    # Create a Plotly bar chart for oil prices

    fig = px.bar(df, x='Country', y='Oil Price (per liter)', text='Oil Price (per liter)', title='Oil Prices per Liter by Country')

 

    # Convert Plotly figure to HTML div

    graph_html = fig.to_html(full_html=False)

 

    return render_template('index.html', graph_html=graph_html, countries=df.to_dict(orient='records'))

 

if __name__ == '__main__':

    app.run(debug=True)