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


* Structural Similarity Index Measure (SSIM)

- **\( \text{SSIM}(x, y) \)**: The SSIM value between two images \( x \) and \( y \).
- **\( \mu_x \) and \( \mu_y \)**: The mean intensity values of images \( x \) and \( y \), respectively.
- **\( \sigma_x^2 \) and \( \sigma_y^2 \)**: The variances of images \( x \) and \( y \), respectively.
- **\( \sigma_{xy} \)**: The covariance between images \( x \) and \( y \).

### Structural Similarity Index Measure (SSIM)

- **SSIM(x, y)**: The SSIM value between two images \( x \) and \( y \).
- **\( \mu_x \) and \( \mu_y \)**: The mean intensity values of images \( x \) and \( y \), respectively.
- **\( \sigma_x^2 \) and \( \sigma_y^2 \)**: The variances of images \( x \) and \( y \), respectively.
- **\( \sigma_{xy} \)**: The covariance between images \( x \) and \( y \).

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


* Information Entropy

$$
H = - \sum_{i=0}^{L-1} p_i \cdot \log_2(p_i)
$$

### Image Entropy for Grayscale Images

- **\( H \)**: The image entropy.
- **\( L \)**: The number of gray levels in the grayscale image (usually, \( L = 256 \)).
- **\( p_i \)**: The probability of occurrence of the \( i \)-th gray level, which is the proportion of pixels having the \( i \)-th gray value in the entire image:

  $$
  p_i = \frac{n_i}{N}
  $$

- **\( n_i \)**: The number of pixels having the \( i \)-th gray value.
- **\( N \)**: The total number of pixels in the image.

Entropy measures the uncertainty or information content of the pixel distribution in an image. When all gray levels have an equal probability of occurrence (i.e., the image has maximum uncertainty), the entropy value is maximized.



## Some of analysis tools:

* Histogram Analysis

* Complexity Analysis
