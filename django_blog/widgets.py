from dashing.widgets import NumberWidget

class CustomWidget(NumberWidget):
    title = 'user'
    value = 25

    def get_more_info(self):
        more_info = 'Random additional info'
        return more_info
