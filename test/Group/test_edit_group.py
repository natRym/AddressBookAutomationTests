from model.group import Group
from random import randrange


def test_edit_some_group(app):
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


# def test_edit_first_group_to_empty_name(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     group.id = old_groups[0].id
#     if app.group.count() == 0:
#         app.group.create(Group(name='group is not created'))
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
#
# def test_edit_group_name_first_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="Edit ONLY Group name")
#     group.id = old_groups[0].id
#     if app.group.count() == 0:
#         app.group.create(Group(name='group is not created'))
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header_first_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(header="Edit ONLY Group Header")
#     group.id = old_groups[0].id
#     if app.group.count() == 0:
#         app.group.create(Group(name='group is not created'))
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_footer_first_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(footer="Edit ONLY Group Footer")
#     group.id = old_groups[0].id
#     if app.group.count() == 0:
#         app.group.create(Group(name='group is not created'))
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

