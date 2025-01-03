# Define variables
PYTHON_GEN := python3
PIP := pip3
PROJECT_NAME := [Tutorial] Automation Testing using Selenium Python

.PHONY: install
install:
	$(PIP) install -r requirements.txt
	@echo "Set env vars LT_USERNAME & LT_ACCESS_KEY"
    # Procure Username and AccessKey from https://accounts.lambdatest.com/security
    export LT_USERNAME=himanshuj
    export LT_ACCESS_KEY=URsVCP7vFs0p

.PHONY: test
test:
    export NODE_ENV = test

.PHONY: test
tool_tip_verification_demo:
	- echo "PyUnit: Tool-Tip verification demo"
	- $(PYTHON_GEN) tests/pyunit/pyunit_tooltip_verification.py

.PHONY: clean
clean:
    # This helped: https://gist.github.com/hbsdev/a17deea814bc10197285
	find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
	@echo "Clean Succeeded"

	find . | grep -E "(.DS_Store)" | xargs rm -rf
	@echo "Clean of DS_Store Succeeded"

	find . | grep -E "(.cache)" | xargs rm -rf
	@echo "Pytest Cache clean Succeeded"

.PHONY: distclean
distclean: clean
	rm -rf venv

.PHONY: help
help:
	@echo ""
	@echo "install : Install project dependencies"
	@echo "clean : Clean up temp files"
	@echo "tool_tip_verification_demo : Get tooltip text for element validation in Selenium"
