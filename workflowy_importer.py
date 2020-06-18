#!/usr/bin/env python

import json
import sys
from typing import Union


def read_file() -> list:
    filename = sys.argv[1]
    with open(filename, "r", encoding="utf-8-sig") as f:
        wunderlist_export = json.load(f)
    return wunderlist_export


def extract_list(lst: dict) -> dict:
    listname = lst.get("title")
    if not lst.get("tasks"):
        return None
    tasks = {}
    for task in lst.get("tasks"):
        taskname = task.get("title")
        task_dict = {}
        task_dict = additional_info(task, "subtasks", "title", task_dict)
        task_dict = additional_info(task, "notes", "content", task_dict)
        task_dict = additional_info(task, "comments", "text", task_dict)
        if task_dict:
            tasks.update({taskname: task_dict})
    return {listname: tasks}


def additional_info(task: dict, field: str, subfield: str, input_dict: dict) -> dict:
    f = task.get(field)
    if f:
        for ff in f:
            if ff.get(subfield):
                input_dict.update({field: ff.get(subfield)})
    return input_dict


def print_next_level(
    inpt: Union[list, dict], level_count: int, sep: str = " ", stop_level: int = 20
) -> None:
    if level_count > stop_level:
        sys.exit()
    if isinstance(inpt, list):
        for el in inpt:
            print(f"{sep*level_count}{el}")
    elif isinstance(inpt, dict):
        for key, value in inpt.items():
            if value:
                next_level = value.splitlines() if isinstance(value, str) else value
                print(f"{sep*level_count}{key}")
                print_next_level(next_level, level_count + 1, sep)


def main() -> None:

    wunderlist_export = read_file()
    structured_dict = {}

    for l in wunderlist_export:
        basic_list = extract_list(l)
        if basic_list is None:
            continue
        f = l.get("folder")
        if f is not None:
            foldername = f.get("title")
            if foldername in structured_dict:
                structured_dict[foldername].update(basic_list)
            else:
                structured_dict[foldername] = basic_list
        else:
            structured_dict.update(basic_list)

    print_next_level(structured_dict, 0, " ")


if __name__ == "__main__":

    main()
