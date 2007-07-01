# Default target executed when no arguments are given to make.
default_target: all

all: start_language_ui.py

clean:
	rm -f start_wizard_ui.py
	rm -f start_language_ui.py
	rm -f *.pyc
	rm -f *~
	rm -f *#

start_language_ui.py: start_language.ui
	pyuic4 -o start_language_ui.py start_language.ui

start_wizard_ui.py: start_wizard.ui
	pyuic4 -o start_wizard_ui.py start_wizard.ui