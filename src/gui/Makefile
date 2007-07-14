# Default target executed when no arguments are given to make.
default_target: all

all: main_window_ui.py select_type_ui.py main_menu_ui.py create_project_ui.py open_project_ui.py project_view_ui.py add_alternative_ui.py

clean:
	rm -f *_ui.py
	rm -f *.pyc
	rm -f *~
	rm -f *#

main_window_ui.py: main_window.ui
	pyuic4 -o main_window_ui.py main_window.ui

select_type_ui.py: select_type.ui
	pyuic4 -o select_type_ui.py select_type.ui

main_menu_ui.py: main_menu.ui
	pyuic4 -o main_menu_ui.py main_menu.ui

create_project_ui.py: create_project.ui
	pyuic4 -o create_project_ui.py create_project.ui

open_project_ui.py: open_project.ui
	pyuic4 -o open_project_ui.py open_project.ui

project_view_ui.py: project_view.ui
	pyuic4 -o project_view_ui.py project_view.ui

add_alternative_ui.py: add_alternative.ui
	pyuic4 -o add_alternative_ui.py add_alternative.ui