class CourseSystem:

    def __init__(self):
        self.courses = {
            "Programming": {
                "credits": 2,
                "semester": 3,
                "prerequisite": None,
                "time": "9AM",
                "capacity": 2
            },
            "Data Structures": {
                "credits": 2,
                "semester": 5,
                "prerequisite": None,
                "time": "10AM",
                "capacity": 2
            },
            "Statistics": {
                "credits": 2,
                "semester": 5,
                "prerequisite": None,
                "time": "11AM",
                "capacity": 2
            },
            "AI": {
                "credits": 2,
                "semester": 5,
                "prerequisite": "Data Structures",
                "time": "1PM",
                "capacity": 2
            },
            "ML": {
                "credits": 1,
                "semester": 5,
                "prerequisite": "AI",
                "time": "2PM",
                "capacity": 2
            }
        }

        self.registrations = {}

    def register(self, student_id, semester,
                 completed_courses, selected_courses):

        current = self.registrations.get(
            student_id, []
        )

        # Check invalid courses
        for course in selected_courses:
            if course not in self.courses:
                return False, "Invalid course"

        # Check duplicate registration
        for course in selected_courses:
            if course in current:
                return False, "Duplicate registration"

        # Check semester and prerequisites
        for course in selected_courses:

            info = self.courses[course]

            if semester != info["semester"]:
                return False, "Semester restriction"

            prerequisite = info["prerequisite"]

            if prerequisite is not None:
                if prerequisite not in completed_courses:
                    return False, (
                        "Missing prerequisite for " + course
                    )

        # Check credit limit
        total_credits = sum(
            self.courses[c]["credits"]
            for c in current + selected_courses
        )

        if total_credits > 8:
            return False, "Credit limit exceeded"

        # Check timetable conflict
        times = []

        for course in current + selected_courses:

            course_time = self.courses[course]["time"]

            if course_time in times:
                return False, "Timetable conflict"

            times.append(course_time)

        # Check course capacity
        for course in selected_courses:

            enrolled = len([
                student
                for student in self.registrations
                if course in self.registrations[student]
            ])

            if enrolled >= self.courses[course]["capacity"]:
                return False, "Course is full"

        # Registration successful
        current.extend(selected_courses)

        self.registrations[student_id] = current

        return True, "Registration successful"

    def get_credits(self, student_id):

        return sum(
            self.courses[c]["credits"]
            for c in self.registrations.get(
                student_id, []
            )
        )


def main():

    print("===== COURSE REGISTRATION =====")

    system = CourseSystem()

    result, message = system.register(
        "S001",
        5,
        ["Data Structures", "Statistics"],
        ["AI"]
    )

    print(message)

    print(
        "Total credits:",
        system.get_credits("S001")
    )


if __name__ == "__main__":
    main()
