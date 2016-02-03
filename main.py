
class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def set_up(self):
        self.log = "setUp "

    def tear_down(self):
        self.log = self.log + 'tearDown'

    def test_method(self):
        self.log = self.log + "test_method "


class TestCaseTest(TestCase):

    def test_template_method(self):
        self.test = WasRun('test_method')
        self.test.run()
        assert self.test.log == "setUp test_method tearDown"


if __name__ == '__main__':
    TestCaseTest("test_template_method").run()
