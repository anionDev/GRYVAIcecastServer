import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def run_testcases():
    TasksForCommonProjectStructure().standardized_tasks_run_testcases_for_docker_project(str(Path(__file__).absolute()), 1, "QualityCheck", sys.argv, True)


if __name__ == "__main__":
    run_testcases()
