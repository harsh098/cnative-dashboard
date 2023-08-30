# cnative-dashboard
A simple Cloud Native Dashboard with Automated Deployments over EKS via Kubernetes API  
`aws/` folder contains scripts for deploying the dashboard to **EKS** and push images to **ECR**  

```.
├── app.py  # Flask Server
├── aws
│   ├── ecr.py #Script to push to ECR
│   └── eks.py #Script to deploy to EKS
├── Dockerfile 
├── requirements.txt
├── templates   
│   └── index.html  #Jinja 2 Template
```
`eks.py` : This script leverages the **K8S API** to create a **Deployment** and a **Service**
