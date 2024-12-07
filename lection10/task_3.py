# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('params', [pytest.param((21, 7, 3), marks=pytest.mark.smoke),
                                    pytest.param((108, -2, -54), marks=pytest.mark.acceptance),
                                    pytest.param((200, 2, 4, 5, 5), marks=pytest.mark.acceptance),
                                    pytest.param((7, 2.5, 2.8), marks=pytest.mark.acceptance),
                                    pytest.param((10, 0, None), marks=pytest.mark.acceptance)])
def test_divided(params):
    numbers, result = params[:-1], params[-1]
    try:
        assert all_division(*numbers) == result
    except ZeroDivisionError:
        assert result is None
