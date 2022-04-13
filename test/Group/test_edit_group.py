from model.group import Group
from random import randrange
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10), ""]
    for header in ["", random_string("header", 20), random_string("header", 20)]
    for footer in ["", random_string("footer", 20), random_string("footer", 20)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_edit_some_group(app, db, group, check_ui):
    groups_before_edit = db.get_group_list()
    index = randrange(len(groups_before_edit))
    group_id_to_edit = groups_before_edit[index].id
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    app.group.edit_group_by_id(group_id_to_edit, group)
    groups_after_edit = db.get_group_list()
    assert len(groups_before_edit) == len(groups_after_edit)
    groups_before_edit[index] = group
    assert sorted(groups_before_edit, key=Group.id_or_max) == sorted(groups_after_edit, key=Group.id_or_max)
    if check_ui:
        assert sorted(groups_after_edit, key=Group.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Group.id_or_max)

