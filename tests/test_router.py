from ..kettle.application import Application


class TestRouterRegister:

    def test_match_path_and_regsiter_path(self):
        self.application = Application()
        test_func = lambda x: x
        for method in ['POST', 'GET', 'PUT', 'PATCH']:
            self.application.router.register(method, '/hams/:ham_id/', test_func)
            view, action = self.application.router.search(method, '/hams/1/')
            assert view == test_func
            assert action == dict(ham_id='1')
