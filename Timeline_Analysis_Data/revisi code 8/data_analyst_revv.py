import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data['Start_Date'] = pd.to_datetime(data['Start_Date'], format="%d %B %Y %H.%M")
    data['Finish_Date'] = pd.to_datetime(data['Finish_Date'], format="%d %B %Y %H.%M")
    data['Duration'] = data['Duration'].str.replace(' days', '').str.replace(' day', '').astype(int)
    return data

data = load_data('project_schedule.csv')

# App setup
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Project Schedule Dashboard", style={"textAlign": "center", "marginBottom": "20px"}),

    # Filters
    html.Div([
        dcc.Dropdown(
            id="task_filter",
            options=[{"label": task, "value": task} for task in data["Task Name"].unique()],
            placeholder="Select Task Name",
            multi=True,
            style={"width": "40%"}
        ),
        dcc.RangeSlider(
            id="duration_filter",
            min=data["Duration"].min(),
            max=data["Duration"].max(),
            step=1,
            marks={i: str(i) for i in range(data["Duration"].min(), data["Duration"].max() + 1, 50)},
            value=[data["Duration"].min(), data["Duration"].max()],
        ),
    ], style={"marginBottom": "20px"}),

    # Statistics
    html.Div([
        html.Div([
            html.H4("Total Tasks"),
            html.P(len(data)),
        ], style={"textAlign": "center", "width": "30%", "display": "inline-block"}),

        html.Div([
            html.H4("Longest Task Duration"),
            html.P(f"{data['Duration'].max()} days"),
        ], style={"textAlign": "center", "width": "30%", "display": "inline-block"}),

        html.Div([
            html.H4("Shortest Task Duration"),
            html.P(f"{data['Duration'].min()} days"),
        ], style={"textAlign": "center", "width": "30%", "display": "inline-block"}),
    ], style={"marginBottom": "20px"}),

    # Graphs
    html.Div([
        dcc.Graph(id="gantt_chart"),
        dcc.Graph(id="duration_distribution"),
    ]),
])

# Callbacks
@app.callback(
    [Output("gantt_chart", "figure"), Output("duration_distribution", "figure")],
    [Input("task_filter", "value"), Input("duration_filter", "value")]
)
def update_graphs(selected_tasks, duration_range):
    filtered_data = data[
        (data["Duration"] >= duration_range[0]) & 
        (data["Duration"] <= duration_range[1])
    ]
    if selected_tasks:
        filtered_data = filtered_data[filtered_data["Task Name"].isin(selected_tasks)]

    # Gantt Chart
    gantt_chart = px.timeline(
        filtered_data,
        x_start="Start_Date",
        x_end="Finish_Date",
        y="Task Name",
        title="Gantt Chart",
        color="Duration",
    )

    # Duration Distribution
    duration_distribution = px.histogram(
        filtered_data,
        x="Duration",
        title="Task Duration Distribution",
        nbins=20,
        color_discrete_sequence=["#636EFA"]
    )

    return gantt_chart, duration_distribution

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
