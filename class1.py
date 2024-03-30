from fastapi import FastAPI, HTTPException
from typing import List, Dict, Optional ,Union

app = FastAPI()

Student = Dict[str, Union[str, int]]  # Type alias for student dictionary

students: List[Student] = [
    {
        "name": "Huzaifa",
        "grade": "10th",
        "age": 14,
        "student_id": "P1"
    },
    {
        "name": "Aqib khan",
        "grade": "10th",
        "age": 15,
        "student_id": "P2"
    },
    {
        "name": "Usman",
        "grade": "10th",
        "age": 16,
        "student_id": "P3"
    }
]

# to get all the students 
#===================================================================
@app.get("/students", response_model=List[Student])
async def get_students():
    return students

# to get the required students
#===================================================================

@app.get("/filter", response_model=Optional[Student])
async def filter_student(id: str):
    cap_id = id.capitalize() 
    for student in students:
        if type(student["student_id"])==str:
            cap_value = student["student_id"].capitalize()
        if cap_value == cap_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


# to add the student in the database
#===============================================================================================
@app.post("/addstudent", response_model=List[Student])
async def add_student(name: str, id: str, grade: str, age: int):
    students.append({"name": name, "student_id": id, "grade": grade, "age": age})
    return students


# to update the student in the database 
#================================================================================================
@app.put("/updateStudent/{student_id}", response_model=List[Student])
async def update_student(student_id: str, name: str, grade: str, age: int):
    global students
    for student in students:
        if student["student_id"] == student_id:
            student["name"] = name
            student["grade"] = grade
            student["age"] = age
            return students
    raise HTTPException(status_code=404, detail="Student not found")


# to deletee student for the database
# =================================================================
@app.delete("/deleteStudent", response_model=List[Student])
async def delete_student(id: str):
    global students
    for student in students:
        if type(student["student_id"])==str:
            cap_value = student["student_id"].capitalize()
        cap_id = id.capitalize()
        if cap_value == cap_id:
            students.remove(student)
            return f"{student}is delelted and other are {students}"
    raise HTTPException(status_code=404, detail="Student not found")
