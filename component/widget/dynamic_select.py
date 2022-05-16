from sepal_ui import sepalwidgets as sw
from sepal_ui import color as sc
import ipyvuetify as v
from ipywidgets import jslink

from component.message import cm


class DynamicSelect(v.Layout):
    def __init__(self):

        self.prev = v.Btn(
            _metadata={"increm": -1},
            x_small=True,
            class_="ml-2 mr-2",
            color=sc.secondary,
            children=[v.Icon(children=["mdi-chevron-left"]), cm.dynamic_select.prev],
        )

        self.next = v.Btn(
            _metadata={"increm": 1},
            x_small=True,
            class_="ml-2 mr-2",
            color=sc.secondary,
            children=[cm.dynamic_select.next, v.Icon(children=["mdi-chevron-right"])],
        )

        self.select = v.Select(dense=True, label=cm.dynamic_select.label, v_model=None)

        super().__init__(
            v_model=None,
            align_center=True,
            row=True,
            class_="ma-1",
            children=[self.prev, self.select, self.next],
        )

        # js behaviour
        jslink((self, "v_model"), (self.select, "v_model"))
        self.prev.on_event("click", self._on_click)
        self.next.on_event("click", self._on_click)

    def set_items(self, items):
        """Change the value of the items of the select"""

        self.select.items = items

        return self

    def _on_click(self, widget, event, data):
        """go to the next value. loop to the first or last one if we reach the end"""

        increm = widget._metadata["increm"]

        # create a sanitized version of the item list without the header
        items = [i["value"] for i in self.select.items if "header" not in i]

        # get the current position in the list
        val = self.select.v_model
        if val in items:
            pos = items.index(val)
            pos += increm

            # check if loop is required
            if pos == -1:
                pos = len(items) - 1
            elif pos >= len(items):
                pos = 0

        # if none was selected always start by the first
        else:
            pos = 0

        self.select.v_model = items[pos]

        return self

    def disable(self):

        self.prev.disabled = True
        self.next.disabled = True
        self.select.disabled = True

        return self

    def unable(self):

        self.prev.disabled = False
        self.next.disabled = False
        self.select.disabled = False

        return self
