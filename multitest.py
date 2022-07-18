import pytest
@pytest.fixture
def input_data():
    total=100
    return total


import pytest
def test_total_by_5(input_data):
    assert input_data %5==0
def test_total_by_10(input_data):
    assert input_data %10==0


#print(df.loc[(df['wetBulbMax'] < 60) & (df['Gender'] == "Female")].count())