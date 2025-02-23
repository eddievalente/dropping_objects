import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Definition of parameters
g = 9.81  # Acceleration due to gravity (m/s²)
dt = 0.001  # Time step (s)
coefficient_of_restitution = 0.7  # Energy loss at each bounce

# Input data
initial_height = float(input("Enter the initial height (m): "))
horizontal_velocity = float(input("Enter the horizontal velocity (m/s): "))

# Variable definitions
x = 0  # Initial horizontal position
y = initial_height  # Initial vertical position
vy = 0  # Initial vertical velocity
time = 0  # Total simulation time

# Lists to store data for plotting
x_data, y_data = [x], [y]

# Simulation loop
while abs(vy) > 0.01 or y > 0:
    vy += -g * dt  # Update vertical velocity
    y += vy * dt  # Update vertical position
    x += horizontal_velocity * dt  # Update horizontal position
    
    # If it hits the ground, reverse the vertical velocity considering energy loss
    if y <= 0:
        y = 0
        vy = -vy * coefficient_of_restitution
    
    x_data.append(x)
    y_data.append(y)
    time += dt

# Animation
fig, ax = plt.subplots()
ax.set_xlim(0, max(x_data))
ax.set_ylim(0, initial_height)
point, = ax.plot([], [], 'bo', markersize=8, animated=True)


# Update function for the animation
def update(frame):
    if frame >= len(x_data):  # Evita acessar índices fora do alcance
        return point,
    
    point.set_data([x_data[frame]], [y_data[frame]])  # Deve ser uma lista
    return point,

ani = animation.FuncAnimation(fig, update, frames=len(x_data), interval=dt*1000, blit=True)

plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.title("Free Fall Simulation with Bounces")
plt.show()
