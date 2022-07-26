import pytest
from playwright.sync_api import Page


def test_example(page: Page):
    page.goto("http://www.baidu.com")
    assert page.title() == "百度一下，你就知道"

    page.close()


if __name__ == '__main__':
    pytest.main(["-v", "te_example_pytest.py"])