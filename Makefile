# .PHONY is used to declare that the targets are not files
.PHONY: clean clean-build clean-pyc clean-test build release

help:
	@echo "Available commands to 'make':"
	@echo "  clean         : remove all build, test, coverage and Python artifacts"
	@echo "  clean-build   : remove build artifacts"
	@echo "  clean-pyc     : remove Python cache file artifacts"
	@echo "  clean-test    : remove test and coverage artifacts"
	@echo "  build         : build package"
	@echo "  release       : upload package to pypi"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '*__pycache__' -exec rm -fr {} +
	find . -name '*_cache' -exec rm -fr {} +

clean-test:
	rm -f .coverage*
	rm -f coverage.xml

build: clean
	python -m build
	ls -l dist

release:
	python -m twine upload dist/*
