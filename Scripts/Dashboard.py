import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests
import plotly.graph_objects as go
app = dash.Dash()


app.layout = html.Div([

  html.H1('Financial Dashboard'), 

   

  html.Div([
    dcc.Input(id='company_selection',value='AAPL'),
    html.H3(id='text'),
    dcc.Graph(id ='revenue'),
    dcc.Graph(id ='netincome'),
  ])
])
  
@app.callback(Output('revenue','figure'),
              [Input('company_selection','value')]
             )  
def retrieve_revenue(company):
  demo = '31fa1a9122c9b0d18024b5eb2d9ef148'
  stock = company
  IS = requests.get(f'https://financialmodelingprep.com/api/v3/financials/income-statement/{company}?apikey={demo}')
  IS = IS.json()
  IS = IS['financials']
  Revenues = []
  Dates = []
  count = 0
  for item in IS:
    Revenues.append(float(IS[count]['Net Income']))
    Dates.append(IS[count]['date'])
    count += 1
 
  datapoints = {'data': [go.Bar(x=Dates, y=Revenues,marker_color='lightsalmon',name='Net Income')],
  'layout': dict(xaxis={'title':'Date'},
                yaxis={'title':'Net Income'},
                  )} 
  return datapoints