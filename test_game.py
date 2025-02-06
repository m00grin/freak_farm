import subprocess

def test_run_game():
    result = subprocess.run(['python3', 'game.py'], capture_output=True, text=True)
    
    assert result.returncode == 0, f"Game.py failed with error: {result.stderr}"
