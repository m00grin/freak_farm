import pytest
from unittest.mock import patch
import game

def test_main_menu():
    with patch("builtins.input", side_effect=["1", "q"]):
        game.main_menu()
