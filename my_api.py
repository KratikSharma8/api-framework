from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

users = [
    {"id": 1, "name": "Kratik Sharma", "email": "kratik@test.com", "role": "admin"},
    {"id": 2, "name": "Rahul Verma", "email": "rahul@test.com", "role": "user"},
    {"id": 3, "name": "Priya Singh", "email": "priya@test.com", "role": "user"},
]

@app.get("/api/users")
def get_all_users():
    return {"total": len(users), "data": users}

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {"data": user}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/api/users")
def create_user(user: dict):
    new_user = {
        "id": len(users) + 1,
        "name": user.get("name", ""),
        "email": user.get("email", ""),
        "role": user.get("role", "user")
    }
    users.append(new_user)
    return JSONResponse(content=new_user, status_code=201)