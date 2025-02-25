
import numpy as np
from overlap_integral.overlap_integral import OverlapIntegral

import plotly.io as pio
pio.kaleido.scope.default_format = "png"


def main():
    np.random.seed(3)  # Set random seed for reproducibility

    metrics = OverlapIntegral()

    # Generate or load data
    data1 = np.random.normal(loc=30, scale=1, size=1000)
    data2 = np.random.normal(loc=30, scale=1.2, size=1000)

    # Choose PDF method: 'kde' or 'gaussian'
    pdf_method = 'gaussian'

    # Get PDFs
    pdf_1 = metrics.get_pdf(data1, method=pdf_method)
    pdf_2 = metrics.get_pdf(data2, method=pdf_method)

    # Calculate overlap integral
    lower_limit = min(np.min(data1), np.min(data2)) - 12 * max(np.std(data1), np.std(data2))
    upper_limit = max(np.max(data1), np.max(data2)) + 12 * max(np.std(data1), np.std(data2))
    integral, error = metrics.overlap_integral(pdf_1, pdf_2, lower_limit, upper_limit)

    print(f"Overlap integral: {integral}")
    print(f"Estimated error: {error}")

    # Plot distributions
    fig = metrics.plot_distributions(pdf_1, pdf_2, integral, error, x_range=(lower_limit, upper_limit))
    fig.write_image("overlap_plot.png")
    ##fig.show()

if __name__ == '__main__':
    main()