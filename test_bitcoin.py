import unittest 
from unittest import TestCase
from unittest.mock import patch 

import bitcoin

class TestExchangeRates(TestCase):

    @patch('builtins.input', side_effect=['2'])
    def test_valid_user_input(self, mock_input):
        example = bitcoin.user_input()
        self.assertEqual(2, example)

    @patch('bitcoin.api_call')
    def test_dollars_to_bitcoin(self, mock_bitcoin_api):
        mock_bitcoin = 1
        a = mock_bitcoin_api.return_value = {"time":{"updated":"Nov 19, 2020 22:00:00 UTC",
            "updatedISO":"2020-11-19T22:00:00+00:00",
            "updateduk":"Nov 19, 2020 at 22:00 GMT"},
            "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin",
            "bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"17,962.7805","description":"United States Dollar","rate_float":17962.7805},
            "GBP":{"code":"GBP","symbol":"&pound;","rate":"13,532.0990","description":"British Pound Sterling","rate_float":13532.099},
            "EUR":{"code":"EUR","symbol":"&euro;","rate":"15,121.6075","description":"Euro","rate_float":15121.6075}}}
        
        expected_dollars = 17962.7805
        dollars = bitcoin.get_exchange_rate(a, 1)
        self.assertEqual(expected_dollars, dollars)
        
        #mock_bitcoin_call.return_value = example_api_response
        #converted = bitcoin.get_exchange_rate(1, mock_bitcoin)
        #expected = 144876.19150000002
        #self.assertAlmostEqual(expected, converted)


    @patch('builtins.print')
    def test_display_total(self, mock_print):
        bitcoin.display_exchange_rate(123, 123)
        mock_print.assert_called_once_with( '123 Bitcoin is equivalent to $123')

if __name__ == '__main__':
    unittest.main()