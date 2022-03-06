from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Edit Group", header="Edit Header", footer="Edit GroupFooter"))
    app.session.logout()


def test_edit_first_group_to_empty_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="", header="", footer=""))
    app.session.logout()


def test_edit_group_name_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Edit Group"))
    app.session.logout()
