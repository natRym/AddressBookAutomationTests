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
def test_edit_some_group(app, group):
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Edit Group", header="Edit Header", footer="Edit GroupFooter")
    group.id = old_groups[index].id
    if app.group.count() == 0:
        app.group.create(Group(name='group is not created'))
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
