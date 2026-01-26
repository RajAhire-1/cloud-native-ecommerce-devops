Cloud-Native E-Commerce DevOps Platform
Overview

This project demonstrates an end-to-end DevOps implementation of a cloud-native microservices platform using AWS, Docker, GitHub Actions CI/CD, and Kubernetes (kubeadm).

The primary objective of this project is practical DevOps learning and job readiness, with a strong focus on:

CI/CD automation

Container image lifecycle management

Kubernetes deployment and operations

Debugging real-world production issues

This is not an application development project.
The emphasis is on infrastructure, automation, and operational workflows.

Architecture Summary
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

Technology Stack
Cloud & Infrastructure

AWS EC2 (ap-south-1)

Ubuntu Linux

IAM Roles for EC2

AWS Elastic Container Registry (ECR)

Containerization & CI/CD

Docker

GitHub Actions (CI/CD pipelines)

Kubernetes

Kubernetes v1.29 (self-managed using kubeadm)

containerd runtime

Calico CNI

NodePort services

Application Layer

Python Flask microservices

REST-based health check endpoints

Microservices
Product Service

Technology: Python Flask

Container Port: 5000

Endpoint: /health

ECR Repository: product-service

Order Service

Technology: Python Flask

Container Port: 5001

Endpoint: /health

ECR Repository: order-service

Each microservice is:

Independently containerized

Independently built and pushed via CI/CD

Independently deployed on Kubernetes

Repository Structure
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

CI/CD Pipeline (GitHub Actions)

The CI/CD pipeline is triggered on every push to the main branch and performs the following steps:

Checkout source code

Build Docker images for each microservice

Authenticate to AWS ECR

Push Docker images to private ECR repositories

This setup avoids Jenkins and demonstrates modern, GitHub-native CI/CD practices.

Kubernetes Deployment

Kubernetes cluster provisioned using kubeadm

One control-plane node and one worker node

Calico CNI used for pod networking

Services exposed using NodePort

No EKS, no managed load balancer

Image Pull Authentication

Private ECR image access is handled using:

Kubernetes imagePullSecrets

Docker registry secret for ECR

ServiceAccount patching for seamless image pulls

This setup reflects real-world troubleshooting and resolution of ImagePullBackOff and ErrImagePull issues.

Service Access

Once deployed, the services are accessible via NodePort:

http://<worker-public-ip>:30001/health   (Product Service)
http://<worker-public-ip>:30002/health   (Order Service)


Example response:

{
  "status": "UP"
}

Key DevOps Learnings

End-to-end CI/CD using GitHub Actions

Docker image build, tag, and push workflows

AWS ECR integration with Kubernetes

Debugging Kubernetes image pull failures

Authentication handling in self-managed clusters

NodePort-based service exposure

Hands-on kubeadm cluster operations

Interview Talking Points

Designed and implemented CI/CD pipelines using GitHub Actions

Deployed containerized microservices on a self-managed Kubernetes cluster

Solved real-world ECR authentication and image pull issues

Worked with Kubernetes networking and service exposure

Avoided managed services to demonstrate core DevOps fundamentals

Author

Joy
Aspiring AWS Cloud & DevOps Engineer

Disclaimer

This project is created for learning, interviews, and demonstrations.
It intentionally avoids managed services (such as EKS) to showcase fundamental DevOps and Kubernetes concepts.
