# Laser Safety Calculator

The **Laser Safety Calculator** is an interactive tool that evaluates the nominal safety distance for a laser system. It computes key parameters such as the Rayleigh range and the distance behind the focal point where the energy density (in J/m²) on a target (simulated by a very small "eye" aperture) falls below a specified safety threshold. This allows users to determine the *Nominal Ocular Hazard Distance (NOHD)* for a given laser configuration.

## Functionality

The calculator uses several input parameters, adjustable via interactive sliders:

- **Max Focal Length:** The maximum focal length in meters (range: 0.5 m to 10 m).
- **Selected Focal Length:** A specific focal length value within the above range for which output values are computed.
- **Wavelength:** Laser wavelength in nanometers.
- **M² (Beam Quality):** A factor representing the beam quality.
- **Beam Radius (w<sub>in</sub>):** The radius of the input beam at the lens in millimeters (adjustable up to 50 mm).
- **Laser Power:** The laser output power in Watts.
- **Exposure Time:** The duration for which the laser is on (in seconds, minimum 0.001 s).

The eye is simulated as a very small aperture (constant at 1e-10 m) to capture the worst-case scenario for beam concentration.

## Calculation Steps

The calculator performs the following computations:

1. **Rayleigh Range Calculation:**  
   The Rayleigh range \( z_R \) is given by:  
   $$
   z_R = \frac{M^2 \lambda f^2}{\pi w_{in}^2}
   $$
   where:
   - \( M^2 \) is the beam quality factor,
   - \( \lambda \) is the wavelength (in meters),
   - \( f \) is the focal length (in meters),
   - \( w_{in} \) is the input beam radius (in meters).

2. **Beam Waist Calculation:**  
   The beam waist \( w_0 \) at the focal point is calculated as:  
   $$
   w_0 = \frac{M^2 \lambda f}{\pi w_{in}}
   $$

3. **Beam Radius as a Function of Distance \( x \) Behind the Focal Point:**  
   The beam radius \( w(x) \) is determined by:  
   $$
   w(x) = w_0 \sqrt{1 + \left(\frac{x}{z_R}\right)^2}
   $$

4. **Power Enclosed in a Circular Aperture (Simulated Eye):**  
   The fraction of beam power captured by an aperture of radius \( r \) is given by the Gaussian profile:  
   $$
   P_{enc} = 1 - \exp\left(-\frac{2r^2}{w(x)^2}\right)
   $$

5. **Energy Density Calculation:**  
   The energy density \( E \) (in J/m²) delivered to the eye over the exposure time \( t \) is computed as:  
   $$
   E = \frac{P \cdot P_{enc} \cdot t}{\pi r^2}
   $$
   where:
   - \( P \) is the laser power,
   - \( t \) is the exposure time,
   - \( r \) is the (small) eye radius.

6. **Safe Distance Determination:**  
   The script iterates over distances \( x \) (starting at \( x = z_R \)) until the energy density \( E \) drops below the safety threshold (10,000 J/m²). The *Nominal Safety Distance* is then given by:
   $$
   \text{Nominal Safety Distance} = f + x
   $$

## Screenshots

Below are example screenshots of the program in action:

- **Focal Point = 1 m:**  
  (Screenshot 1)  
  (Screenshot 2)

- **Focal Point = 8 m:**  
  (Screenshot 3)

## Conclusion

The results show that the nominal safety zone does not increase significantly for a 1 m focal point. Even with an 8 m focal point, the safety distance is within feasible limits when combined with additional safety sensors. This indicates that the laser system can be made safe across a range of configurations with proper sensor integration and safety measures.

---

Feel free to modify or expand this README as needed. Enjoy using the Laser Safety Calculator!

