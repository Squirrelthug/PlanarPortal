class ScreenHandler():
    def __init__(self,):
        self.button_positions = {}

    def save_positions(self, buttons):
        for button in buttons:
            self.button_positions[button] = button.pos

    def clear_screen(self, widget):
        widget.canvas.clear()

    def restore_positions(self):
        for button, pos in self.button_positions.items():
            button.pos = pos
