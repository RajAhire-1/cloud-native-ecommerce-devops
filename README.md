# Cloud-Native E-Commerce DevOps Platform

## 📋 Overview

This project demonstrates an **end-to-end DevOps implementation** of a cloud-native microservices platform using **AWS, Docker, GitHub Actions CI/CD, and Kubernetes (kubeadm)**.

**Primary Objective**: Practical DevOps learning and job readiness with strong focus on:
- CI/CD automation
- Container image lifecycle management
- Kubernetes deployment and operations
- Debugging real-world production issues

> **Note**: This is **not** an application development project. The emphasis is on infrastructure, automation, and operational workflows.

## 🏗️ Architecture

```
Developer
   |
   | Git Push
   v
GitHub Repository
   |
   | GitHub Actions (CI/CD)
   v
Docker Image Build & Tag
   |
   | Push Images
   v
AWS Elastic Container Registry (ECR)
   |
   | Image Pull
   v
Kubernetes Cluster (kubeadm)
   |
   | NodePort Services
   v
External Client / Browser
```

## 🛠️ Technology Stack

### Cloud & Infrastructure
- **AWS EC2** (ap-south-1)
- **Ubuntu Linux**
- IAM Roles for EC2
- **AWS Elastic Container Registry (ECR)**

### Containerization & CI/CD
- **Docker**
- **GitHub Actions** (CI/CD pipelines)

### Kubernetes
- **Kubernetes v1.29** (self-managed using kubeadm)
- containerd runtime
- Calico CNI
- NodePort services

### Application Layer
- Python Flask microservices
- REST-based health check endpoints

## 📦 Microservices

| Service | Technology | Container Port | Endpoint | ECR Repository |
|---------|------------|----------------|----------|----------------|
| Product Service | Python Flask | 5000 | `/health` | `product-service` |
| Order Service | Python Flask | 5001 | `/health` | `order-service` |

**Key Characteristics:**
- Independently containerized
- Independently built and pushed via CI/CD
- Independently deployed on Kubernetes

## 📁 Repository Structure

```
cloud-native-ecommerce-devops/
├── product-service/
│   ├── app.py
│   └── Dockerfile
├── order-service/
│   ├── app.py
│   └── Dockerfile
├── k8s/
│   ├── product-deployment.yaml
│   ├── product-service.yaml
│   ├── order-deployment.yaml
│   └── order-service.yaml
├── .github/
│   └── workflows/
│       └── docker-ecr.yml
├── screenshots/
└── README.md
```

## 🔄 CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline is triggered on **every push to the main branch** and performs:

1. **Checkout** source code
2. **Build Docker images** for each microservice
3. **Authenticate** to AWS ECR
4. **Push Docker images** to private ECR repositories

> This setup avoids Jenkins and demonstrates modern, GitHub-native CI/CD practices.

## ☸️ Kubernetes Deployment

- **Kubernetes cluster** provisioned using `kubeadm`
- **One control-plane node** and **one worker node**
- **Calico CNI** for pod networking
- Services exposed using **NodePort**
- **No EKS**, no managed load balancer

### Image Pull Authentication
Private ECR image access is handled using:
- Kubernetes `imagePullSecrets`
- Docker registry secret for ECR
- ServiceAccount patching for seamless image pulls

> This setup reflects real-world troubleshooting and resolution of `ImagePullBackOff` and `ErrImagePull` issues.

## 🌐 Service Access

Once deployed, services are accessible via NodePort:

- **Product Service**: `http://<worker-public-ip>:30001/health`
- **Order Service**: `http://<worker-public-ip>:30002/health`

**Example response:**
```json
{
  "status": "UP"
}
```

## 🎯 Key DevOps Learnings

- End-to-end CI/CD using GitHub Actions
- Docker image build, tag, and push workflows
- AWS ECR integration with Kubernetes
- Debugging Kubernetes image pull failures
- Authentication handling in self-managed clusters
- NodePort-based service exposure
- Hands-on kubeadm cluster operations

## 💼 Interview Talking Points

- Designed and implemented CI/CD pipelines using GitHub Actions
- Deployed containerized microservices on a self-managed Kubernetes cluster
- Solved real-world ECR authentication and image pull issues
- Worked with Kubernetes networking and service exposure
- Avoided managed services to demonstrate core DevOps fundamentals

## 👤 Author

**Joy**  
Aspiring AWS Cloud & DevOps Engineer

## ⚠️ Disclaimer

This project is created for **learning, interviews, and demonstrations**.  
It intentionally avoids managed services (such as EKS) to showcase **fundamental DevOps and Kubernetes concepts**.

---

## 🚀 Quick Start

### Prerequisites
- AWS Account
- GitHub Account
- Basic knowledge of Docker and Kubernetes
- AWS CLI configured with appropriate credentials

### Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cloud-native-ecommerce-devops.git
   cd cloud-native-ecommerce-devops
   ```

2. **Configure GitHub Secrets**
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION` (ap-south-1)
   - `ECR_REPOSITORY_URL`

3. **Set up Kubernetes Cluster**
   ```bash
   # Follow kubeadm installation guide
   kubeadm init --pod-network-cidr=192.168.0.0/16
   kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
   ```

4. **Deploy Applications**
   ```bash
   kubectl apply -f k8s/
   ```

## 📊 Monitoring & Verification

Check deployment status:
```bash
kubectl get pods
kubectl get services
kubectl get deployments
```

## 🔍 Troubleshooting Common Issues

### Image Pull Errors
```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### Service Access Issues
```bash
# Check if NodePort is exposed
kubectl get svc
# Check worker node IP
curl http://<worker-ip>:30001/health
```

## 🤝 Contributing

This is a learning project. Feel free to fork and adapt for your own DevOps learning journey!

## 📄 License

Educational Purpose - Free to use for learning and interviews.

---

**⭐ Star this repo if you found it helpful for your DevOps journey!**
