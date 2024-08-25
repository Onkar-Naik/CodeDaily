"""
Write a program to access value of key from nested json data
"""
import json
a = """{
  "student": {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science",
    "courses": {
      "current": [
        {
          "course_name": "Data Structures",
          "instructor": "Dr. Smith"
        },
        {
          "course_name": "Operating Systems",
          "instructor": "Prof. Johnson"
        }
      ],
      "completed": [
        {
          "course_name": "Introduction to Programming",
          "grade": "A"
        },
        {
          "course_name": "Algorithms",
          "grade": "B+"
        }
      ]
    }
  }
}"""

b = json.loads(a)
print(b["student"]["courses"]["completed"])