# Default target executed when no arguments are given to make.
default_target: all

all: main_window_ui.py select_type_ui.py create_project_ui.py open_project_ui.py project_view_ui.py add_alternative_ui.py add_criteria_ui.py add_ordinal_option_ui.py mca_wizard_ui.py mca_wizard2_ui.py mca_result_view_ui.py

clean:
	rm -f *_ui.py
	rm -f *.pyc
	rm -f *~
	rm -f *#

main_window_ui.py: main_window.ui
	pyuic4 -o main_window_ui.py main_window.ui

select_type_ui.py: select_type.ui
	pyuic4 -o select_type_ui.py select_type.ui

create_project_ui.py: create_project.ui
	pyuic4 -o create_project_ui.py create_project.ui

open_project_ui.py: open_project.ui
	pyuic4 -o open_project_ui.py open_project.ui

project_view_ui.py: project_view.ui
	pyuic4 -o project_view_ui.py project_view.ui

add_alternative_ui.py: add_alternative.ui
	pyuic4 -o add_alternative_ui.py add_alternative.ui

add_criteria_ui.py: add_criteria.ui
	pyuic4 -o add_criteria_ui.py add_criteria.ui

add_ordinal_option_ui.py: add_ordinal_option.ui
	pyuic4 -o add_ordinal_option_ui.py add_ordinal_option.ui

mca_wizard_ui.py: mca_wizard.ui
	pyuic4 -o mca_wizard_ui.py mca_wizard.ui

mca_wizard2_ui.py: mca_wizard2.ui
	pyuic4 -o mca_wizard2_ui.py mca_wizard2.ui
	
mca_result_view_ui.py: mca_result_view.ui
	pyuic4 -o mca_result_view_ui.py mca_result_view.ui