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

    # Add extra course only for testing credit limit
    system.courses["Cloud Computing"] = {
        "credits": 4,
        "semester": 5,
        "prerequisite": None,
        "time": "3PM",
        "capacity": 2
    }

    result, message = system.register(
        "S1",
        5,
        ["Data Structures"],
        [
            "Statistics",
            "AI",
            "ML",
            "Cloud Computing"
        ]
    )

    assert not result
    assert message == "Credit limit exceeded"

    print("Credit limit: PASS")


def test_timetable_conflict():

    system = CourseSystem()

    # Make ML and AI have the same time
    system.courses["ML"]["time"] = "1PM"

    result, message = system.register(
        "S1",
        5,
        ["Data Structures"],
        ["AI", "ML"]
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

    result, message = system.register(
        "S1",
        5,
        ["Data Structures", "Statistics"],
        ["AI", "ML"]
    )

    assert result

    # AI = 2 credits
    # ML = 1 credit
    # Total = 3 credits
    assert system.get_credits("S1") == 3

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