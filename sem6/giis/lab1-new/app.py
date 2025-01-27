import sys

from PyQt5.QtWidgets import QApplication, QStackedWidget

from view import MainView, ExplainView


class App(QApplication):
    current_view = None
    
    def __init__(self, *args):
        super().__init__(list(args))
        self.widgets = QStackedWidget()
        self.main_view = MainView()
        self.explain_view = ExplainView()

        self._init_view()
        self._init_app()

    def _init_app(self):
        self.widgets.addWidget(self.main_view)
        self.widgets.addWidget(self.explain_view)
        self.widgets.setFixedWidth(700)
        self.widgets.setFixedHeight(700)
        self._switch_view(self.main_view)
        self.widgets.show()
    
    def _init_view(self):
        self.main_view.ui.ExplainPushButton.clicked.connect(self._goto_explain)
        self.explain_view.ui.BackPushButton.clicked.connect(self._goto_main)
        
    def _switch_view(self, view):
        self.current_view = view
        self.widgets.setCurrentWidget(self.current_view)
        
    def _goto_explain(self):
        table_data, model_name = self.main_view.get_explain_data()
        if table_data:
            self.explain_view.set_table_data(
                data=table_data,
                model_name=model_name
            )
            self._switch_view(self.explain_view)
        else:
            print("line not drawed!")

    def _goto_main(self):
        self.main_view.draw_line()
        self._switch_view(self.main_view)

def application():
    app = App(sys.argv)
    app.setApplicationName("Line Drawer")
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
