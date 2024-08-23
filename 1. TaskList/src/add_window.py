import flet as ft


# This class is used to reference the window that will contain the form to add a new task.
class AddWindow(ft.Column):
    # Private attributes
    __task_title: ft.TextField
    __task_description: ft.TextField
    __add_task_view: ft.Row

    # The methods for the buttons below are assigned to these attributes.
    __add_event: None
    __cancel_event: None

    # Constructor
    def __init__(self, add_event, cancel_event, visible=False):
        super().__init__()
        self.visible = visible
        self.__add_event = add_event
        self.__cancel_event = cancel_event

        self.__task_title = ft.TextField(hint_text="Task Title", width=200, height=40, text_size=12)
        self.__task_description = ft.TextField(hint_text="Task Description", width=200, height=40, text_size=12)

        self.__add_task_view = self.__add_task_view_build()

        self.width = 600
        self.controls = [self.__add_task_view]
    
    # Getters
    @property
    def task_title(self) -> ft.TextField: return self.__task_title
    @property
    def task_description(self) -> ft.TextField: return self.__task_description

    # Public methods: These are the most controlled way to set the values.
    def title_default(self): self.__task_title.value = ""
    def description_default(self): self.__task_description.value = ""

    # Private methods. This method shows the form to add a new task.
    def __add_task_view_build(self) -> ft.Row:
        add_task = ft.Row([
            ft.Column([
                self.__task_title,
                self.__task_description,
            ]),
            ft.Column([
                ft.IconButton(icon=ft.icons.SAVE, on_click=self.__add_event),
                ft.IconButton(icon=ft.icons.CANCEL, on_click=self.__cancel_event)
            ])
        ], alignment=ft.MainAxisAlignment.CENTER)
        return add_task
    