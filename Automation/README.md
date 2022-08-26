# pytest-BDD
pytest-BDD with python and selenium

pip install -r requirement.txt

Please go to Automation dir and fire below mentioned commands

run cmd = pytest Tests/Web/step_defs/test_Scenario.py

run cmd = pytest Tests/Web/step_defs/test_Scenarios.py

run cmd = pytest Tests/Web/step_defs/test_ScenarioOutline.py
  
run cmd = pytest -m sanity Tests/Web/step_defs/test_Scenario.py

run cmd = pytest -m regression Tests/Web/step_defs/test_Scenario.py

run cmd = pytest -v -s  -m regression Tests/Web/step_defs/test_Scenario.py --html-report=./Reports/reports.html

run cmd = pytest -v -s  -m sanity Tests/Web/step_defs/test_Scenario.py --html-report=./Reports/reports.html

:)
