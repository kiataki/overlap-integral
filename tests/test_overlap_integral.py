import numpy as np
import pytest
from overlap_integral.overlap_integral import OverlapIntegral


@pytest.fixture
def overlap_integral_instance():
    return OverlapIntegral()

def test_overlap_integral(overlap_integral_instance):
    np.random.seed(3)  
    
    data1 = np.random.normal(loc=30, scale=1, size=1000)
    data2 = np.random.normal(loc=30, scale=1.2, size=1000)

    function_type = "kde"
    pdf_1 = overlap_integral_instance.get_pdf(data1, pdf_type=function_type)
    pdf_2 = overlap_integral_instance.get_pdf(data2, pdf_type=function_type)

    lower_limit = min(np.min(data1), np.min(data2)) - 12 * max(np.std(data1), np.std(data2))
    upper_limit = max(np.max(data1), np.max(data2)) + 12 * max(np.std(data1), np.std(data2))

    integral, error = overlap_integral_instance.overlap_integral(pdf_1, pdf_2, lower_limit, upper_limit)

    assert 0 <= integral <= 1, "The integral value should be between 0 and 1"
    assert error >= 0, "The error value should be non-negative"
    assert isinstance(integral, float), "The integral must be a float"
    assert isinstance(error, float), "The error must be a float"

