import matplotlib.pyplot as plt
import numpy as np

# Define tracking timeline (steps over a 2-hour storm duration)
time_steps = np.linspace(0, 120, 100)

# 1. Normal Storm Trajectory (Follows the background mean wind straight East)
x_normal = 0.5 * time_steps  # Standard easterly velocity component
y_normal = np.zeros_like(time_steps)  # Stays perfectly on the baseline wind track

# 2. Supercell "Right-Mover" Trajectory (Internal rotation alters the path)
# The storm splits, and internal vertical pressure gradients force it Northeast
x_supercell = 0.45 * time_steps  # Slower easterly progression
y_supercell = 0.002 * (time_steps ** 2)  # Quadratic curving northward/northeastward

# Plot the tactical navigation grid
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('#1e222b')  # Dark interface theme

# Plot your home safety zone anchor
ax.plot(0, 0, 'go', markersize=12, markeredgecolor='w', label='Langlaagte North')

# Plot the storm trajectories
ax.plot(x_normal, y_normal, color='#aab2bd', linestyle='--', linewidth=2, label='Normal Storm Track (Straight East)')
ax.plot(x_supercell, y_supercell, color='#e74c3c', linewidth=3, label='Supercell Track (Pivoting Northeast)')

# Annotate visual highlights from your Feb 17 observation
ax.annotate('Your Observation Point:\nPartly Cloudy & Dry Sky', xy=(5, 0), xytext=(5, -2),
            arrowprops=dict(facecolor='#3498db', shrink=0.08, width=1, headwidth=6),
            color='#3498db', weight='bold', fontsize=9)

ax.annotate('Storm Hooks Northeast:\nAway from your Neighborhood!', xy=(45, 4), xytext=(20, 8),
            arrowprops=dict(facecolor='#2ecc71', shrink=0.08, width=1, headwidth=6),
            color='#2ecc71', weight='bold', fontsize=9)

# Formatting the meteorological chart
ax.set_title('Highveld Supercell Deflection Vector Model (Feb 17, 2026)', color='w', fontsize=12, weight='bold', pad=15)
ax.set_xlabel('West-to-East Geographic Distance Axis (km)', color='w')
ax.set_ylabel('South-to-North Geographic Distance Axis (km)', color='w')
ax.tick_params(colors='w')
ax.set_xlim(-5, 65)
ax.set_ylim(-5, 35)
ax.grid(True, linestyle=':', alpha=0.2, color='w')
ax.legend(loc='upper left', facecolor='#1e222b', labelcolor='w')

plt.tight_layout()
plt.show()
