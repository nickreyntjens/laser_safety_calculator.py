#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ---------------------------------------------------
# Initial Parameters
# ---------------------------------------------------
initial_fmax = 10.0              # Initial maximum focal length in m (range: 0.5 to 10 m)
initial_selected_f = 1.0         # Initial selected focal length in m
initial_wavelength_nm = 1550.0   # Wavelength (nm)
initial_M_squared = 2.0          # Beam quality factor (M²)
initial_w_in_mm = 2.5            # Input beam radius at the lens in mm
constant_eye_radius_m = 1e-10    # Very small eye radius for worst-case scenario
initial_laser_power = 10.0       # Laser power (W)
initial_exposure_time = 0.25     # Exposure time (s)
safety_energy_density = 10000.0  # Safety threshold (J/m²)

# ---------------------------------------------------
# Helper Functions
# ---------------------------------------------------
def calculate_rayleigh_range(f, w_in, wavelength, M_squared):
    return (M_squared * wavelength * f**2) / (np.pi * w_in**2)

def calculate_beam_waist(f, w_in, wavelength, M_squared):
    return (M_squared * wavelength * f) / (np.pi * w_in)

def beam_radius_at_x(w0, zR, x):
    return w0 * np.sqrt(1 + (x / zR)**2)

def power_enclosed_in_eye(wx, eye_radius):
    return 1.0 - np.exp(-2.0 * (eye_radius**2) / (wx**2))

def energy_density_at_x(x, f, w_in, wavelength, M_squared, eye_radius, laser_power, exposure_time):
    w0 = calculate_beam_waist(f, w_in, wavelength, M_squared)
    zR = calculate_rayleigh_range(f, w_in, wavelength, M_squared)
    wx = beam_radius_at_x(w0, zR, x)
    frac = power_enclosed_in_eye(wx, eye_radius)
    power_into_eye = laser_power * frac
    eye_area = np.pi * (eye_radius**2)
    return (power_into_eye * exposure_time) / eye_area

def find_safe_distance(f, w_in, wavelength, M_squared, eye_radius, laser_power, exposure_time, safety_energy_density):
    w0 = calculate_beam_waist(f, w_in, wavelength, M_squared)
    zR = calculate_rayleigh_range(f, w_in, wavelength, M_squared)
    x = zR
    max_search = 100.0
    while x < max_search:
        ed = energy_density_at_x(x, f, w_in, wavelength, M_squared, eye_radius, laser_power, exposure_time)
        if ed < safety_energy_density:
            return x
        x += 0.01
    return np.nan

# ---------------------------------------------------
# Main Interactive Plotting Function
# ---------------------------------------------------
def main():
    # Convert initial parameters to SI units
    wavelength_m = initial_wavelength_nm * 1e-9
    w_in_m = initial_w_in_mm * 1e-3

    num_points = 50
    focal_lengths = np.linspace(0.5, initial_fmax, num_points)

    rayleigh_vals = np.array([
        calculate_rayleigh_range(f, w_in_m, wavelength_m, initial_M_squared)
        for f in focal_lengths
    ])
    safe_x_vals = np.array([
        find_safe_distance(f, w_in_m, wavelength_m, initial_M_squared,
                           constant_eye_radius_m, initial_laser_power,
                           initial_exposure_time, safety_energy_density)
        for f in focal_lengths
    ])
    nohd_vals = focal_lengths + safe_x_vals

    fig, ax = plt.subplots()
    # Adjust right margin to make room for the text annotation.
    plt.subplots_adjust(left=0.25, bottom=0.65, right=0.75)

    rayleigh_line, = ax.plot(focal_lengths, rayleigh_vals, '-o', color='blue', label="Rayleigh Range (z_R)")
    safe_x_line, = ax.plot(focal_lengths, safe_x_vals, '-o', color='green', label="Safe_x (x)")
    nohd_line, = ax.plot(focal_lengths, nohd_vals, '-o', color='orange', label="Nominal Safety Distance (f + x)")

    ax.set_xlabel("Focal Length (m)")
    ax.set_ylabel("Distance (m)")
    ax.set_title("Laser Safety vs. Focal Length")
    ax.grid(True)
    ax.legend(loc='upper left')

    # Place text outside the main plot area, on the right.
    text_display = ax.text(
        1.02, 0.95, "",
        transform=ax.transAxes,
        va="top", ha="left",
        bbox=dict(facecolor="white", alpha=0.7)
    )

    axcolor = 'lightgoldenrodyellow'
    ax_fmax = plt.axes([0.25, 0.55, 0.65, 0.03], facecolor=axcolor)
    ax_selected = plt.axes([0.25, 0.50, 0.65, 0.03], facecolor=axcolor)
    ax_wavelength = plt.axes([0.25, 0.45, 0.65, 0.03], facecolor=axcolor)
    ax_M_squared = plt.axes([0.25, 0.40, 0.65, 0.03], facecolor=axcolor)
    ax_w_in = plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=axcolor)
    ax_power = plt.axes([0.25, 0.30, 0.65, 0.03], facecolor=axcolor)
    ax_exposure = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)

    # Create sliders.
    s_fmax = Slider(ax_fmax, 'Max Focal Length (m)', 0.5, 10.0, valinit=initial_fmax, valstep=0.01)
    s_selected = Slider(ax_selected, 'Selected Focal Length (m)', 0.5, initial_fmax, valinit=initial_selected_f, valstep=0.01)
    s_wavelength = Slider(ax_wavelength, 'Wavelength (nm)', 500, 2000, valinit=initial_wavelength_nm, valstep=10)
    s_M_squared = Slider(ax_M_squared, 'M²', 1, 5, valinit=initial_M_squared, valstep=0.1)
    # Update the beam radius slider max to 50 mm.
    s_w_in = Slider(ax_w_in, 'Beam Radius (mm)', 0.1, 50, valinit=initial_w_in_mm, valstep=0.1)
    s_power = Slider(ax_power, 'Laser Power (W)', 1, 50, valinit=initial_laser_power, valstep=1)
    s_exposure = Slider(ax_exposure, 'Exposure Time (s)', 0.001, 5, valinit=initial_exposure_time, valstep=0.001)

    def update(_):
        fmax_val = s_fmax.val
        selected_val = s_selected.val
        wavelength_val = s_wavelength.val * 1e-9
        M_val = s_M_squared.val
        w_in_val = s_w_in.val * 1e-3
        power_val = s_power.val
        exposure_val = s_exposure.val

        # Ensure selected focal length does not exceed max.
        s_selected.ax.set_xlim(0.5, fmax_val)
        if selected_val > fmax_val:
            s_selected.set_val(fmax_val)

        focal_lengths_new = np.linspace(0.5, fmax_val, num_points)
        rayleigh_new = np.array([
            calculate_rayleigh_range(f, w_in_val, wavelength_val, M_val)
            for f in focal_lengths_new
        ])
        safe_new = np.array([
            find_safe_distance(f, w_in_val, wavelength_val, M_val, constant_eye_radius_m,
                               power_val, exposure_val, safety_energy_density)
            for f in focal_lengths_new
        ])
        nohd_new = focal_lengths_new + safe_new

        rayleigh_line.set_data(focal_lengths_new, rayleigh_new)
        safe_x_line.set_data(focal_lengths_new, safe_new)
        nohd_line.set_data(focal_lengths_new, nohd_new)

        ax.set_xlim(focal_lengths_new[0], focal_lengths_new[-1])
        all_y = np.concatenate((rayleigh_new, safe_new, nohd_new))
        ax.set_ylim(0, np.nanmax(all_y) * 1.1 if np.isfinite(np.nanmax(all_y)) else 1)
        ax.legend(loc='upper left')

        # Compute for the selected focal length.
        rayleigh_sel = calculate_rayleigh_range(selected_val, w_in_val, wavelength_val, M_val)
        safe_sel = find_safe_distance(selected_val, w_in_val, wavelength_val, M_val,
                                      constant_eye_radius_m, power_val, exposure_val, safety_energy_density)
        nohd_sel = selected_val + safe_sel

        # Update text.
        text_display.set_text(
            f"Selected f: {selected_val:.2f} m\n"
            f"Rayleigh: {rayleigh_sel:.2f} m\n"
            f"Safe_x: {safe_sel:.2f} m\n"
            f"Nominal Safety Distance: {nohd_sel:.2f} m"
        )

        fig.canvas.draw_idle()

    s_fmax.on_changed(update)
    s_selected.on_changed(update)
    s_wavelength.on_changed(update)
    s_M_squared.on_changed(update)
    s_w_in.on_changed(update)
    s_power.on_changed(update)
    s_exposure.on_changed(update)

    plt.show()

if __name__ == '__main__':
    main()

