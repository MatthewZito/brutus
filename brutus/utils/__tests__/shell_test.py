import unittest
from os import path

from ..exceptions import ScriptFailed
from ..shell import invoke_script

FIXTURES = path.abspath(path.join(path.dirname(__file__), "fixtures"))


def fixture(p: str) -> str:
    return path.join(FIXTURES, p)


class TestShellUtils(unittest.TestCase):
    """
    Test shell utilities
    """

    def test_invoke_script_ok(self):
        try:
            invoke_script(script=fixture('exit_with.bash'), args='0', autoresolve=False)
        except BaseException:
            self.fail('invoke_script raised an unexpected exception')

    def test_invoke_script_nonexistent_file(self):
        """
        Test: invoking a non-existent script raises a `FileNotFoundError`
        """
        with self.assertRaises(FileNotFoundError):
            invoke_script('noexist')

    def test_invoke_script_shellfail(self):
        """
        Test: invoking a script that returns a non-zero exit code should result in
        a `ScriptFailed` exception being raised
        """
        with self.assertRaises(ScriptFailed):
            invoke_script(script=fixture('exit_with.bash'), args='1', autoresolve=False)


if __name__ == '__main__':
    unittest.main()
