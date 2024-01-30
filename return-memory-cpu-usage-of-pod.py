import os
from kubernetes import client, config
import psutil

def get_pod_resource_usage(namespace, pod_name):
    try:
        # Load Kubernetes configuration from default location or kubeconfig
        config.load_kube_config()

        # Create Kubernetes API client
        api_instance = client.CoreV1Api()

        # Retrieve pod information
        pod_info = api_instance.read_namespaced_pod(name=pod_name, namespace=namespace)

        # Extract container name from the first container in the pod
        container_name = pod_info.spec.containers[0].name

        # Retrieve container resource usage
        container_stats = api_instance.read_namespaced_pod_exec(
            name=pod_name,
            namespace=namespace,
            command=['/bin/sh', '-c', f'top -b -n 1 | grep {container_name}'],
            container=container_name,
            stdout=True,
            stderr=True,
            stdin=False,
            tty=False,
        )

        # Extract CPU and memory usage from the top command output
        top_output = container_stats.output.decode('utf-8').split('\n')
        cpu_usage = top_output[0].split()[9]
        memory_usage = top_output[2].split()[5]

        return {
            'pod_name': pod_name,
            'namespace': namespace,
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
        }

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    # Replace these values with your namespace and pod name
    namespace = "your-namespace"
    pod_name = "your-pod-name"

    result = get_pod_resource_usage(namespace, pod_name)
    print(result)
