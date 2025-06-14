import cv2
from ultralytics import YOLO

# Load the model
yolo = YOLO('yolov8s.pt')

# Load the video capture
videoCap = cv2.VideoCapture(0)

# Function to get class colors
def getColours(cls_num):
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = cls_num % len(base_colors)
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    color = [base_colors[color_index][i] + increments[color_index][i] * 
    (cls_num // len(base_colors)) % 256 for i in range(3)]
    return tuple(color)

img = cv2.imread("hello.jpg")
results = yolo.track(img, stream=True)
for result in results:
    # get the classes names
    classes_names = result.names

    # iterate over each box
    for box in result.boxes:
        # check if confidence is greater than 40 percent
        if box.conf[0] > 0.4:
            # get coordinates
            [x1, y1, x2, y2] = box.xyxy[0]
            # convert to int
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # get the class
            cls = int(box.cls[0])

            # get the class name
            class_name = classes_names[cls]

            # get the respective colour
            colour = getColours(cls)

            # draw the rectangle
            cv2.rectangle(img, (x1, y1), (x2, y2), colour, 2)

            # put the class name and confidence on the image
            cv2.putText(img, f'{classes_names[int(box.cls[0])]} {box.conf[0]:.2f}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, colour, 2)
            
# show the image
cv2.imshow('frame', img)
cv2.waitKey(0)

'''

    <!-- Display processed faces -->
    {% if processed_faces %}
        <h2>Detected Faces</h2>
        <form method="POST" action="{% url 'process_output' %}">
            {% csrf_token %}
            <label for="course">Select Course:</label>
            <select name="course" id="course" required>
                {% for course in courses %}
                    <option value="{{ course.id }}">{{ course.name }}</option>
                {% endfor %}
            </select>

            <div style="display: flex; flex-wrap: wrap; gap: 10px;">
                {% for face in processed_faces %}
                    <div style="border: 1px solid #ccc; padding: 10px;">
                        <img src="{{ face }}" alt="Detected Face" style="width: 100px; height: 100px; object-fit: cover;">
                        <input type="hidden" name="face_image_url" value="{{ face }}">
                        <label for="student_{{ forloop.counter }}">Select Student:</label>
                        <select name="student" id="student_{{ forloop.counter }}" required>
                            {% for student in students %}
                                <option value="{{ student.id }}">{{ student.name }}</option>
                            {% endfor %}
                        </select>
                        <button type="submit">Mark Present</button>
                    </div>
                {% endfor %}
            </div>
        </form>
    {% endif %}
    '''