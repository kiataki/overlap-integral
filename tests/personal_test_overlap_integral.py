
import numpy as np
from overlap_integral.overlap_integral import OverlapIntegral

import plotly.io as pio
pio.kaleido.scope.default_format = "png"


def main():
    np.random.seed(3)  # Set random seed for reproducibility

    overlap_integral_instance = OverlapIntegral()

    # Generate or load data
    data1 = np.random.normal(loc=10, scale=1, size=1000)
    data2 = np.random.normal(loc=10, scale=2, size=1000)

    # Choose PDF method: 'kde' or 'gaussian'
    function_type = 'kde'

    # Get PDFs
    pdf_1 = overlap_integral_instance.get_pdf(data1, pdf_type=function_type)
    pdf_2 = overlap_integral_instance.get_pdf(data2, pdf_type=function_type)

    # Calculate overlap integral
    lower_limit = min(np.min(data1), np.min(data2)) - 12 * max(np.std(data1), np.std(data2))
    upper_limit = max(np.max(data1), np.max(data2)) + 12 * max(np.std(data1), np.std(data2))
    integral, error = overlap_integral_instance.overlap_integral(pdf_1, pdf_2, lower_limit, upper_limit)

    print(f"Overlap integral: {integral}")
    print(f"Estimated error: {error}")

    # Plot distributions
    fig = overlap_integral_instance.plot_distributions(pdf_1, pdf_2, integral, error, x_range=(lower_limit, upper_limit))
    fig.write_image("overlap_plot.png")
    #fig.show()

    print(f"Everything worked!")

if __name__ == '__main__':
    main()