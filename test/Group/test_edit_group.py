from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Edit Group", header="Edit Header", footer="Edit GroupFooter"))


def test_edit_first_group_to_empty_name(app):
    app.group.edit_first_group(Group(name="", header="", footer=""))


def test_edit_group_name_first_group(app):
    app.group.edit_first_group(Group(name="Edit ONLY Group name"))


def test_edit_group_header_first_group(app):
    app.group.edit_first_group(Group(header="Edit ONLY Group Header"))


def test_edit_group_footer_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='group is not created'))
    app.group.edit_first_group(Group(footer="Edit ONLY Group Footer"))
