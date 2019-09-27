.PHONY: install
install:
	sudo apt-get install python3-opencv && sudo apt-get ffmpeg

.PHONY: test
test:
	Make is not configured to run any tests

.PHONY: run
run:
	python3 vid.py