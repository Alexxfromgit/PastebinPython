def check_paste_in_list(paste_list, paste_url):

    paste_was_created = False
    for paste in paste_list:
        if paste['paste_url'] == paste_url:
            return True

    return paste_was_created