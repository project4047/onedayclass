from oneday import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# 클래스등록
class Course(db.Model):
    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True)
    classid = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)                 # 설명
    price = db.Column(db.Integer, nullable=False, default=0)         # 가격(원)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())             # 생성시각(DB가 기록)

    def __repr__(self):
        return f"<Course {self.classid}>"
