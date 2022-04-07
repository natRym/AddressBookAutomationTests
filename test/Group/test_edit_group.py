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
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_data = Group(name="Edit Group", header="Edit Header", footer="Edit GroupFooter")
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    app.group.edit_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
