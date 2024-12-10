import pywt
import numpy as np
import matplotlib.pyplot as plt

# Function to add noise to the data
def add_noise(data, error_rate=0.1):
    noisy_data = data.copy()
    num_errors = int(len(data) * error_rate)
    error_indices = np.random.choice(len(data), num_errors, replace=False)
    for idx in error_indices:
        noisy_data[idx] = (noisy_data[idx] + np.random.randint(1, 10)) % 256
    return noisy_data

# Function to manually correct errors using redundancy (simplified example)
def correct_errors(data, reference):
    corrected = data.copy()
    for i in range(len(data)):
        if abs(data[i] - reference[i]) > 20:  # Threshold for error detection
            corrected[i] = reference[i]  # Correct using reference
    return corrected

# Generate input signal
np.random.seed(42)  # For reproducibility
original_data = np.random.randint(0, 256, 64)  # Example: 64 random integers (0-255)

# Step 1: Wavelet-Based Channel Encoding
wavelet = 'haar'
coeffs = pywt.wavedec(original_data, wavelet, level=2)  # Wavelet decomposition

# Extract low-frequency coefficients
low_frequency_coeffs = coeffs[0]

# Simulate transmission with noise
noisy_low_frequency_coeffs = add_noise(low_frequency_coeffs, error_rate=0.1)

# Correct errors manually using the original low-frequency coefficients as a reference
corrected_low_frequency_coeffs = correct_errors(noisy_low_frequency_coeffs, low_frequency_coeffs)

# Replace low-frequency coefficients with corrected ones
coeffs[0] = corrected_low_frequency_coeffs

# Reconstruct the signal using inverse wavelet transform
reconstructed_wavelet_data = pywt.waverec(coeffs, wavelet)

# Step 2: Alternative Method - Parity-Based Channel Encoding
parity_data = np.hstack((original_data, [original_data.sum() % 256]))  # Add parity bit
noisy_parity_data = add_noise(parity_data)

# Parity decoding and error detection
if noisy_parity_data[:-1].sum() % 256 == noisy_parity_data[-1]:
    reconstructed_parity_data = noisy_parity_data[:-1]
else:
    reconstructed_parity_data = np.zeros_like(original_data)  # Error detected but not corrected

# Plotting the signals
plt.figure(figsize=(12, 8))

# Original Signal
plt.subplot(3, 1, 1)
plt.plot(original_data, label="Original Signal", color='blue')
plt.title("Original Signal")
plt.legend()

# Reconstructed Signal - Wavelet Encoding
plt.subplot(3, 1, 2)
plt.plot(reconstructed_wavelet_data[:len(original_data)], label="Reconstructed (Wavelet)", color='green')
plt.title("Wavelet-Based Encoding")
plt.legend()

# Reconstructed Signal - Parity Encoding
plt.subplot(3, 1, 3)
plt.plot(reconstructed_parity_data, label="Reconstructed (Parity)", color='orange')
plt.title("Parity-Based Encoding")
plt.legend()

plt.tight_layout()
plt.show()

# Compare results
wavelet_mse = np.mean((original_data - reconstructed_wavelet_data[:len(original_data)]) ** 2)
parity_mse = np.mean((original_data - reconstructed_parity_data) ** 2)

print("\nPerformance Comparison:")
print(f"Wavelet-Based Encoding Mean Squared Error (MSE): {wavelet_mse:.4f}")
print(f"Parity-Based Encoding Mean Squared Error (MSE): {parity_mse:.4f}")
