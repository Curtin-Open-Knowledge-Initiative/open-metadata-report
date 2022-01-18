import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

from typing import Optional, Union, List

from observatory.reports.abstract_chart import AbstractObservatoryChart


class BarLine(AbstractObservatoryChart):
    def __init__(self,
                 xdata,
                 bardata,
                 linedata):

        self.xdata = xdata
        self.bardata = bardata
        self.linedata = linedata
        self.processed_data = False

    def process_data(self):
        assert len(self.xdata) == len(self.bardata)
        assert len(self.xdata) == len(self.linedata)

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
            name='Crossref DOIs'
        ), secondary_y=True)

        fig.add_trace(go.Scatter(
            x=self.xdata,
            y=self.linedata,
            mode='lines',
            name='DOIs in MAG (%)'
        ), secondary_y=False)

        fig.update_yaxes(title_text="Registered Crossref DOIs", secondary_y=True)
        fig.update_yaxes(title_text="DOIs in MAG (%)",
                         secondary_y=False,
                         range=[0,100])
        # Update template
        fig.update_layout(template='simple_white')

        return fig