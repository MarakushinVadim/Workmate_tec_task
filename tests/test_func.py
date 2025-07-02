from utils.func import where_filter, aggregate_filter, read_csv

data = read_csv('test_data.csv')


def test_read_csv():
    assert read_csv('test_data.csv') == [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'},
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'}
    ]


def test_where_filter():
    assert where_filter('price=199', data) == [
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'}]
    assert where_filter('price>199', data) == [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'galaxy s23 ultra', 'brand': 'samsung', 'price': '1199', 'rating': '4.8'}]
    assert where_filter('price<1000', data) == [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'},
        {'name': 'redmi note 12', 'brand': 'xiaomi', 'price': '199', 'rating': '4.6'}]
    assert where_filter('brand=apple', data) == [
        {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'}]
    assert where_filter('brand>apple', data) == []
    assert where_filter('brand<apple', data) == []


def test_aggregate_filter():
    assert aggregate_filter('price=min', data) == [{'min': 199.0}]
    assert aggregate_filter('price=max', data) == [{'max': 1199.0}]
    assert aggregate_filter('price=avg', data) == [{'avg': 799.0}]
    assert aggregate_filter('brand=avg', data) == []
    assert aggregate_filter('price=342', data) == []
