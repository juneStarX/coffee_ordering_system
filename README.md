

RUN YOUR APP IN A VIRTUAL ENVIRONMENT
1. Open VS Code
2. Open the project directory coffee_ordering_system
3. Open the Terminal
4. Creating a virtual environment: python -m venv cos_venv
5. Select your python interpreter
6. Activating a virtual environment (macOS/Linux): source cos_venv/bin/activate
    - Once activated, your terminal will display the virtual environment name in parenthesis (cos_venv) before your usual terminal prompt.
7. Install Dependencies: pip install -r requirements.txt
8. Run the Flask application using: python run.py (It will load the development environment by default.)
    - By default, Flask runs the server on 127.0.0.1 (localhost) and port 5000.

VIRTUAL ENVIRONMENT - MISC.
1. (Optional) Freeze or update dependencies file requirements.txt using: pip freeze > requirements.txt
2. (Optional) Deactivate the virtual environment when you are done running the app: deactivate

RUN TESTS USING PYTEST (UNIT & FUNCTIONAL TESTING)
RUN YOUR APP IN A VIRTUAL ENVIRONMENT
1. Open VS Code
2. Open the project directory coffee_ordering_system
3. Open the Terminal
4. Activate virtual environment (macOS/Linux): source cos_venv/bin/activate
    - Once activated, your terminal will display the virtual environment name in parenthesis (cos_venv) before your usual terminal prompt.
5. On the terminal prompt run: pytest 
6. On the terminal prompt run a specific test file: pytest tests/test_home.py
7. Deactivate your virtual environment: deactivate
