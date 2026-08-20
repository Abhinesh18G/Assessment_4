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

    result, message = system.register(
        "S1",
        5,
        ["Data Structures", "Statistics", "AI"],
        ["ML", "AI"]
    )

    assert not result

    print("Credit limit: PASS")


def test_timetable_conflict():

    system = CourseSystem()

    # Create a conflict by registering two courses
    # with the same timetable.
    system.courses["ML"]["time"] = "1PM"

    result, message = system.register(
        "S1",
        5,
        ["Data Structures", "AI"],
        ["ML", "AI"]
    )

    assert not result
    assert message == "Timetable conflict"

    print("Timetable conflict: PASS")


def test_full_course():

    system = CourseSystem()

    system.register(
        "S1",
        5,
        ["Data Structures"],
        ["AI"]
    )

    system.register(
        "S2",
        5,
        ["Data Structures"],
        ["AI"]
    )

    result, message = system.register(
        "S3",
        5,
        ["Data Structures"],
        ["AI"]
    )

    assert not result
    assert message == "Course is full"

    print("Full course: PASS")


def test_duplicate_registration():

    system = CourseSystem()

    system.register(
        "S1",
        5,
        ["Data Structures"],
        ["AI"]
    )

    result, message = system.register(
        "S1",
        5,
        ["Data Structures"],
        ["AI"]
    )

    assert not result
    assert message == "Duplicate registration"

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
    assert system.get_credits("S1") == 5

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
