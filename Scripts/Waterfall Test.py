# Get this figure: fig = py.get_figure("https://plotly.com/~HitchSlightly/2/")
# Get this figure's data: data = py.get_figure("https://plotly.com/~HitchSlightly/2/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="Waterfall Test", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plotly.com/~HitchSlightly/2/").get_data()[0]["y"]

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
  "meta": {"columnNames": {
      "x": "Trace 0, x; Trace 1, x; Trace 2, x; Trace 3, x", 
      "y": "Trace 0, y"
    }}, 
  "type": "bar", 
  "xsrc": "HitchSlightly:1:059fc8", 
  "x": ["Product<br>Revenue", "Services<br>Revenue", "Total<br>Revenue", "Fixed<br>Costs", "Variable<br>Costs", "Total<br>Costs", "Total"], 
  "ysrc": "HitchSlightly:1:b4ef48", 
  "y": [0, 430, 0, 570, 370, 370, 0], 
  "marker": {"color": "rgba(1,1,1, 0.0)"}
}
trace2 = {
  "meta": {"columnNames": {
      "x": "Trace 0, x; Trace 1, x; Trace 2, x; Trace 3, x", 
      "y": "Trace 1, y"
    }}, 
  "type": "bar", 
  "xsrc": "HitchSlightly:1:059fc8", 
  "x": ["Product<br>Revenue", "Services<br>Revenue", "Total<br>Revenue", "Fixed<br>Costs", "Variable<br>Costs", "Total<br>Costs", "Total"], 
  "ysrc": "HitchSlightly:1:fa1bfa", 
  "y": [430, 260, 690, 0, 0, 0, 0], 
  "marker": {
    "line": {
      "color": "rgba(55, 128, 191, 1.0)", 
      "width": 2
    }, 
    "color": "rgba(55, 128, 191, 0.7)"
  }
}
trace3 = {
  "meta": {"columnNames": {
      "x": "Trace 0, x; Trace 1, x; Trace 2, x; Trace 3, x", 
      "y": "Trace 2, y"
    }}, 
  "type": "bar", 
  "xsrc": "HitchSlightly:1:059fc8", 
  "x": ["Product<br>Revenue", "Services<br>Revenue", "Total<br>Revenue", "Fixed<br>Costs", "Variable<br>Costs", "Total<br>Costs", "Total"], 
  "ysrc": "HitchSlightly:1:49de38", 
  "y": [0, 0, 0, 120, 200, 320, 0], 
  "marker": {
    "line": {
      "color": "rgba(219, 64, 82, 1.0)", 
      "width": 2
    }, 
    "color": "rgba(219, 64, 82, 0.7)"
  }
}
trace4 = {
  "meta": {"columnNames": {
      "x": "Trace 0, x; Trace 1, x; Trace 2, x; Trace 3, x", 
      "y": "Trace 3, y"
    }}, 
  "type": "bar", 
  "xsrc": "HitchSlightly:1:059fc8", 
  "x": ["Product<br>Revenue", "Services<br>Revenue", "Total<br>Revenue", "Fixed<br>Costs", "Variable<br>Costs", "Total<br>Costs", "Total"], 
  "ysrc": "HitchSlightly:1:8fe538", 
  "y": [0, 0, 0, 0, 0, 0, 370], 
  "marker": {
    "line": {
      "color": "rgba(50, 171, 96, 1.0)", 
      "width": 2
    }, 
    "color": "rgba(50, 171, 96, 0.7)"
  }
}
data = Data([trace1, trace2, trace3, trace4])
layout = {
  "title": {"text": "Annual Profit- 2015"}, 
  "xaxis": {
    "type": "category", 
    "range": [-0.5, 6.5], 
    "autorange": True
  }, 
  "yaxis": {
    "type": "linear", 
    "range": [0, 726.3157894736842], 
    "autorange": True
  }, 
  "barmode": "stack", 
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
      "showarrow": False
    }
  ], 
  "plot_bgcolor": "rgba(245, 246, 249, 1)", 
  "paper_bgcolor": "rgba(245, 246, 249, 1)"
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)