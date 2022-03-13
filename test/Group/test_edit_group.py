from model.group import Group


def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='group is not created'))
    app.group.edit_first_group(Group(name="Edit Group", header="Edit Header", footer="Edit GroupFooter"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_group_to_empty_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='group is not created'))
    app.group.edit_first_group(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_name_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='group is not created'))
    app.group.edit_first_group(Group(name="Edit ONLY Group name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='group is not created'))
    app.group.edit_first_group(Group(header="Edit ONLY Group Header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_footer_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='group is not created'))
    app.group.edit_first_group(Group(footer="Edit ONLY Group Footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
