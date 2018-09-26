from collections import namedtuple
from typing import List

Row = namedtuple('Row', ['id', 'name', 'pattern'])


def print_row(row_: Row):
    print('id: {}, name: {}, pattern: {}'.format(row_.id, row_.name, row_.pattern))


def draw_list(l: List[Row]):
    largest_id = Row('', '', '')
    largest_name = Row('', '', '')
    largest_pattern = Row('', '', '')

    largest_rows = {
        'id': None,
        'name': None,
        'pattern': None
    }

    largest_attr_name = ''
    largest_attr_val = 0

    for key in largest_rows.keys():
        if largest_attr_val < len(key):
            largest_attr_name = key
            largest_attr_val = len(key)

    for row in l:
        if len(largest_id.id) < len(row.id):
            largest_id = row
            largest_rows['id'] = largest_id
        if len(largest_name.name) < len(row.name):
            largest_name = row
            largest_rows['name'] = largest_name
        if len(largest_pattern.pattern) < len(row.pattern):
            largest_pattern = row
            largest_rows['pattern'] = largest_pattern

    largest_attr_row_val = ''
    largest_attr_row_name = 'id'
    largest_attr_row_count = 0
    for k, v in largest_rows.items():
        if len(getattr(v, k)) > largest_attr_row_count:
            largest_attr_row_val = v
            largest_attr_row_name = k
            largest_attr_row_count = len(getattr(v, k))

    largest_row = largest_rows[largest_attr_row_name]
    print_row(largest_row)
    print(largest_attr_val)
    name_width = largest_attr_val if largest_attr_val > 4 else 4
    value_width = largest_attr_row_count if largest_attr_row_count > 4 else 4

    print('{Name: <{name_width}}|{Value: <{value_width}}'.format(name='Name',
                                                                 name_width=name_width-4,
                                                                 value='Value',
                                                                 value_width=value_width-4))


if __name__ == '__main__':
    rows = [
        Row(id='13802380948209480397823978397548930', name='my_name', pattern='pattern'),
        Row(id='1', name='my_ndkfdpkdspoame', pattern='my_pattern')
    ]
    draw_list(rows)
