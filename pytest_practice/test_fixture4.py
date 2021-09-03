import logging
import pytest
logger = logging.getLogger(__file__)

test_data = [("3+5", 8), ("2+4", 6), ("6*9", 54)]


@pytest.fixture(scope='function', autouse=True)
def setup_and_teardown(test_input, expected):
    logger.info("setup")
    logger.info('Parameters: %s=%s' % (test_input, expected))
    assert eval(test_input) != 6
    yield test_input, 90
    logger.info(expected)
    logger.info("teardown")


@pytest.mark.parametrize("test_input,expected", test_data)
def test_eval(setup_and_teardown):
    test_input, expected = setup_and_teardown
    assert eval(test_input) == expected
    logger.info("*************************************")



# import pytest
#
# @pytest.fixture
# def one():
#     return 1
#
#
# @pytest.fixture
# def two():
#     return 2
#
#
# @pytest.fixture(params=[
#     pytest.lazy_fixture('one'),
#     pytest.lazy_fixture('two')
# ])
# def some(request):
#     return request.param
#
#
# def test_func(some):
#     assert some in [1, 2]