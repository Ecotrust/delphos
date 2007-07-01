# Default target executed when no arguments are given to make.
default_target: all

all: main_window_ui.py start_language_ui.py
clean:
	rm -f main_window_ui.py
	rm -f start_wizard_ui.py
	rm -f start_language_ui.py
	rm -f *.pyc
	rm -f *~
	rm -f *#

main_window_ui.py: main_window.ui
	pyuic4 -o main_window_ui.py main_window.ui

start_language_ui.py: start_language.ui
	pyuic4 -o start_language_ui.py start_language.ui

start_wizard_ui.py: start_wizard.ui
	pyuic4 -o start_wizard_ui.py start_wizard.ui