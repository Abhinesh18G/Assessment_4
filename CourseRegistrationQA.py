from CourseRegistration import CourseSystem


def test_valid_registration():

    system = CourseSystem()

    result, message = system.register(
        "S1",
        5,
        ["Data Structures"],
        ["AI"]
    )

    assert result
    assert message == "Registration successful"

    print("Valid registration: PASS")


def test_missing_prerequisite():

    system = CourseSystem()

    result, message = system.register(
        "S1",
        5,
        [],
        ["AI"]
    )

    assert not result
    assert message == "Missing prerequisite for AI"

    print("Missing prerequisite: PASS")


def test_credit_limit():

    system = CourseSystem()

    # Add temporary courses only for QA testing
    system.courses["Test Credit A"] = {
        "credits": 5,
        "semester": 5,
        "prerequisite": None,
        "time": "4PM",
        "capacity": 10
    }

    system.courses["Test Credit B"] = {
        "credits": 5,
        "semester": 5,
        "prerequisite": None,
        "time": "5PM",
        "capacity": 10
    }

    result, message = system.register(
        "S1",
        5,
        [],
        ["Test Credit A", "Test Credit B"]
    )

    assert not result
    assert message == "Credit limit exceeded"

    print("Credit limit: PASS")


def test_timetable_conflict():

    system = CourseSystem()

    # Add temporary courses with the same timetable
    system.courses["Test Time A"] = {
        "credits": 2,
        "semester": 5,
        "prerequisite": None,
        "time": "1PM",
        "capacity": 10
    }

    system.courses["Test Time B"] = {
        "credits": 2,
        "semester": 5,
        "prerequisite": None,
        "time": "1PM",
        "capacity": 10
    }

    result, message = system.register(
        "S1",
        5,
        [],
        ["Test Time A", "Test Time B"]
    )

    assert not result
    assert message == "Timetable conflict"

    print("Timetable conflict: PASS")


def test_full_course():

    system = CourseSystem()

    result1, message1 = system.register(
        "S1",
        5,
        ["Data Structures"],
        ["AI"]
    )

    result2, message2 = system.register(
        "S2",
        5,
        ["Data Structures"],
        ["AI"]
    )

    result3, message3 = system.register(
        "S3",
        5,
        ["Data Structures"],
        ["AI"]
    )

    assert result1
    assert result2
    assert not result3
    assert message3 == "Course is full"

    print("Full course: PASS")


def test_duplicate_registration():

    system = CourseSystem()

    result1, message1 = system.register(
        "S1",
        5,
        ["Data Structures"],
        ["AI"]
    )

    result2, message2 = system.register(
        "S1",
        5,
        ["Data Structures"],
        ["AI"]
    )

    assert result1
    assert not result2
    assert message2 == "Duplicate registration"

    print("Duplicate registration: PASS")


def test_invalid_course():

    system = CourseSystem()

    result, message = system.register(
        "S1",
        5,
        ["Data Structures"],
        ["Python"]
    )

    assert not result
    assert message == "Invalid course"

    print("Invalid course: PASS")


def test_semester_restriction():

    system = CourseSystem()

    result, message = system.register(
        "S1",
        3,
        ["Programming"],
        ["AI"]
    )

    assert not result
    assert message == "Semester restriction"

    print("Semester restriction: PASS")


def test_boundary_credit():

    system = CourseSystem()

    # Add a temporary 2-credit course.
    # Selected courses will total exactly 8 credits:
    #
    # Data Structures = 2
    # Statistics      = 2
    # AI              = 2
    # Test Boundary   = 2
    #
    # Total = 8

    system.courses["Test Boundary"] = {
        "credits": 2,
        "semester": 5,
        "prerequisite": None,
        "time": "4PM",
        "capacity": 10
    }

    result, message = system.register(
        "S1",
        5,
        ["Data Structures", "AI"],
        [
            "Data Structures",
            "Statistics",
            "AI",
            "Test Boundary"
        ]
    )

    assert result
    assert message == "Registration successful"

    assert system.get_credits("S1") == 8

    print("Boundary credit value: PASS")


def main():

    print("================================")
    print("COURSE REGISTRATION QA")
    print("================================")

    test_valid_registration()
    test_missing_prerequisite()
    test_credit_limit()
    test_timetable_conflict()
    test_full_course()
    test_duplicate_registration()
    test_invalid_course()
    test_semester_restriction()
    test_boundary_credit()

    print("================================")
    print("ALL COURSE REGISTRATION TESTS PASSED")
    print("================================")


if __name__ == "__main__":
    main()