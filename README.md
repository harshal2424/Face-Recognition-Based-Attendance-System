
# 📸 Face Recognition Based Attendance System

A web-based smart attendance system that uses face recognition from group photos to mark attendance efficiently and contactlessly.

---

## 🚀 Project Overview

This system replaces traditional or RFID-based attendance methods with a fully automated solution powered by computer vision. Instructors can upload classroom images, and the system detects and recognizes faces to mark attendance — significantly reducing manual effort and preventing proxies.

---

## 🔍 Key Features

- ✅ **Automatic Attendance** using face recognition from group photos  
- 🎯 **High-Accuracy Face Detection** using DeepFace (RetinaFace backend)  
- 🧠 **Face Matching** with `face_recognition` (ResNet-based embeddings)  
- 👨‍🏫 **Instructor Dashboard** for attendance review and correction  
- 📁 **Export Attendance** to Excel sheets  
- 🧑‍🎓 **Student Photo Database** management  
- ⚙️ Built with **Django (MVT architecture)**  

---

## 🧰 Tech Stack

| Technology         | Purpose                          |
|--------------------|----------------------------------|
| Python 3.11        | Core programming language        |
| Django 5.x         | Web framework                    |
| DeepFace           | Face detection                   |
| face_recognition   | Face encoding & comparison       |
| OpenCV, Pillow     | Image processing                 |
| SQLite / PostgreSQL| Database                         |
| openpyxl           | Excel export                     |

---

## 🧪 Setup Instructions

### ⚙️ 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 💡 2. Activate the Environment

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

### 📦 3. Install Required Packages

```bash
pip install Django==5.*
pip install deepface
pip install face_recognition
pip install opencv-python
pip install Pillow
pip install openpyxl
```

> Make sure Python version is **3.11**

---

## 🧑‍💻 User Roles

### 🛠 Admin
- Create/manage courses and subjects  
- Add students and upload their reference photos  

### 👨‍🏫 Instructor
- Upload group photos for attendance  
- Auto-detect & mark present/absent students  
- Manually tag unidentified faces  
- Export attendance reports  

---

## 📷 How It Works

1. Instructor selects course and uploads group photo(s)  
2. System detects all faces using `DeepFace`  
3. Each face is compared with stored student images using `face_recognition`  
4. Attendance is automatically recorded  
5. Unidentified faces are shown for manual correction  
6. Attendance can be exported to Excel  

---

## 🖼️ Sample Output Screens

## 🔐 Login Screen

[![Login Dashboard](Dashboard.png)](Dashboard.png)

## 🗂️ Course Dashboard

[![Course Dashboard](course%20dashboard.png)](course%20dashboard.png)


### 🔒 Admin Dashboard
![Admin Dashboard](admin%20dashboard.jpg)

## 🖼️ Instructor Dashboard – Photo Upload & Detection Result

[![Instructor Dashboard](instructor%20dashboard.jpg)](instructor%20dashboard.jpg)

### 📋 Instructor Dashboard with Attendance Results
![Instructor Dashboard](instructor%20dashboard2.jpg)

## 📊 Excel Attendance Export

[![Excel View](excel%20view.png)](excel%20view.png)



---

