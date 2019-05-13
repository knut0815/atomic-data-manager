"""
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


def box_list(layout, title, items, icon):
    # a title label followed by a box that contains a two column list of items, each of which is preceded by a
    # uniform icon that does not change depending on the objects type

    # Section Title
    row = layout.row()  # extra row for additional spacing
    row = layout.row()
    row.label(text=title)
    box = layout.box()

    if len(items) != 0:
        # Section List
        flow = box.column_flow(columns=2)
        for item in items:
            flow.label(text=item, icon=icon)
    else:
        # No Data in Section Notification
        row = box.row()
        row.enabled = False
        row.label(text="none")


def box_list_diverse(layout, title, items):
    # a title label follwed by a box that contains a two column list of items, each of which is preceded by an icon
    # that changes depending on the type of object that is being listed

    # Section Title
    row = layout.row()  # extra row for additional spacing
    row = layout.row()
    row.label(text=title)
    box = layout.box()

    if len(items) != 0:
        # Section List
        flow = box.column_flow(columns=3)
        objects = bpy.data.objects
        for item in items:
            if objects[item].type == 'ARMATURE':
                flow.label(text=item, icon="OUTLINER_OB_ARMATURE")
            elif objects[item].type == 'CAMERA':
                flow.label(text=item, icon="OUTLINER_OB_CAMERA")
            elif objects[item].type == 'CURVE':
                flow.label(text=item, icon="OUTLINER_OB_CURVE")
            elif objects[item].type == 'EMPTY':
                flow.label(text=item, icon="OUTLINER_OB_EMPTY")
            elif objects[item].type == 'FONT':
                flow.label(text=item, icon="OUTLINER_OB_FONT")
            elif objects[item].type == 'GPENCIL':
                flow.label(text=item, icon="OUTLINER_OB_GREASEPENCIL")
            elif objects[item].type == 'LATTICE':
                flow.label(text=item, icon="OUTLINER_OB_LATTICE")
            elif objects[item].type == 'LIGHT':
                flow.label(text=item, icon="OUTLINER_OB_LIGHT")
            elif objects[item].type == 'LIGHT_PROBE':
                flow.label(text=item, icon="OUTLINER_OB_LIGHTPROBE")
            elif objects[item].type == 'MESH':
                flow.label(text=item, icon="OUTLINER_OB_MESH")
            elif objects[item].type == 'META':
                flow.label(text=item, icon="OUTLINER_OB_META")
            elif objects[item].type == 'SPEAKER':
                flow.label(text=item, icon="OUTLINER_OB_SPEAKER")
            elif objects[item].type == 'SURFACE':
                flow.label(text=item, icon="OUTLINER_OB_SURFACE")
            else:
                flow.label(text=item, icon="QUESTION")
    else:
        # No Data in Section Notification
        row = box.row()
        row.enabled = False
        row.label(text="none")


def inspect_header(layout, dmgr_prop, data):
    # a single column containing a search property and basic data manipulation functions that appears at the top of all
    # inspect data set dialogs

    dmgr = bpy.context.scene.datamgr

    # exterior box and prop search
    col = layout.column(align=True)
    box = col.box()
    row = box.row()
    split = row.split()
    split.prop_search(dmgr, dmgr_prop, bpy.data, data, text="")

    # convert the data set string into an actual data set reference
    data = getattr(bpy.data, data)
    # convert the dmgr_prop input into the value of its respective string property
    text_field = getattr(dmgr, dmgr_prop)

    # determine whether or not the text entered in the string property is a valid key
    is_valid_key = text_field in data.keys()

    # determine whether or not the piece of data is using a fake user
    has_fake_user = is_valid_key and data[text_field].use_fake_user

    # buttons that follow the prop search
    split = row.split()
    row = split.row(align=True)

    # disable the buttons if the key in the search property is invalid
    row.enabled = is_valid_key

    # icon and depression changes depending on whether or not the object is using a fake user
    if not data == bpy.data.collections:
        if has_fake_user:
            row.operator("datamgr.toggle_fake_user", text="", icon="FAKE_USER_ON", depress=True)
        else:
            row.operator("datamgr.toggle_fake_user", text="", icon="FAKE_USER_OFF", depress=False)

    row.operator("datamgr.inspection_duplicate", text="", icon="DUPLICATE")

    if not data == bpy.data.collections:
        row.operator("datamgr.replace", text="", icon="UV_SYNC_SELECT")

    row.operator("datamgr.rename", text="", icon="GREASEPENCIL")  # Alternate Icon: OUTLINER_DATA_FONT
    row.operator("datamgr.inspection_delete", text="", icon="TRASH")


def number_suffix(text, number):
    # returns the text properly formatted as a suffix
    return text + " ({0})".format(number) if int(number) != 0 else text
