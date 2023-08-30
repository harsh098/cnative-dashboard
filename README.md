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

# Demo
![Demo](https://github.com/harsh098/cnative-dashboard/assets/23445112/0f7d2db9-1f06-4fea-925e-0f5e30e52b54)  
![Port Forward from cluster to localhost](https://github.com/harsh098/cnative-dashboard/assets/23445112/fe4f0ef0-ba43-4fc5-ae6c-ae4fcf085052)


# AWS EKS Cluster
![EKS Cluster](https://github.com/harsh098/cnative-dashboard/assets/23445112/bc1c4bd9-ef9f-47ab-8ca6-9df78610148f)

# AWS EC2 NodeGroups
![Node Groups](https://github.com/harsh098/cnative-dashboard/assets/23445112/603c5934-67c3-4acf-808a-88c438bc1d5b)  

# AWS VPC Security Groups
![Amazon VPC SG](https://github.com/harsh098/cnative-dashboard/assets/23445112/1e1bd055-6824-47fd-9656-6d08796fcbd2)


# AWS ECR Image
![Screenshot from 2023-08-30 16-56-52](https://github.com/harsh098/cnative-dashboard/assets/23445112/7212b338-9848-4959-8504-1e3fb36341ef)  

# AWS IAM User for Managing ECR and EKS
![IAM user perms](https://github.com/harsh098/cnative-dashboard/assets/23445112/1a8b8a04-f6d3-4f51-a69a-5d440e037709)  

# AWS IAM Roles for Cluster and NodeGroups
![IAM Roles for Cluster and NodeGroup Management](https://github.com/harsh098/cnative-dashboard/assets/23445112/9cf906e5-a70b-43ef-bce1-8e6d75957baf)

# IAM Permissions for IAM Role to Manage EKS Cluster
![Role to Manage EKS Cluster](https://github.com/harsh098/cnative-dashboard/assets/23445112/3a9c7f1f-df94-4a36-8625-ac556a766eb5)

# IAM Permissions for IAM Role to Manage EC2 NodeGroups
![Role to Manage EC2 Nodegroups](https://github.com/harsh098/cnative-dashboard/assets/23445112/cba37ab7-dcae-4fcc-bd77-62ffb6ec96c5)



