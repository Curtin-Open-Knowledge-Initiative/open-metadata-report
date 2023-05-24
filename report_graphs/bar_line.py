import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

from typing import Optional, Union, List

from observatory.reports.abstract_chart import AbstractObservatoryChart


class BarLine(AbstractObservatoryChart):
    def __init__(self,
                 xdata,
                 bardata,
                 barname,
                 linedata,
                 linename):
        self.xdata = xdata
        self.bardata = bardata
        self.barname = barname
        self.linedata = linedata
        self.linename = linename
        self.processed_data = False

    def process_data(self,
                     **kwargs):
        assert len(self.xdata) == len(self.bardata)
        assert len(self.xdata) == len(self.linedata)

        palette = kwargs.get('palette')

    def plot(self):
        pass

    def plotly(self,
               **kwargs):
        if not self.processed_data:
            self.process_data()

        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(go.Bar(
            x=self.xdata,
            y=self.bardata,
            name=self.barname,
            opacity=0.65
        ), secondary_y=False)

        fig.add_trace(go.Scatter(
            x=self.xdata,
            y=self.linedata,
            mode='lines',
            name=self.linename
        ), secondary_y=True)

        fig.update_yaxes(title_text=self.barname, secondary_y=False, position=1, side='right')
        fig.update_yaxes(title_text=self.linename,
                         secondary_y=True, position=0, side='left',
                         range=[0, 100])
        # Update template
        fig.update_layout(template='simple_white',
                          colorway=palette)

        return fig
