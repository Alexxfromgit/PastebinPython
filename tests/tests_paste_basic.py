import pastebin_python
import pytest
import os

from pastebin_python import PastebinPython


@pytest.fixture(scope='module')
def login_to_pastebin(request):
    api_dev_key = os.environ.get('PASTE_API_KEY')
    username = os.environ.get('PASTE_USERNAME')
    password = os.environ.get('PASTE_PASSWORD')

    pbin = PastebinPython(api_dev_key=api_dev_key)
    pbin.createAPIUserKey(username, password)

    return pbin


def test_version():
    assert pastebin_python.__version__ == '1.2'


# def test_listUserPastes(login_to_pastebin):
#     assert len(login_to_pastebin.listUserPastes()) == 3


def test_create_paste(login_to_pastebin):
    paste_text = 'This is teest paste text.'

    paste_url = login_to_pastebin.createPaste(api_paste_code=paste_text, api_paste_name='test_paste')

    pastes = login_to_pastebin.listUserPastes()
    paste_was_created = False
    for paste in pastes:
        if paste['paste_url'] == paste_url:
            paste_was_created = True

    assert paste_was_created == True


def test_delete_paste(login_to_pastebin):
    paste_text = 'This is teest paste text.'
    paste_url = login_to_pastebin.createPaste(api_paste_code=paste_text, api_paste_name='test_paste')
    api_paste_key = paste_url[21:]

    import ipdb; ipdb.set_trace()

    login_to_pastebin.deletePaste(api_paste_key)

    pastes = login_to_pastebin.listUserPastes()
    paste_was_deleted = True
    for paste in pastes:
        if paste['paste_url'] == paste_url:
            paste_was_deleted = False

    assert paste_was_deleted == True
