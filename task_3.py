from task_2 import logger


class FlatIterator:
    path = 'test.log'

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.external_index = 0
        self.internal_index = -1
        self.index = 0
        return self

    @logger(path)
    def __next__(self):
        self.internal_index += 1
        if self.internal_index >= len(self.list_of_list[self.external_index]):
            self.external_index += 1
            self.internal_index = 0
        if self.external_index >= len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.external_index][self.internal_index]


def test_3():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print('Тест 3-го задания пройден успешно.')

# list_of_lists_1 = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f', 'h', False],
#     [1, 2, None]
# ]
# instance = FlatIterator(list_of_lists_1)
# for elem in instance:
#     print(elem)
