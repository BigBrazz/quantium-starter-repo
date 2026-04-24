import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

app = dash.Dash(__name__)

app.layout = html.Div(style={
    "fontFamily": "Arial",
    "backgroundColor": "#f4f6f8",
    "padding": "20px"
}, children=[

    html.H1(
        "Pink Morsel Sales Dashboard",
        style={"textAlign": "center", "color": "#333"}
    ),

    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold"}),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        ),
    ]),

    dcc.Graph(id="sales-chart")
])


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="white"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)