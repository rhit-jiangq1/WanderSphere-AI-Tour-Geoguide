import pytest
import pandas as pd
from io import BytesIO
from unittest.mock import patch
import os
from ExcelUtils import ExcelOperations

@pytest.fixture
def mock_excel_file():
    data = {
        'Place Name': ['Place A', 'Place B', 'Place C', 'Place D', 'Place E'],
        'Image URL': ['url_A', 'url_B', 'url_C', 'url_D', 'url_E'],
        'Sentiment Score': [0.8, 0.9, 0.7, 0.5, 0.6],
        'Views': [100, 200, 150, 50, 75],
        'Comment Count': [10, 20, 15, 5, 8]
    }
    df = pd.DataFrame(data)
    
    excel_file = BytesIO()
    df.to_excel(excel_file, index=False, engine='openpyxl')
    excel_file.seek(0)
    return excel_file

@pytest.fixture
def excel_operations():
    return ExcelOperations()

def test_dataprocessing(excel_operations, mock_excel_file):
    mock_file_path = 'mock_file.xlsx'
    with open(mock_file_path, 'wb') as f:
        f.write(mock_excel_file.getvalue())

    images_info = excel_operations.dataprocessing(mock_file_path)

    assert isinstance(images_info, list)
    # 5 places in the mock data
    assert len(images_info) == 5
    # First place name
    assert images_info[0][0] == 'Place A'
    # Last place map link
    assert 'https://www.google.com/maps?q=Place+E,+New+York' in images_info[-1]

    os.remove(mock_file_path)

def test_read_flickrdata(excel_operations, mock_excel_file):

    mock_flickr_file_path = 'mock_flickr_data.xlsx'
    with open(mock_flickr_file_path, 'wb') as f:
        f.write(mock_excel_file.getvalue())

    Parent_Folder_Path = "/mock/path"
    os.makedirs(Parent_Folder_Path, exist_ok=True)

    excel_operations.read_flickrdata(mock_flickr_file_path, Parent_Folder_Path)
    top_10_images_filepath = os.path.join(Parent_Folder_Path, "top_10_images.xlsx")
    assert os.path.exists(top_10_images_filepath)

    os.remove(mock_flickr_file_path)
    os.remove(top_10_images_filepath)
    os.rmdir(Parent_Folder_Path)

def test_invalid_excel_file(excel_operations):
    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.side_effect = Exception("File not found")
        error_status = excel_operations.read_flickrdata('invalid_file.xlsx', '/mock/path')
        assert error_status == 'Error Occured'
