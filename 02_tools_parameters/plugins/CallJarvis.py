class Tasks:

    def change_task_title(self, task_id: str, new_title: str) -> int:
        print(f"Changing title of task {task_id} to {new_title}")
        # Here you should call the API to change title
        # api will return new version of the task
        new_version = 7
        return new_version
    
    def search_task(self, search_string: str) -> str:
        print(f"Searching for task {search_string}")
        # Here you should call the API to search for a task
        # api will return a list of tasks
        tasks = ["Task_3", "Task_4", "Task_6"]
        return tasks
    
    def load_task(self, task_id: str) -> str:
        """
        Load a task from the API and return the task content in json format
        """
        print(f"Loading task {task_id}")
        # Here you should call the API to load a task
        # api will return the task content
        tasks = {
            "Task_3": {
                "id": "Task_3",
                "title": "Hey I'm task 3",
                "description": "This is the description of task 3",
                "version": 5,
                "due_date": "2021-10-10"
            },
            "Task_4": {
                "id": "Task_4",
                "title": "I'm beautiful task 4",
                "description": "This is the description of task 4",
                "version": 5,
                "due_date": "2022-10-10"
            },
            "Task_6": {
                "id": "Task_6",
                "title": "I'm the six",
                "description": "This is the description of task 6",
                "version": 5,
                "due_date": "2023-10-10"
            }
        }
        return tasks.get(task_id)

        