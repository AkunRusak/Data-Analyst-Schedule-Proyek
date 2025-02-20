import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# memuat file CSV
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data['Start_Date'] = pd.to_datetime(data['Start_Date'], format="%d %B %Y %H.%M")
        data['Finish_Date'] = pd.to_datetime(data['Finish_Date'], format="%d %B %Y %H.%M")

        # untuk membersihkan spasi dalam kolom Durasi
        data['Duration'] = data['Duration'].str.replace(' days', '').str.replace(' day', '')
        data['Duration'] = data['Duration'].astype(int)  # mengkonversi ke integer
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# inisialisasi Dashboard
app = dash.Dash(__name__)

# memuat data
file_path = 'project_schedule.csv'  # mengganti jalur file
data = load_data(file_path)

if data is None:
    raise ValueError("Gagal memuat data. Silakan periksa jalur dan format file.")

# Desain App layout
app.layout = html.Div([
    html.H1("Schedule Proyek Pembangunan Transmisi SUTT 150KV Menes Baru - Tanjung Lesung PT. Krakatau Engineering", style={'text-align': 'center'}),

    dcc.Graph(id='gantt-chart'),

    html.Div([
        html.Label("Filter berdasarkan Durasi Tugas (hari):"),
        dcc.RangeSlider(
            id='duration-slider',
            min=data['Duration'].min(),
            max=data['Duration'].max(),
            step=1,
            marks={i: str(i) for i in range(int(data['Duration'].min()), int(data['Duration'].max()) + 1, 50)},
            value=[data['Duration'].min(), data['Duration'].max()]
        )
    ], style={'margin': '20px'}),

    dcc.Graph(id='duration-distribution'),
])

# Callback untuk bagan gantt-chart
@app.callback(
    Output('gantt-chart', 'figure'),
    [Input('duration-slider', 'value')]
)
def update_gantt(duration_range):
    filtered_data = data[(data['Duration'] >= duration_range[0]) & (data['Duration'] <= duration_range[1])]

    fig = px.timeline(
        filtered_data,
        x_start="Start_Date",
        x_end="Finish_Date",
        y="Task Name",
        title="Project Schedule Gantt Chart",
        color="Duration",
        labels={"Duration": "Duration (days)"}
    )
    
    fig.update_yaxes(
        categoryorder="total ascending",
        tickmode="array",
        tickvals=list(range(len(filtered_data))),
        ticktext=filtered_data["Task Name"].tolist(),
        
    )

    fig.update_layout(
    autosize=True,
    plot_bgcolor="#f7f9fb",
    paper_bgcolor="#ffffff",
    font=dict(color="#2c3e50"),
    title_font=dict(size=20),
    margin=dict(l=200, r=20, t=30, b=20),
    yaxis=dict(
        automargin=True,
        title=dict(text="Task Name", font=dict(size=14))
    )
)
    return fig

# Callback untuk distribusi duration-distribution
@app.callback(
    Output('duration-distribution', 'figure'),
    [Input('duration-slider', 'value')]
)
def update_duration_distribution(duration_range):
    filtered_data = data[(data['Duration'] >= duration_range[0]) & (data['Duration'] <= duration_range[1])]

    fig = px.histogram(
        filtered_data,
        x="Duration",
        nbins=20,
        title="Duration Distribution",
        labels={"Duration": "Duration (days)"},
        color_discrete_sequence=['skyblue']
    )
    fig.update_layout(xaxis_title="Duration (days)", yaxis_title="Frequency")
    return fig

# menjalankan server web Dashboard
if __name__ == "__main__":
    app.run_server(debug=True)
