Wavelet in Channel Coding
Overview
This project explores the application of Wavelet Transforms in Channel Coding to enhance signal quality and improve data transmission efficiency. Wavelets, particularly Haar Wavelets, are used for signal decomposition, noise reduction, and reconstruction in communication systems, enabling reliable data transmission.

Features
Implementation of Haar Wavelet Transform for:
Decomposing signals into approximation and detail components.
Filtering noise and reconstructing the original signal.
Handling noisy digital signals to demonstrate noise removal.
Visualization of the signal processing workflow.
Project Workflow
Signal Generation:

Generate a binary digital signal to represent transmitted data.
Add Noise:

Simulate real-world transmission scenarios by adding Gaussian noise to the signal.
Wavelet Transform:

Apply Haar Wavelet Transform to decompose the signal into:
Approximation Coefficients (Low-pass): Represent the primary structure of the signal.
Detail Coefficients (High-pass): Capture variations like noise.
Signal Reconstruction:

Reconstruct the signal using the coefficients, reducing noise and preserving key features.
Visualization:

Plot the original signal, noisy signal, decomposed components, and reconstructed signal for comparison.
Applications
Error Correction: Minimize transmission errors by reducing noise.
Signal Compression: Efficiently transmit data by isolating critical components.
Reliable Communication: Improve signal-to-noise ratio (SNR) for robust communication.
