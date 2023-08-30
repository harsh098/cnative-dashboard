#!/usr/bin/python3

from kubernetes import config, client

config.load_kube_config("kubeconfig")
v1 = client.ApiClient()

# Create a deployment object

deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="cnative-dashboard"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "cnative-dashboard"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "cnative-dashboard"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="cnative-dashboard",
                        image="016173386347.dkr.ecr.us-east-1.amazonaws.com/cnative-dashboard:latest",
                        ports=[client.V1ContainerPort(container_port=3000)]
                    )
                ]
            )
        )
    ))



#Create a service object
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="cnative-dashboard"),
    spec=client.V1ServiceSpec(
        selector={"app": "cnative-dashboard"},
        ports=[client.V1ServicePort(port=80, target_port=3000)],
        type="NodePort"
    )
)

# Create an instance of the API class apiVersion:apps/v1
api_instance = client.AppsV1Api(v1)

# Apply the deployment
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

# Create an instance of the API class apiVersion:v1
api_instance = client.CoreV1Api(v1)

api_instance.create_namespaced_service(
    namespace="default",
    body=service
)