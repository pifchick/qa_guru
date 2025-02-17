from selene import browser, query


def test_poisk(browser_conf):
    browser.open('https://ya.ru/')
    browser.element('.search3__inner .search3__input').click()
    browser.element('.search3__inner .search3__input').type('jdncpsisnvmipfovmnepgobvegirob').press_enter()
    text2 = browser.element('.RequestMeta-Level_type_error .RequestMeta-Message').get(query.text)
    assert text2 == 'По вашему запросу ничего не нашлось'

def test_git_commits():
    pass
