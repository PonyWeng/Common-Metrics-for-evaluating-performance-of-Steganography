# Common-Metrics-for-evaluating-performance-of-Steganography

In this project, we collect lots of evaluation metrics or tools for evaluating the performance of Steganography methods or information hiding techniques.

Some of metrics are provided:

* PSNR

$$
\text{PSNR} = 10 \cdot \log_{10} \left( \frac{{\text{MAX}^2}}{{\text{MSE}}} \right)
$$

$$
\text{MSE} = \frac{1}{mn} \sum_{i=0}^{m-1} \sum_{j=0}^{n-1} \left[ I(i,j) - K(i,j) \right]^2
$$


* SSIM

$$
\text{SSIM}(x, y) = \frac{(2 \mu_x \mu_y + C_1)(2 \sigma_{xy} + C_2)}{(\mu_x^2 + \mu_y^2 + C_1)(\sigma_x^2 + \sigma_y^2 + C_2)}
$$

* Information Entropy

$$
H = - \sum_{i=0}^{L-1} p_i \cdot \log_2(p_i)
$$

## Some of analysis tools:

* Histogram Analysis

* Complexity Analysis
