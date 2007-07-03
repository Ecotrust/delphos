# Default target executed when no arguments are given to make.
default_target: all

all: main_window_ui.py start_ui.py
clean:
	rm -f main_window_ui.py
	rm -f start_ui.py
	rm -f *.pyc
	rm -f *~
	rm -f *#

main_window_ui.py: main_window.ui
	pyuic4 -o main_window_ui.py main_window.ui

start_ui.py: start.ui
	pyuic4 -o start_ui.py start.ui