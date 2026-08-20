class ICUSystem:

    def __init__(self, total_beds):
        self.total_beds = total_beds
        self.available_beds = total_beds
        self.waiting_list = []
        self.admitted_patients = []

    def calculate_priority(self, patient):
        score = 0

        oxygen = patient["oxygen"]
        heart_rate = patient["heart_rate"]
        systolic, diastolic = patient["blood_pressure"]
        temperature = patient["temperature"]

        if oxygen < 90:
            score += 40
        elif oxygen < 94:
            score += 20

        if heart_rate > 120 or heart_rate < 50:
            score += 20

        if systolic < 90 or diastolic < 60:
            score += 20

        if temperature >= 39:
            score += 10

        if patient["emergency"]:
            score += 30

        if len(patient["conditions"]) > 0:
            score += 10

        return score

    def get_category(self, score):
        if score >= 60:
            return "CRITICAL"
        elif score >= 30:
            return "URGENT"
        else:
            return "NORMAL"

    def admit_patient(self, patient):

        if patient["oxygen"] < 0 or patient["oxygen"] > 100:
            return False, "Invalid oxygen level"

        if patient["heart_rate"] <= 0:
            return False, "Invalid heart rate"

        for p in self.admitted_patients:
            if p["patient_id"] == patient["patient_id"]:
                return False, "Duplicate patient"

        score = self.calculate_priority(patient)
        category = self.get_category(score)

        patient["score"] = score
        patient["category"] = category

        if self.available_beds > 0:
            self.available_beds -= 1
            self.admitted_patients.append({
                "patient_id": patient["patient_id"]
            })

            return True, category + " patient allocated ICU bed"

        self.waiting_list.append(patient["patient_id"])

        return True, category + " patient added to waiting list"


def create_patient(patient_id, age, oxygen, heart_rate,
                   systolic, diastolic, temperature,
                   conditions=None, emergency=False):

    return {
        "patient_id": patient_id,
        "age": age,
        "oxygen": oxygen,
        "heart_rate": heart_rate,
        "blood_pressure": (systolic, diastolic),
        "temperature": temperature,
        "conditions": conditions or [],
        "emergency": emergency
    }


def main():

    print("===== ICU RESOURCE ALLOCATION =====")

    hospital = ICUSystem(2)

    patients = [

        create_patient(
            "P001", 65, 82, 135,
            85, 60, 39.5,
            ["Diabetes"]
        ),

        create_patient(
            "P002", 40, 97, 75,
            120, 80, 37.0
        ),

        create_patient(
            "P003", 70, 88, 125,
            88, 60, 39.2,
            ["Heart Disease"],
            True
        )
    ]

    for patient in patients:

        result, message = hospital.admit_patient(patient)

        print(patient["patient_id"], ":", message)

        if result:
            print(
                "Priority:",
                patient.get("score"),
                "Category:",
                patient.get("category")
            )

    print("Available ICU beds:",
          hospital.available_beds)

    print("Waiting list:",
          hospital.waiting_list)


if __name__ == "__main__":
    main()
