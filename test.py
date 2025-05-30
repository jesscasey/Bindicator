import unittest
from unittest.mock import patch, mock_open, MagicMock
import main

class TestBindicator(unittest.TestCase):
    # Simulate dependencies
    @patch("builtins.open", new_callable=mock_open, 
           read_data="AB1,foo,CouncilX\n")
    @patch("main.next_bin_day")
    def test_find_council_found(self, mock_next_bin_day, mock_filey):
        postcode = "AB1"
        with patch("builtins.print") as mock_print:
            main.find_council(postcode)
            mock_print.assert_any_call(
                "The local authority for AB1 is CouncilX."
                )
            mock_next_bin_day.assert_called_with("AB1", "CouncilX")

    @patch("builtins.open", new_callable=mock_open, 
           read_data="AB1,foo,CouncilX\n")
    def test_find_council_not_found(self, mock_file):
        postcode = "ZZ9"
        with patch("builtins.print") as mock_print:
            main.find_council(postcode)
            mock_print.assert_any_call("Postcode not found.")

    @patch("builtins.open", new_callable=mock_open, 
           read_data="CouncilX,http://example.com\n")
    @patch("main.driver")
    def test_next_bin_day_council_found(self, mock_driver, mock_file):
        mock_driver.get = MagicMock()
        mock_driver.find_element.return_value = MagicMock()
        # Simulate Select and dropdown
        with patch("main.Select") as mock_select:
            mock_select.return_value.options = [MagicMock(
                text="1 High Street"
                )]
            mock_select.return_value.select_by_visible_text = MagicMock()
            mock_select.return_value.submit = MagicMock()
            # Simulate input and print
            with patch("builtins.input", return_value="1 High Street"):
                with patch("builtins.print") as mock_print:
                    # Simulate finding elements for dates
                    mock_elem = MagicMock()
                    mock_elem.find_element.return_value.text = "2025-01-01"
                    mock_driver.find_element.side_effect = [MagicMock(), 
                                                            mock_elem, 
                                                            MagicMock(), 
                                                            mock_elem]
                    main.next_bin_day("AB1", "CouncilX")
                    self.assertTrue(mock_print.called)

    @patch("builtins.open", new_callable=mock_open, 
           read_data="CouncilX,http://example.com\n")
    @patch("main.driver")
    def test_next_bin_day_council_not_found(self, mock_driver, mock_file):
        with patch("builtins.print") as mock_print:
            main.next_bin_day("ZZ9", "CouncilY")
            mock_print.assert_any_call(
                "Bin collection information for CouncilY could not be found."
                )

if __name__ == "__main__":
    unittest.main()
    print(unittest.TestResult.failures) # Print which (if any) tests failed
