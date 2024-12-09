import pytest
from brute import Brute
from unittest.mock import Mock, patch

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():
    def describe_init():
        def test_if_data_members_are_set_not_equal_to_string():
            string = "hello"
            b = Brute('hello')
            assert string != b.target

        @patch("brute.Brute.hash")
        def test_init_calls_hash(mock_hash):
            mock_hash.return_value = "mocked_hash"
            b = Brute("test")
            mock_hash.assert_called_once_with("test")
            assert b.target == "mocked_hash"

    def describe_hash():
        def test_if_hash_hashes_and_affects_data_members():
            string = "hello"
            b = Brute(string)
            test_sting = "hash this"
            hashed = b.hash(test_sting)
            assert test_sting != hashed
    def describe_randomGuess():
        def test_if_the_return_value_is_random():
            b = Brute("jeff")
            random_string1 = b.randomGuess()
            random_string2 = b.randomGuess()
            assert random_string1 != random_string2
    def describe_BruteOnce():
        def test_with_correct_attempt():
            b = Brute("jeff")
            vaild = b.bruteOnce("jeff")
            assert vaild == True
        def test_with_Incorrect_attempt():
            b = Brute("jeff")
            vaild = b.bruteOnce("hehhe")
            assert vaild == False
        
        @patch("brute.Brute.hash")
        def test_bruteOnce_calls_hash(mock_hash):
            mock_hash.return_value = "mocked_hash"
            b = Brute("test")
            valid = b.bruteOnce("hehe")
            mock_hash.assert_called_with("hehe")
    def describe_bruteMany():
        @patch("brute.Brute.bruteOnce")
        def test_bruteMany_terminates_on_success(mock_bruteOnce):
            mock_bruteOnce.side_effect = [False, False, True]
            b = Brute("test")
            result = b.bruteMany(limit=3)
            assert result > 0 
            assert mock_bruteOnce.call_count == 3

        @patch("brute.Brute.randomGuess")
        @patch("brute.Brute.bruteOnce")
        def test_bruteMany_calls_randomGuess(mock_bruteOnce, mock_randomGuess):
            mock_bruteOnce.return_value = False
            mock_randomGuess.return_value = "random_guess"
            b = Brute("test")
            b.bruteMany(limit=2)
            assert mock_randomGuess.call_count == 2
            assert mock_bruteOnce.call_count == 2
            mock_bruteOnce.assert_called_with("random_guess")

#hope this is enough to get full criedit on the final Jeffy 
