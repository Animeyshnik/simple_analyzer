source ../.venv/bin/activate
nohup python3 ../simple_analyzer/main.py > output.log 2>&1 &
echo "Program started in background. Check output.log"
