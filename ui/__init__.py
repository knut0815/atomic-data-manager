""""
Copyright (C) 2019 Grant Wilk

This file is part of Data MGR.

Data MGR is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

Data MGR is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License along
with Data MGR.  If not, see <https://www.gnu.org/licenses/>.
"""

import bpy
from atomic_data_manager.ui import main_panel_ui, stats_panel_ui


def register():
    main_panel_ui.register()
    stats_panel_ui.register()
    inspect_ui.register()


def unregister():
    main_panel_ui.unregister()
    stats_panel_ui.unregister()
    inspect_ui.unregister()
