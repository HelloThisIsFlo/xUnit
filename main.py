
class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)
        self.wasRun = None

    def test_method(self):
        self.wasRun = 1


class TestTestCase(TestCase):
    def test_running(self):
        test = WasRun("test_method")
        assert not test.wasRun
        test.run()
        assert test.wasRun
        print("Test passed")


if __name__ == '__main__':
    TestTestCase("test_running").run()
