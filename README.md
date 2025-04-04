# Laser Safety Calculator

The **Laser Safety Calculator** is an interactive tool that evaluates the nominal safety distance for a laser system. It computes key parameters such as the Rayleigh range and the distance behind the focal point where the energy density (in J/m²) on a target (simulated by an extremely small "eye" aperture) falls below a specified safety threshold. This allows users to determine the *Nominal Ocular Hazard Distance (NOHD)* for a given laser configuration.
The thresshold 10000 J / M^2 is taken from international eye safety standards and is the MPE for 1550 nm. Since 1550 nm cannot reach the retina, this wavelenght is preferred.

## Functionality

The calculator uses several input parameters, adjustable via interactive sliders:

- **Max Focal Length:** Maximum focal length (0.5 m to 10 m).
- **Selected Focal Length:** A specific focal length value within the above range for which output values are computed.
- **Wavelength:** Laser wavelength in nanometers.
- **M² (Beam Quality):** A factor representing the beam quality.
- **Beam Radius (w<sub>in</sub>):** The input beam radius at the lens in millimeters (adjustable up to 50 mm).
- **Laser Power:** The laser output power in Watts.
- **Exposure Time:** The duration for which the laser is on (in seconds, minimum 0.001 s).

For worst-case analysis, the eye is simulated as an infinitely small aperture (constant at \(1 \times 10^{-10}\) m) to capture the higher concentration of the Gaussian beam distribution.

## Calculation Steps

The safety calculator performs the following computations. Instead of rendering LaTeX, we embed screenshots of the formulas used:

1. **Rayleigh Range Calculation:**  
   The Rayleigh range \( z_R \) is calculated using:
   
   ![Rayleigh Range Formula](rayleigh_range_formula.png)
   
   where:
   - \( M^2 \) is the beam quality factor,
   - \( \lambda \) is the wavelength (in meters),
   - \( f \) is the focal length (in meters),
   - \( w_{in} \) is the input beam radius (in meters).

2. **Beam Waist Calculation:**  
   The beam waist \( w_0 \) at the focal point is given by:
   
   ![Beam Waist Formula](beam_waist_formula.png)

3. **Beam Radius as a Function of Distance \( x \) Behind the Focal Point:**  
   The beam radius \( w(x) \) is determined by:
   
   ![Beam Radius Formula](beam_radius_formula.png)

4. **Power Enclosed in a Circular Aperture (Simulated Eye):**  
   The fraction of beam power captured by an aperture of radius \( r \) is:
   
   ![Enclosed Power Formula](enclosed_power_formula.png)

5. **Energy Density Calculation:**  
   The energy density \( E \) (in J/m²) delivered to the eye over the exposure time \( t \) is computed as:
   
   ![Energy Density Formula](energy_density_formula.png)
   
   where:
   - \( P \) is the laser power,
   - \( t \) is the exposure time,
   - \( r \) is the eye radius.

6. **Nominal Safety Distance Determination:**  
   The safe distance \( x \) is found by iterating until \( E \) falls below 10,000 J/m², and the *Nominal Safety Distance* is:
   
   ![Nominal Safety Distance Formula](nominal_safety_distance_formula.png)
   
   That is,  
   $$
   \text{Nominal Safety Distance} = f + x
   $$

## Screenshots

Below are example screenshots of the program in action:

### Focal Point = 1 m
![Screenshot 1](screenshot1.png)  
![Screenshot 2](screenshot2.png)

### Focal Point = 8 m
![Screenshot 3](screenshot3.png)

## Conclusion

The results demonstrate that the nominal safety zone is not much wider for a 1 m focal point. Even with an 8 m focal point, the safety distance remains feasible when combined with additional safety sensors. This indicates that the laser system can be made safe across a range of configurations with appropriate sensor integration and safety measures.

---

*Note: Replace the image filenames with the actual filenames of your formula screenshots. These images must be committed to the same directory as the README.md for the links to work correctly.*
