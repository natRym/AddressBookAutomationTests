# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group1", header="groupHeader1", footer="GroupFooter1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()


def test_add_group_with_long_name(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group
                     (name="group1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test tes",
                      header="Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)",
                      footer="Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)"))
    app.session.logout()