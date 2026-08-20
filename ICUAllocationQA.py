from ICUAllocation import ICUSystem, create_patient


def test_critical_patient():

    hospital = ICUSystem(2)

    patient = create_patient(
        "P1", 65, 82, 135,
        85, 60, 39.5,
        ["Diabetes"]
    )

    result, message = hospital.admit_patient(patient)

    assert result
    assert patient["category"] == "CRITICAL"

    print("Critical patient: PASS")


def test_normal_patient():

    hospital = ICUSystem(2)

    patient = create_patient(
        "P2", 40, 97, 75,
        120, 80, 37
    )

    result, message = hospital.admit_patient(patient)

    assert result
    assert patient["category"] == "NORMAL"

    print("Normal patient: PASS")


def test_emergency_case():

    hospital = ICUSystem(2)

    patient = create_patient(
        "P3", 70, 95, 80,
        120, 80, 37,
        emergency=True
    )

    result, message = hospital.admit_patient(patient)

    assert result
    assert patient["score"] >= 30

    print("Emergency case: PASS")


def test_no_icu_beds():

    hospital = ICUSystem(1)

    patient1 = create_patient(
        "P1", 50, 95, 80,
        120, 80, 37
    )

    patient2 = create_patient(
        "P2", 50, 95, 80,
        120, 80, 37
    )

    hospital.admit_patient(patient1)

    result, message = hospital.admit_patient(patient2)

    assert result
    assert len(hospital.waiting_list) == 1

    print("No ICU beds: PASS")


def test_duplicate_patient():

    hospital = ICUSystem(2)

    patient = create_patient(
        "P1", 50, 95, 80,
        120, 80, 37
    )

    hospital.admit_patient(patient)

    result, message = hospital.admit_patient(patient)

    assert not result

    print("Duplicate patient: PASS")


def test_invalid_oxygen():

    hospital = ICUSystem(2)

    patient = create_patient(
        "P1", 50, 150, 80,
        120, 80, 37
    )

    result, message = hospital.admit_patient(patient)

    assert not result

    print("Invalid oxygen: PASS")


def test_invalid_heart_rate():

    hospital = ICUSystem(2)

    patient = create_patient(
        "P1", 50, 95, 0,
        120, 80, 37
    )

    result, message = hospital.admit_patient(patient)

    assert not result

    print("Invalid heart rate: PASS")


def test_priority_boundary():

    hospital = ICUSystem(2)

    patient = create_patient(
        "P1", 50, 89, 125,
        120, 80, 37
    )

    score = hospital.calculate_priority(patient)

    assert score >= 50

    print("Priority boundary: PASS")


def test_multiple_patients():

    hospital = ICUSystem(2)

    for i in range(3):

        patient = create_patient(
            "P" + str(i),
            50,
            95,
            80,
            120,
            80,
            37
        )

        hospital.admit_patient(patient)

    assert hospital.available_beds == 0
    assert len(hospital.waiting_list) == 1

    print("Multiple patients competing for beds: PASS")


def main():

    print("================================")
    print("ICU ALLOCATION QA")
    print("================================")

    test_critical_patient()
    test_normal_patient()
    test_emergency_case()
    test_no_icu_beds()
    test_duplicate_patient()
    test_invalid_oxygen()
    test_invalid_heart_rate()
    test_priority_boundary()
    test_multiple_patients()

    print("================================")
    print("ALL ICU TESTS PASSED")
    print("================================")


if __name__ == "__main__":
    main()
