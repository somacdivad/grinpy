lint:
	flake8 grinpy/

check-formatting:
	black --check grinpy/

format:
	black grinpy/
