import unittest 
from unittest import TestCase
from unittest.mock import patch, call

import timesheets

class TestTimeSheet(TestCase):

    """ mock input() and force it to return a value """

    @patch('builtins.input', side_effect=['2'])
    def test_get_hours_for_day(self, mock_input):
        hours = timesheets.get_hours_for_day('Tuesday')
        self.assertEqual(2, hours)

    @patch('builtins.input', side_effect=['dog','2', '', 'fish', '765cat', 'coffee290'])
    def test_get_hours_for_day_non_numeric_rejected(self, mock_input):
        hours = timesheets.get_hours_for_day('Tuesday')
        self.assertEqual(2, hours)

    #@patch('builtins.input', side_effect=['-25, 5, -1000'])
    #def test_get_hours_for_day_hours_greater_then_zero(self, mock_input):
        #hours = timesheets.get_hours_for_day('Tuesday')
        #self.assertEqual(5, hours)

    #@patch('builtins.input', side_effect=['24.00001, 6, 1000', '25'])
    #def test_get_hours_for_day_hours_less_than_24(self, mock_input):
        #hours = timesheets.get_hours_for_day('Tuesday')
        #self.assertEqual(6, hours)

    @patch('builtins.print')
    def test_display_total(self, mock_print):
        timesheets.display_total(123)
        mock_print.assert_called_once_with('Total hours worked: 123')

    @patch('timesheets.alert')
    def test_alert_meet_min_hours_doesnt_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(12, 30)
        mock_alert.assert_called_once()

    @patch('timesheets.alert')
    def test_alert_meet_min_hours_does_meet_min(self, mock_alert):
        timesheets.alert_not_meet_min_hours(40, 30)
        mock_alert.assert_not_called()

    @patch('timesheets.get_hours_for_day')
    def test_get_hours(self, mock_get_hours):
        mock_hours = [2, 3, 8]
        mock_get_hours.side_effect = mock_hours
        days = ['m', 't', 'w']
        expected_hours = dict(zip(days, mock_hours)) # {'m': 2, 't': 3, 'w': 8}
        hours = timesheets.get_hours(days)
        self.assertEqual(expected_hours, hours)

    @patch('builtins.print')
    def test_display_hours(self, mock_print):

        # arrange
        example = {'m': 2, 't': 3, 'w': 8}
        expected_table_calls = [
            call('Day            Hours Worked   '),
            call('m              2              '),
            call('t              3              '),
            call('w              8              ')
            ]
        # action
        timesheets.display_hours(example)
        # assert
        mock_print.assert_has_calls(expected_table_calls)

    def test_total_hours(self):    
        example = {'m': 2, 't': 3, 'w': 8}
        total = timesheets.total_hours(example)
        expected_total = 2 + 3 + 8
        self.assertEqual(total, expected_total)
        
if __name__ == '__main__':
    unittest.main()