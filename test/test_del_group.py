def test_delete_first_group1(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()
