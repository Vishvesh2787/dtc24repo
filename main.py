import os
from utils.database import create_tables, add_initial_master_admin
from modules.login_gui import start_login_gui

# Step 1: Create required folders
required_folders = [
    'assets/barcodes',
    'assets/icons',
    'assets/sounds',
    'data/reports/daily',
    'data/reports/monthly',
    'data/logs'
]

for folder in required_folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Step 2: Setup database
create_tables()
add_initial_master_admin()

# Step 3: Start GUI Login
start_login_gui()
