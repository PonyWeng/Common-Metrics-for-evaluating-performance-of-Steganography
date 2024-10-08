# Common-Metrics-for-evaluating-performance-of-Steganography

In this project, we collect lots of evaluation metrics or tools for evaluating the performance of Steganography methods or information hiding techniques.

Some of metrics are provided:

### Peak Signal-to-Noise Ratio (PSNR)

- **PSNR**: The PSNR value measures the quality of the reconstructed or compressed image relative to the original image. It is expressed in decibels (dB).

The formula for PSNR is defined as:

$$
\text{PSNR} = 10 \cdot \log_{10} \left( \frac{{\text{MAX}^2}}{{\text{MSE}}} \right)
$$

- **MAX**: The maximum possible pixel value of the image. For an 8-bit grayscale image, `MAX = 255`.
- **MSE**: The Mean Squared Error between the original and distorted images, defined as:

$$
\text{MSE} = \frac{1}{mn} \sum_{i=0}^{m-1} \sum_{j=0}^{n-1} \left[ I(i,j) - K(i,j) \right]^2  
$$

where:
  - \( I(i, j) \) is the pixel value at position \( (i, j) \) in the original image.
  - \( K(i, j) \) is the pixel value at position \( (i, j) \) in the distorted image.
  - \( m \) and \( n \) are the height and width of the images, respectively.

The PSNR value is typically used to evaluate the quality of compressed or reconstructed images. A higher PSNR value indicates better image quality and less distortion.

---
### Structural Similarity Index Measure (SSIM)
The SSIM formula is defined as:

$$
\text{SSIM}(x, y) = \frac{(2 \mu_x \mu_y + C_1)(2 \sigma_{xy} + C_2)}{(\mu_x^2 + \mu_y^2 + C_1)(\sigma_x^2 + \sigma_y^2 + C_2)}
$$

- **\( C_1 \) and \( C_2 \)**: Constants added to stabilize the division, preventing the denominator from approaching zero. These constants are defined as:

$$
C_1 = (K_1 \cdot L)^2, \quad C_2 = (K_2 \cdot L)^2
$$

  where:
  - \( L \) is the dynamic range of the pixel values (e.g., \( L = 255 \) for 8-bit images).
  - \( K_1 \) and \( K_2 \) are small constants (typically \( K_1 = 0.01 \) and \( K_2 = 0.03 \)).

The SSIM index measures the similarity between two images in terms of luminance, contrast, and structure. Its value ranges from \(-1\) to \(1\), where \(1\) indicates perfect similarity.

---

### Image Entropy for Grayscale Images

$$
H = - \sum_{i=0}^{L-1} p_i \cdot \log_2(p_i)
$$


- **\( H \)**: The image entropy.
- **\( L \)**: The number of gray levels in the grayscale image (usually, \( L = 256 \)).
- **\( p_i \)**: The probability of occurrence of the \( i \)-th gray level, which is the proportion of pixels having the \( i \)-th gray value in the entire image:

  $$
  p_i = \frac{n_i}{N}
  $$

- **\( n_i \)**: The number of pixels having the \( i \)-th gray value.
- **\( N \)**: The total number of pixels in the image.

Entropy measures the uncertainty or information content of the pixel distribution in an image. When all gray levels have an equal probability of occurrence (i.e., the image has maximum uncertainty), the entropy value is maximized.

---

## Some of analysis tools:

### Histogram Analysis

Histogram analysis is a technique used to examine the distribution of pixel intensities in an image. By analyzing the histogram of both the original image and the stego-image, we can determine whether there are significant differences in their pixel value distributions. This analysis helps identify any abnormal gaps or the emergence of multiple peak points in the histogram.

#### Purpose

The main objectives of histogram analysis include:

- **Detecting Differences**: Assessing the histogram distributions of the original and stego-images to identify any noticeable differences that may indicate the presence of hidden information.
- **Identifying Anomalies**: Spotting irregularities such as gaps in the histogram, which may suggest distortions or artifacts introduced during the embedding process.
- **Finding Multiple Peaks**: Detecting multiple peak points in the histogram, which could indicate that the image has been altered significantly, potentially revealing the use of steganography.

#### Input and Output

- **Input**: The analysis takes an image as input, which can either be the original image or the stego-image.
- **Output**: The output is the histogram of the input image, visualizing the distribution of pixel values. This histogram provides valuable insights into the image's characteristics.

By performing histogram analysis, we can effectively evaluate the impact of steganographic methods on the original image and assess the quality and security of the stego-image.

---

### Complexity Analysis

Complexity analysis is a method used to evaluate the security of encrypted images by examining their visual characteristics. This analysis focuses on detecting the presence of outlines or contours within the encrypted image. If prominent outlines are detected, it may indicate that the encryption method is insecure, as it can potentially reveal sensitive information about the underlying content. Conversely, a secure encryption method should produce results that appear random and chaotic.

#### Purpose

The main objectives of complexity analysis include:

- **Detecting Outlines**: Assessing the encrypted image for visible contours that could compromise the confidentiality of the information. The presence of such outlines suggests that the encryption method is not robust enough to obscure the original content.
- **Evaluating Security**: Ensuring that the output images from the encryption process exhibit a high level of complexity and randomness, which is characteristic of a secure encryption method.

#### Methodology

To effectively conduct complexity analysis, the following considerations must be taken into account:

- **Threshold Adjustment**: Manual adjustment of the threshold is required to avoid resulting images from appearing entirely black or entirely white. Setting the threshold appropriately is crucial to accurately assess the complexity of the image without losing significant details.
- **Visual Inspection**: The output images should be visually inspected to determine the presence of outlines or patterns that might indicate weaknesses in the encryption.

By performing complexity analysis, we can better understand the effectiveness of the encryption method and ensure that sensitive information remains protected from potential attacks.

