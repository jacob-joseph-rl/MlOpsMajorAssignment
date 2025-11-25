# MlOpsMajorAssignment

A Flask web app for image upload and face class prediction, containerized with Docker and orchestrated using Kubernetes/Minikube.

Features
Upload image files via a web interface

Predict face classes using a trained machine learning model (savedmodel.pth)

Responsive UI styled with static/css/style.css

Containerized with Docker

Supports Kubernetes deployment and scaling

Minikube development support (Mac M1/M2 ready)

**Directory Structure**
MlOpsMajorAssignment/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── savedmodel.pth
├── static/
│   └── css/style.css
├── templates/
│   └── index.html
├── uploads/         # For uploaded images
├── README.md
└── .gitignore


**Setup & Run (Local)**
1. Install dependencies:
pip install -r requirements.txt

2. Run the app:
python app.py

3. Access the app at http://localhost:5000

**Docker Build & Run**
1. Build the image:
docker build -t mlops-major-assignment .

2. Run the container:
docker run -p 5000:5000 mlops-major-assignment

3. Access http://localhost:5000

**Kubernetes Deployment (Minikube)**
1. Start Minikube:
minikube start

2. Apply deployment:
kubectl apply -f deployment.yaml

3. Forward port or use NodePort to access:
kubectl port-forward service/myapp 8080:8080

Access http://127.0.0.1:8080

**Notes**
Do not commit minikube-darwin-arm64 or any large binaries to git.
See .gitignore for excluded files.

Author
Jacob Joseph
G24AI2049