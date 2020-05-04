def _project():
    return {
        "title": "Demo Project",
        "code": "DEMO",
        "counts": {
            "cases": 10,
            "suites": 3,
            "milestones": 0,
            "runs": {"total": 1, "active": 1},
            "defects": {"total": 0, "open": 0},
        },
    }


def _test_case():
    return {
        "id": 5,
        "position": 1,
        "title": "Test case",
        "description": "Description for case",
        "preconditions": "",
        "postconditions": "",
        "severity": 4,
        "priority": 2,
        "type": 1,
        "behavior": 2,
        "automation": "is-not-automated",
        "status": "actual",
        "milestone_id": None,
        "suite_id": 1,
        "tags": [],
        "links": [],
        "revision": 1,
        "custom_fields": [],
        "attachments": [],
        "steps": [],
        "created": "2018-05-02T20:32:23.000000Z",
        "updated": "2019-07-21T13:24:08.000000Z",
    }


def _test_run():
    return {
        "id": 1,
        "title": "Test run 2019/12/12",
        "description": None,
        "status": 0,
        "start_time": "2019-12-12 12:12:12",
        "end_time": None,
        "public": False,
        "stats": {
            "total": 3,
            "untested": 3,
            "passed": 0,
            "failed": 0,
            "blocked": 0,
            "skipped": 0,
            "retest": 0,
            "deleted": 4,
        },
        "time_spent": 0,
        "user_id": 1,
        "environment": None,
        "cases": [1, 2, 3],
    }


def _test_run_result():
    return {
        "hash": "6efce6e4f9de887a2ee863e8197cb74ab626a273",
        "comment": "some comment",
        "run_id": 1,
        "case_id": 1,
        "steps": None,
        "status": "Passed",
        "is_api_result": True,
        "time_spent": 0,
        "end_time": "2018-11-11 11:11:11",
    }


def _list(data):
    return {"total": 10, "filtered": 10, "count": 1, "entities": [data]}


def _status_true(data):
    return {"status": True, "result": data}