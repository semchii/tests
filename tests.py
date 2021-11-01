from unittest import TestCase, main
from first_task import first_task


class FirstTaskTest (TestCase):

    def test_one (self):
        self.assertEqual(first_task('abcd efgh'), 'dcba hgfe')


if __name__ == '__main__':
    main()
