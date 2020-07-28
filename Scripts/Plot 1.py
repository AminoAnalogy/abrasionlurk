# Get this figure: fig = py.get_figure("https://plotly.com/~pawel_sobala/1/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~pawel_sobala/1/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Plot 1", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plotly.com/~pawel_sobala/1/").get_data()[0]["y"]

# Get figure documentation: https://plotly.com/python/get-requests/
# Add data documentation: https://plotly.com/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plotly.com/python/getting-started
# Find your api_key here: https://plotly.com/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "type": "bar", 
  "x": ["Product<br>Revenue", "Services<br>Revenue", "Total<br>Revenue", "Fixed<br>Costs", "Variable<br>Costs", "Total<br>Costs", "Total"], 
  "y": [0, 430, 0, 570, 370, 370, 0], 
  "frame": None, 
  "xaxis": "x", 
  "yaxis": "y", 
  "marker": {
    "line": {"color": "transparent"}, 
    "color": "rgba(1,1,1, 0.0)", 
    "fillcolor": "rgba(31,119,180,1)"
  }
}
trace2 = {
  "type": "bar", 
  "x": ["Product<br>Revenue", "Services<br>Revenue", "Total<br>Revenue", "Fixed<br>Costs", "Variable<br>Costs", "Total<br>Costs", "Total"], 
  "y": [430, 260, 690, 0, 0, 0, 0], 
  "frame": None, 
  "xaxis": "x", 
  "yaxis": "y", 
  "marker": {
    "line": {
      "color": "rgba(55, 128, 191, 0.7)", 
      "width": 2
    }, 
    "color": "rgba(55, 128, 191, 0.7)", 
    "fillcolor": "rgba(255,127,14,1)"
  }
}
trace3 = {
  "type": "bar", 
  "x": ["Product<br>Revenue", "Services<br>Revenue", "Total<br>Revenue", "Fixed<br>Costs", "Variable<br>Costs", "Total<br>Costs", "Total"], 
  "y": [0, 0, 0, 120, 200, 320, 0], 
  "frame": None, 
  "xaxis": "x", 
  "yaxis": "y", 
  "marker": {
    "line": {
      "color": "rgba(219, 64, 82, 1.0)", 
      "width": 2
    }, 
    "color": "rgba(219, 64, 82, 0.7)", 
    "fillcolor": "rgba(44,160,44,1)"
  }
}
trace4 = {
  "type": "bar", 
  "x": ["Product<br>Revenue", "Services<br>Revenue", "Total<br>Revenue", "Fixed<br>Costs", "Variable<br>Costs", "Total<br>Costs", "Total"], 
  "y": [0, 0, 0, 0, 0, 0, 370], 
  "frame": None, 
  "xaxis": "x", 
  "yaxis": "y", 
  "marker": {
    "line": {
      "color": "rgba(50, 171, 96, 1.0)", 
      "width": 2
    }, 
    "color": "rgba(50, 171, 96, 0.7)", 
    "fillcolor": "rgba(214,39,40,1)"
  }
}
data = Data([trace1, trace2, trace3, trace4])
layout = {
  "title": {"text": "Annual Profit - 2015"}, 
  "xaxis": {
    "type": "category", 
    "range": [-0.5, 6.5], 
    "title": {"text": ""}, 
    "domain": [0, 1], 
    "autorange": True, 
    "categoryorder": "array", 
    "categoryarraysrc": "RPlotBot:3531:381dc1"
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [0, 726.3157894736842], 
    "title": {"text": ""}, 
    "domain": [0, 1], 
    "autorange": True
  }, 
  "margin": {
    "b": 40, 
    "l": 60, 
    "r": 10, 
    "t": 25
  }, 
  "barmode": "stack", 
  "hovermode": "closest", 
  "showlegend": False, 
  "annotations": [
    {
      "x": "Product<br>Revenue", 
      "y": 400, 
      "font": {
        "size": 14, 
        "color": "rgba(245, 246, 249, 1)", 
        "family": "Arial"
      }, 
      "text": "$430K", 
      "xref": "x", 
      "yref": "y", 
      "showarrow": False
    }, 
    {
      "x": "Services<br>Revenue", 
      "y": 660, 
      "font": {
        "size": 14, 
        "color": "rgba(245, 246, 249, 1)", 
        "family": "Arial"
      }, 
      "text": "$260K", 
      "xref": "x", 
      "yref": "y", 
      "showarrow": False
    }, 
    {
      "x": "Total<br>Revenue", 
      "y": 660, 
      "font": {
        "size": 14, 
        "color": "rgba(245, 246, 249, 1)", 
        "family": "Arial"
      }, 
      "text": "$690K", 
      "xref": "x", 
      "yref": "y", 
      "showarrow": False
    }, 
    {
      "x": "Fixed<br>Costs", 
      "y": 590, 
      "font": {
        "size": 14, 
        "color": "rgba(245, 246, 249, 1)", 
        "family": "Arial"
      }, 
      "text": "$-120K", 
      "xref": "x", 
      "yref": "y", 
      "showarrow": False
    }, 
    {
      "x": "Variable<br>Costs", 
      "y": 400, 
      "font": {
        "size": 14, 
        "color": "rgba(245, 246, 249, 1)", 
        "family": "Arial"
      }, 
      "text": "$-200K", 
      "xref": "x", 
      "yref": "y", 
      "showarrow": False
    }, 
    {
      "x": "Total<br>Costs", 
      "y": 400, 
      "font": {
        "size": 14, 
        "color": "rgba(245, 246, 249, 1)", 
        "family": "Arial"
      }, 
      "text": "$-320K", 
      "xref": "x", 
      "yref": "y", 
      "showarrow": False
    }, 
    {
      "x": "Total", 
      "y": 340, 
      "font": {
        "size": 14, 
        "color": "rgba(245, 246, 249, 1)", 
        "family": "Arial"
      }, 
      "text": "$370K", 
      "xref": "x", 
      "yref": "y", 
      "showarrow": False
    }
  ], 
  "plot_bgcolor": "rgba(245, 246, 249, 1)", 
  "paper_bgcolor": "rgba(245, 246, 249, 1)"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)