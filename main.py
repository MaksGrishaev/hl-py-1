def parse(query: str) -> dict:
    result_dict = {}
    if query.find('?') == -1:
        return result_dict

    data_list = query.split('?')[1].split('&') if query.find('&') != -1 else query.split('?')[1].split('\n')

    for dict_item in data_list:
        if len(dict_item) > 0 \
                and dict_item.count('=') == 1 \
                and len(dict_item[0:dict_item.find('='):]) > 1 \
                and len(dict_item[dict_item.find('=') + 1::]) > 1:
            result_dict[dict_item.split('=')[0]] = dict_item.split('=')[1]
    return result_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('https://example.com/path/to/page?name==ferret&color=purple') == {'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=pur=ple') == {'name': 'ferret'}
    assert parse('https://example.com/path/to/page?nameferret&color=purple') == {'color': 'purple'}
    assert parse('http://example.com/??') == {}
    assert parse('http://example.com/?name=Dima=Vasya') == {}
    assert parse('https://example.com/path/to/page?name=ferret&&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/?name=') == {}
    assert parse('https://example.com/path/to/page?name=&color=purple') == {'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=&color=') == {}
    assert parse('https://example.com/path/to/page?name=ferret&color=') == {'name': 'ferret'}


# def parse_cookie(query: str) -> dict:
#     if len(query) == 0 or query.count(';') == 0 or query.count('=') == 0:
#         return {}
#     result_dict = {}
#     data_list = query.split(';')
#     for dict_item in data_list:
#         if len(dict_item) != 0 and dict_item.count('=') > 0:
#             result_dict[dict_item.split('=')[0]] = dict_item[dict_item.find('=') + 1::]
#     return result_dict
#
#
# if __name__ == '__main__':
#     assert parse_cookie('name=Dima;') == {'name': 'Dima'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
#     assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
