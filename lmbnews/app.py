from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chuoi_bao_mat_cua_ban'
# Sử dụng SQLite cho nhẹ và dễ quản lý khi làm app nhỏ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Định nghĩa cấu trúc bảng Bài viết (Post)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    # category sẽ nhận 1 trong 3 giá trị: 'learn', 'movie', 'book'
    category = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=True) # Dành riêng cho Movie/Book (ví dụ: 1-5 sao)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Tạo cơ sở dữ liệu (Chạy lần đầu tiên)
with app.app_context():
    db.create_all()

# 1. TRANG CHỦ: Hiển thị toàn bộ bài viết mới nhất
@app.route('/')
def index():
    all_posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=all_posts)

# 2. TRANG DANH MỤC: Lọc bài viết theo Learn, Movie hoặc Book
@app.route('/category/<cat_name>')
def category_page(cat_name):
    if cat_name not in ['learn', 'movie', 'book']:
        return "Danh mục không tồn tại!", 404
    
    # Lấy các bài viết thuộc danh mục được yêu cầu
    posts = Post.query.filter_by(category=cat_name).order_by(Post.created_at.desc()).all()
    return render_template('category.html', posts=posts, category=cat_name)

# 3. TRANG TẠO BÀI VIẾT MỚI
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        category = request.form.get('category')
        content = request.form.get('content')
        rating = request.form.get('rating') # Có thể để trống nếu là 'learn'

        # Kiểm tra dữ liệu hợp lệ cơ bản
        if not title or not content or not category:
            flash('Vui lòng điền đầy đủ thông tin!')
            return redirect(url_for('create_post'))

        # Lưu vào database
        new_post = Post(title=title, category=category, content=content, rating=rating)
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for('index'))
        
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(debug=True)
