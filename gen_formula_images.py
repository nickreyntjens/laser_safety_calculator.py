#!/usr/bin/env python3
import matplotlib.pyplot as plt

# Define the formulas with corresponding filenames.
formulas = {
    "rayleigh_range_formula.png": r"$z_R = \frac{M^2\, \lambda\, f^2}{\pi\, w_{in}^2}$",
    "beam_waist_formula.png": r"$w_0 = \frac{M^2\, \lambda\, f}{\pi\, w_{in}}$",
    "beam_radius_formula.png": r"$w(x) = w_0 \sqrt{1+\left(\frac{x}{z_R}\right)^2}$",
    "enclosed_power_formula.png": r"$P_{enc} = 1 - \exp\left(-\frac{2r^2}{w(x)^2}\right)$",
    "energy_density_formula.png": r"$E = \frac{P\; P_{enc}\; t}{\pi\, r^2}$",
    "nominal_safety_distance_formula.png": r"$\text{Nominal Safety Distance} = f + x$"
}

# Loop over each formula and save an image.
for filename, formula in formulas.items():
    # Create a figure with white background
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.text(0.5, 0.5, formula, fontsize=24, ha='center', va='center')
    ax.axis('off')  # Hide axes
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)
    plt.close(fig)

print("Formula images generated successfully!")

