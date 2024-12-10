import numpy as np
import matplotlib.pyplot as plt
import pywt

# Step 1: Generate a Digital Signal (Binary Sequence)
# Generate a binary digital signal (0s and 1s)
signal_length = 16  # Length of the signal
digital_signal = np.random.choice([0, 1], size=signal_length)

# Plot the original digital signal
plt.figure(figsize=(8, 4))
plt.stem(digital_signal)  # Removed 'use_line_collection'
plt.title("Original Digital Signal")
plt.xlabel("Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Step 2: Add Noise to the Digital Signal
# Adding Gaussian noise to the digital signal
noise = np.random.normal(0, 0.1, digital_signal.shape)
noisy_signal = digital_signal + noise

# Plot the noisy digital signal
plt.figure(figsize=(8, 4))
plt.stem(noisy_signal)  # Removed 'use_line_collection'
plt.title("Noisy Digital Signal")
plt.xlabel("Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Step 3: Perform Wavelet Decomposition (Single Level)
# Perform single-level wavelet decomposition using Haar wavelet
coeffs = pywt.dwt(noisy_signal, 'haar')

# Coefficients: (CA, CD)
CA, CD = coeffs

# Plot the Approximation (CA) and Detail (CD) coefficients
plt.figure(figsize=(8, 6))

plt.subplot(2, 1, 1)
plt.stem(CA)  # Removed 'use_line_collection'
plt.title("Approximation Coefficients (CA)")

plt.subplot(2, 1, 2)
plt.stem(CD)  # Removed 'use_line_collection'
plt.title("Detail Coefficients (CD)")

plt.tight_layout()
plt.show()

# Step 4: Reconstruct the Digital Signal
# Reconstruct the signal from CA and CD using inverse DWT
reconstructed_signal = pywt.idwt(CA, CD, 'haar')

# Step 5: Apply Thresholding to Reconstructed Signal
# Threshold at 0.5 to classify values as 0 or 1
thresholded_signal = np.where(reconstructed_signal >= 0.5, 1, 0)

# Plot the original, noisy, reconstructed, and thresholded signals
plt.figure(figsize=(8, 6))

plt.subplot(4, 1, 1)
plt.stem(digital_signal)  # Removed 'use_line_collection'
plt.title("Original Digital Signal")

plt.subplot(4, 1, 2)
plt.stem(noisy_signal)  # Removed 'use_line_collection'
plt.title("Noisy Digital Signal")

plt.subplot(4, 1, 3)
plt.stem(reconstructed_signal)  # Removed 'use_line_collection'
plt.title("Reconstructed Digital Signal")

plt.subplot(4, 1, 4)
plt.stem(thresholded_signal)  # Removed 'use_line_collection'
plt.title("Thresholded Signal")

plt.tight_layout()
plt.show()

# Step 6: Print Coefficients
# Print the CA and CD coefficients
print("Approximation Coefficients (CA):")
print(CA)
print("\nDetail Coefficients (CD):")
print(CD)
