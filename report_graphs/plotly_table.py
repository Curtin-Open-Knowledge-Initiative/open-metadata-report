import plotly.graph_objects as go
import pandas as pd

from typing import Optional, Union, List  # , Literal

from observatory.reports.abstract_chart import AbstractObservatoryChart


class PlotlyTable(AbstractObservatoryChart):

    def __init__(self,
                 table_dict):
        self.table_dict = table_dict
        self.processed_data = False
        self.figdata = None

    def process_data(self):

        header_values = [column.get('name') for column in self.table_dict.get('columns')]
        header_alignment = [column.get('alignment') for column in self.table_dict.get('columns')]
        column_values = [
            [row.get(column) for row in self.table_dict.get('rows')]
            for column in header_values
        ]
        figdata = [go.Table(header=dict(values=header_values,
                                     align=header_alignment),
                         cells=dict(values=column_values,
                                    align=header_alignment))
                ]
        self.figdata = figdata

    def plot(self):
        pass

    def plotly(self):
        if not self.figdata:
            self.process_data()
        fig = go.Figure(data=self.figdata)
        return fig
