from datetime import datetime


class InsuranceSystem:

    def __init__(self):

        self.policies = {
            "POL1001": {
                "customer": "CUS001",
                "type": "Health",
                "coverage": 50000,
                "deductible": 5000,
                "start": "2026-01-01",
                "end": "2026-12-31"
            },

            "POL1002": {
                "customer": "CUS002",
                "type": "Health",
                "coverage": 30000,
                "deductible": 3000,
                "start": "2026-01-01",
                "end": "2026-06-30"
            }
        }

    def process_claim(
        self,
        policy_number,
        customer_id,
        insurance_type,
        claim_amount,
        policy_start,
        incident_date,
        previous_claims,
        fraud_score,
        claim_type,
        documents
    ):

        # Invalid policy
        if policy_number not in self.policies:
            return {
                "status": "REJECTED",
                "coverage": 0,
                "deductible": 0,
                "customer_contribution": 0,
                "payout": 0,
                "fraud_score": fraud_score
            }

        policy = self.policies[policy_number]

        # Customer mismatch
        if customer_id != policy["customer"]:
            return {
                "status": "REJECTED",
                "coverage": 0,
                "deductible": 0,
                "customer_contribution": 0,
                "payout": 0,
                "fraud_score": fraud_score
            }

        # Invalid incident date
        try:
            incident = datetime.strptime(
                incident_date,
                "%Y-%m-%d"
            )

        except ValueError:
            return {
                "status": "REJECTED",
                "coverage": 0,
                "deductible": 0,
                "customer_contribution": 0,
                "payout": 0,
                "fraud_score": fraud_score
            }

        # Check policy dates
        start = datetime.strptime(
            policy["start"],
            "%Y-%m-%d"
        )

        end = datetime.strptime(
            policy["end"],
            "%Y-%m-%d"
        )

        if incident < start or incident > end:
            return {
                "status": "REJECTED",
                "coverage": policy["coverage"],
                "deductible": policy["deductible"],
                "customer_contribution": 0,
                "payout": 0,
                "fraud_score": fraud_score
            }

        # Check policy start date supplied to function
        try:
            supplied_start = datetime.strptime(
                policy_start,
                "%Y-%m-%d"
            )

            if supplied_start != start:
                return {
                    "status": "REJECTED",
                    "coverage": policy["coverage"],
                    "deductible": policy["deductible"],
                    "customer_contribution": 0,
                    "payout": 0,
                    "fraud_score": fraud_score
                }

        except ValueError:
            return {
                "status": "REJECTED",
                "coverage": policy["coverage"],
                "deductible": policy["deductible"],
                "customer_contribution": 0,
                "payout": 0,
                "fraud_score": fraud_score
            }

        # Claim amount validation
        if claim_amount <= 0:
            return {
                "status": "REJECTED",
                "coverage": policy["coverage"],
                "deductible": policy["deductible"],
                "customer_contribution": 0,
                "payout": 0,
                "fraud_score": fraud_score
            }

        # Excessive claim
        if claim_amount > policy["coverage"]:
            status = "REJECTED"
        elif documents is False:
            status = "REJECTED"
        elif previous_claims >= 5:
            status = "FRAUD SUSPECTED"
        elif fraud_score >= 70:
            status = "FRAUD SUSPECTED"
        elif fraud_score >= 40:
            status = "MANUAL REVIEW"
        else:
            status = "APPROVED"

        coverage = policy["coverage"]
        deductible = policy["deductible"]

        payable = min(
            claim_amount,
            coverage
        )

        customer_contribution = min(
            deductible,
            payable
        )

        payout = payable - customer_contribution

        if status == "REJECTED":
            payout = 0

        return {
            "status": status,
            "coverage": coverage,
            "deductible": deductible,
            "customer_contribution": customer_contribution,
            "payout": payout,
            "fraud_score": fraud_score
        }


def main():

    print("===== INSURANCE CLAIM PROCESSING =====")

    system = InsuranceSystem()

    result = system.process_claim(
        "POL1001",
        "CUS001",
        "Health",
        50000,
        "2026-01-01",
        "2026-08-10",
        0,
        25,
        "Medical",
        True
    )

    print("Claim Status:", result["status"])
    print("Coverage:", result["coverage"])
    print("Deductible:", result["deductible"])
    print(
        "Customer Contribution:",
        result["customer_contribution"]
    )
    print("Insurance Payout:", result["payout"])
    print("Fraud Risk Score:", result["fraud_score"])


if __name__ == "__main__":
    main()
