
import numpy as np
from overlap_integral.overlap_integral import OverlapIntegral

import plotly.io as pio
pio.kaleido.scope.default_format = "png"


def main():
    np.random.seed(3)  # Set random seed for reproducibility

    metrics = OverlapIntegral()

    # Generate or load data
    data1 = np.random.normal(loc=60, scale=1, size=1000)
    data2 = np.random.normal(loc=65, scale=1.5, size=1000)

    # Choose PDF method: 'kde' or 'gaussian'
    pdf_method = 'kde'

    # Get PDFs
    pdf_1 = metrics.get_pdf(data1, method=pdf_method)
    pdf_2 = metrics.get_pdf(data2, method=pdf_method)

    # Calculate overlap integral
    lower_limit = min(np.min(data1), np.min(data2)) - 2
    upper_limit = max(np.max(data1), np.max(data2))
    integral, error = metrics.overlap_integral(pdf_1, pdf_2, lower_limit, upper_limit)

    print(f"Overlap integral: {integral}")
    print(f"Estimated error: {error}")

    # Plot distributions
    fig = metrics.plot_distributions(pdf_1, pdf_2, integral, error, x_range=(lower_limit, upper_limit))
    fig.write_image("overlap_plot.png")
    ##fig.show()

if __name__ == '__main__':
    main()