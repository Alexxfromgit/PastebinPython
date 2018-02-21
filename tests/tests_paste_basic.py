import pastebin_python
import pytest
import time

from config import api_dev_key, username, password
from pastebin_python import PastebinPython
from tools import check_paste_in_list

@pytest.fixture(scope='module')
def login_to_pastebin(request):
    pbin = PastebinPython(api_dev_key=api_dev_key)
    pbin.createAPIUserKey(username, password)

    return pbin

@pytest.mark.parametrize('paste_name',
                         ['', 'my_name', 'my name', '12345'])
def test_create_paste(login_to_pastebin, paste_name):
    time.sleep(5)

    paste_text = 'This is teest paste text.'
    print("PASTE_NAME", paste_name)
    paste_url = login_to_pastebin.createPaste(api_paste_code=paste_text, api_paste_name=paste_name)

    pastes = login_to_pastebin.listUserPastes()

    assert check_paste_in_list(pastes, paste_url) == True


def test_delete_paste(login_to_pastebin):
    paste_text = 'This is teest paste text.'
    paste_url = login_to_pastebin.createPaste(api_paste_code=paste_text, api_paste_name='test_paste')
    api_paste_key = paste_url[21:]

    # import ipdb; ipdb.set_trace()

    login_to_pastebin.deletePaste(api_paste_key)

    pastes = login_to_pastebin.listUserPastes()
    paste_was_deleted = True
    for paste in pastes:
        if paste['paste_url'] == paste_url:
            paste_was_deleted = False

    assert paste_was_deleted == True
