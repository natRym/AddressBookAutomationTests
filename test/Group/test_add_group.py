# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="group1", header="groupHeader1", footer="GroupFooter1")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group_with_long_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="group1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 "
                           "test testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test "
                           "testgroup1 test testgroup1 test testgroup1 test testgroup1 test testgroup1 test tes",
                      header="Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)Group header header header header header header (Logo)",
                      footer="Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)Group footer (Comment)")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
