from InsuranceClaim import InsuranceSystem


def valid_claim(system):

    result = system.process_claim(
        "POL1001",
        "CUS001",
        "Health",
        50000,
        "2026-01-01",
        "2026-08-01",
        0,
        20,
        "Medical",
        True
    )

    assert result["status"] == "APPROVED"
    assert result["payout"] == 45000

    print("Valid claim: PASS")


def expired_policy(system):

    result = system.process_claim(
        "POL1002",
        "CUS002",
        "Health",
        10000,
        "2026-01-01",
        "2026-08-01",
        0,
        20,
        "Medical",
        True
    )

    assert result["status"] == "REJECTED"

    print("Expired policy: PASS")


def claim_before_policy(system):

    result = system.process_claim(
        "POL1001",
        "CUS001",
        "Health",
        10000,
        "2026-01-01",
        "2025-12-01",
        0,
        20,
        "Medical",
        True
    )

    assert result["status"] == "REJECTED"

    print("Claim before policy: PASS")


def excessive_claim(system):

    result = system.process_claim(
        "POL1001",
        "CUS001",
        "Health",
        60000,
        "2026-01-01",
        "2026-08-01",
        0,
        20,
        "Medical",
        True
    )

    assert result["status"] == "REJECTED"
    assert result["payout"] == 0

    print("Excessive claim: PASS")


def missing_documents(system):

    result = system.process_claim(
        "POL1001",
        "CUS001",
        "Health",
        10000,
        "2026-01-01",
        "2026-08-01",
        0,
        20,
        "Medical",
        False
    )

    assert result["status"] == "REJECTED"

    print("Missing documents: PASS")


def multiple_previous_claims(system):

    result = system.process_claim(
        "POL1001",
        "CUS001",
        "Health",
        10000,
        "2026-01-01",
        "2026-08-01",
        5,
        20,
        "Medical",
        True
    )

    assert result["status"] == "FRAUD SUSPECTED"

    print("Multiple previous claims: PASS")


def fraud_scenario(system):

    result = system.process_claim(
        "POL1001",
        "CUS001",
        "Health",
        10000,
        "2026-01-01",
        "2026-08-01",
        0,
        80,
        "Medical",
        True
    )

    assert result["status"] == "FRAUD SUSPECTED"

    print("Fraud scenario: PASS")


def boundary_claim(system):

    result = system.process_claim(
        "POL1001",
        "CUS001",
        "Health",
        50000,
        "2026-01-01",
        "2026-08-01",
        0,
        20,
        "Medical",
        True
    )

    assert result["status"] == "APPROVED"
    assert result["payout"] == 45000

    print("Boundary claim: PASS")


def invalid_policy(system):

    result = system.process_claim(
        "INVALID",
        "CUS001",
        "Health",
        10000,
        "2026-01-01",
        "2026-08-01",
        0,
        20,
        "Medical",
        True
    )

    assert result["status"] == "REJECTED"

    print("Invalid policy number: PASS")


def invalid_incident_date(system):

    result = system.process_claim(
        "POL1001",
        "CUS001",
        "Health",
        10000,
        "2026-01-01",
        "wrong-date",
        0,
        20,
        "Medical",
        True
    )

    assert result["status"] == "REJECTED"

    print("Invalid incident date: PASS")


def main():

    print("================================")
    print("INSURANCE CLAIM QA")
    print("================================")

    system = InsuranceSystem()

    valid_claim(system)
    expired_policy(system)
    claim_before_policy(system)
    excessive_claim(system)
    missing_documents(system)
    multiple_previous_claims(system)
    fraud_scenario(system)
    boundary_claim(system)
    invalid_policy(system)
    invalid_incident_date(system)

    print("================================")
    print("ALL INSURANCE TESTS PASSED")
    print("================================")


if __name__ == "__main__":
    main()
