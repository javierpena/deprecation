import unittest2

import deprecation

__version__ = "1.5"


@deprecation.deprecated(deprecated_in="1.0", removed_in="2.0",
                        current_version=__version__,
                        details="Use the ``one`` function instead")
def won():
    """This function returns 1"""
    # Oops, it's one, not won. Let's deprecate this and get it right.
    return 1


def one():
    """This function returns 1"""
    return 1


@deprecation.deprecated(deprecated_in="1.0", removed_in="1.5",
                        current_version=__version__,
                        details="Why would you ever do this anyway?")
def why():
    """This isn't necessary"""
    return None


class Tests(unittest2.TestCase):

    @deprecation.fail_if_not_removed
    def test_won(self):
        self.assertEqual(1, won())

    @deprecation.fail_if_not_removed
    def test_why(self):
        self.assertIsNone(why())

    def test_one(self):
        self.assertEqual(1, one())
