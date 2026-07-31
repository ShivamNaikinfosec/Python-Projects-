import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

#Client side interface users will interact with weathersmarty api 

# Initialize the Dash application
app = dash.Dash(__name__, title="Global Weather Early-Warning Aggregator")

# Layout definition: Top Header -> Navigation Tabs -> Tab Content Container
app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '20px'}, children=[
    html.H1("Global Weather Resilience Platform", style={'textAlign': 'center', 'color': '#2C3E50'}),
    html.P("Shivam Naik Intellectual Property — Open-Core Template Client", style={'textAlign': 'center', 'color': '#7F8C8D'}),
    
    # Core Tabbed System
    dcc.Tabs(id="dashboard-tabs", value="tab-map", children=[
        dcc.Tab(label="🌐 Live Threat Map", value="tab-map"),
        dcc.Tab(label="💬 Chaser & Meteorologist Forums", value="tab-forum"),
        dcc.Tab(label="⚠️ Active Weather Warnings", value="tab-warnings"),
    ]),
    
    # Dynamic container filled by the callback functions below
    html.Div(id="tab-content-render", style={'marginTop': '20px'})
])

# ==============================================================================
# TAB RENDERING CONTROLLER (Open Source - Devs can expand this)
# ==============================================================================
@app.callback(
    Output("tab-content-render", "children"),
    Input("dashboard-tabs", "value")
)
def render_tab_content(tab_name):
    if tab_name == "tab-map":
        return generate_map_interface()
    elif tab_name == "tab-forum":
        return generate_forum_interface()
    elif tab_name == "tab-warnings":
        return generate_warnings_interface()

# ==============================================================================
# FUNCTION: GENERATE INTERACTIVE GEO-MAP LAYER
# ==============================================================================
def generate_map_interface():
    # Simulated incoming event telemetry payload from your AWS pipeline
    mock_active_zones = [
        {"lat": -26.2041, "lon": 28.0473, "city": "Johannesburg", "type": "Severe Thunderstorm", "color": "red", "radius": 40},
        {"lat": 25.7617, "lon": -80.1918, "city": "Miami", "type": "Hurricane", "color": "maroon", "radius": 150},
        {"lat": 35.4676, "lon": -97.5164, "city": "Oklahoma City", "type": "Tornado on Ground", "color": "yellow", "radius": 25}
    ]
    
    fig = go.Figure()

    # Draw the dynamic, colored geographic risk regions onto the map
    for zone in mock_active_zones:
        fig.add_trace(go.Scattermap(
            lat=[zone["lat"]],
            lon=[zone["lon"]],
            mode='markers',
            marker=go.scattermap.Marker(
                size=zone["radius"],
                color=zone["color"],
                opacity=0.6
            ),
            text=f"🚨 EMERGENCY WARNING: {zone['type']} detected over {zone['city']}!",
            hoverinfo='text',
            name=zone['type']
        ))

    # Configure global map aesthetics and background engine
    fig.update_layout(
        map=dict(
            style="open-street-map",  # Completely free, zero-cost tier dependency mapping
            center=dict(lat=0, lon=0),
            zoom=1
        ),
        margin=dict(r=0, t=0, l=0, b=0),
        height=600,
        showlegend=True
    )

    return html.Div([
        html.H3("Active Tactical Risk Zones & SOS Geo-Broadcasts"),
        dcc.Graph(figure=fig),
        html.Div(id="sos-alert-box", style={'marginTop': '15px', 'padding': '15px', 'backgroundColor': '#FDEDEC', 'borderLeft': '5px solid #C0392B'}, children=[
            html.B("🚨 CRITICAL SOS EMERGENCY BROADCAST ENGINES ACTIVE:"),
            html.P("Geofenced push alerts are broadcasting location coordinates directly to regional emergency response networks and civilian cell networks within the highlighted impact boundaries.")
        ])
    ])

def generate_forum_interface():
    return html.Div([
        html.H3("Storm Chasers & Meteorologists Secure Forum"),
        html.P("Decentralized peer-to-peer communication node. (AWS ECS / Fargate container layer connection pending).")
    ])

def generate_warnings_interface():
    return html.Div([
        html.H3("Active Infrastructure Feed Targets"),
        html.P("Historical and active logging indices powered by Amazon Timestream database pipelines.")
    ])

if __name__ == "__main__":
    # Runs a local server. Open http://127.0.0.1:8050 in your browser to view
    app.run_server(debug=True)
