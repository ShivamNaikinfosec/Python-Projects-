import matplotlib.pyplot as plt
import numpy as np
#This is a weather simulation of how a thunderstorm complex develops as a MCS(Mesocale Convective System

# Set up the figure and axis for the atmospheric cross-section
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_facecolor('#1a1a24')  # Dark, ominous pre-storm sky color

# 1. Simulate the Land Topography (Langlaagte Valley to Brixton Ridge)
x_terrain = np.linspace(0, 50, 500)
# A curve representing the elevation drop from the ridge into the valley basin
y_terrain = 2 - 1.2 / (1 + np.exp(-0.2 * (x_terrain - 20)))
ax.fill_between(x_terrain, 0, y_terrain, color='#2d302e', label='Terrain (Highveld Ridge/Valley)')

# 2. Plot the Cold Pool (Outflow Lake of Dense Air)
# Cold, dense air hugs the ground behind the leading edge of the storm
ax.fill_between(x_terrain[150:], y_terrain[150:], 3.5, where=(x_terrain[150:] > 15),
                color='#4a6984', alpha=0.3, label='Cold Pool (Dense Downdraft Air)')

# 3. Simulate and Plot the MCS Cloud Structures
# Leading Edge / Shelf Cloud (The horizontal wall of cloud)
x_shelf = np.linspace(12, 18, 100)
y_shelf_bottom = 3.5 + 0.5 * (x_shelf - 12)
y_shelf_top = 7 + 0.2 * (x_shelf - 12)
ax.fill_between(x_shelf, y_shelf_bottom, y_shelf_top, color='#3a404a', alpha=0.95)

# Main Explosive Updraft Tower (The convective core)
x_tower = np.linspace(17, 30, 200)
y_tower_bottom = 4.5 + 0.1 * (x_tower - 17)
y_tower_top = 11 - 0.02 * (x_tower - 25)**2
ax.fill_between(x_tower, y_tower_bottom, y_tower_top, color='#2c323d', alpha=0.95, label='Convective Updraft Core')

# Massive Stratiform Rain Shield Blanket (Trailing behind the core)
x_shield = np.linspace(29, 50, 200)
y_shield_bottom = 5.5 - 0.05 * (x_shield - 29)
y_shield_top = 10 - 0.08 * (x_shield - 29)
ax.fill_between(x_shield, y_shield_bottom, y_shield_top, color='#434a54', alpha=0.85, label='Stratiform Shield Blanket')

# 4. Add Visual Dynamics: Airflow Vectors (Arrows)
# Inflow: Warm, humid air being sucked from the valley into the core
ax.annotate('Warm, Humid Inflow Air\n(From Riverlea/Valleys)', xy=(18, 5.5), xytext=(2, 4),
            arrowprops=dict(facecolor='#e67e22', shrink=0.05, width=2, headwidth=8),
            color='#e67e22', fontsize=10, weight='bold')

# Outflow: Cold air slamming down to the surface
ax.annotate('Cold Heavy Downdraft\n(Collapsing Rain/Hail Core)', xy=(24, 3.8), xytext=(32, 7.5),
            arrowprops=dict(facecolor='#3498db', shrink=0.05, width=2, headwidth=8),
            color='#3498db', fontsize=10, weight='bold')

# 5. Add Rainfall Fields
# Heavy convective rain/hail under the core
x_heavy_rain = np.linspace(20, 28, 40)
for x in x_heavy_rain:
    terrain_height = 2 - 1.2 / (1 + np.exp(-0.2 * (x - 20)))
    ax.plot([x, x], [terrain_height, 5.0], color='#7fa9c7', alpha=0.4, linewidth=1.5, linestyle='--')
ax.text(21, 2.5, 'Heavy Core\n(Small Hail Zone)', color='#7fa9c7', weight='bold', fontsize=9)

# Steady, widespread stratiform rain under the massive blanket shield
x_steady_rain = np.linspace(29, 48, 60)
for x in x_steady_rain:
    terrain_height = 2 - 1.2 / (1 + np.exp(-0.2 * (x - 20)))
    ax.plot([x, x], [terrain_height, 5.2], color='#5d7a8c', alpha=0.25, linewidth=1, linestyle=':')
ax.text(36, 2.5, 'Widespread Steady Stratiform Rain\n(Stabilizes Atmosphere, Kills Tornadic Growth)', 
        color='#aab2bd', weight='bold', fontsize=9, ha='center')

# Labels and Diagram Details
ax.text(12, 4.3, 'Horizontal Shelf Cloud\n(Looks scary, but flat)', color='#f5f7fa', fontsize=9, weight='bold')
ax.set_title('Highveld Mesoscale Convective System (MCS) Structure', color='white', fontsize=14, weight='bold', pad=15)
ax.set_xlabel('Horizontal Distance Across Johannesburg Suburbs (km)', color='white')
ax.set_ylabel('Atmospheric Altitude (km)', color='white')
ax.tick_params(colors='white')
ax.set_ylim(0, 13)
ax.set_xlim(0, 50)
ax.grid(True, linestyle=':', alpha=0.2, color='white')
ax.legend(loc='upper right', facecolor='#1a1a24', labelcolor='white')

plt.tight_layout()
plt.show()

