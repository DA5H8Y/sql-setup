# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
python3 -m pip install --upgrade pip
python3 -m pip --version
python3 -m pip install -r requirements.txt

# Deactivate virtual environment
deactivate