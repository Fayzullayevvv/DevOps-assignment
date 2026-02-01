## Agriculture Platform: Cloud-Native Monitoring & GitOps Deployment

This project demonstrates a robust, automated DevOps pipeline and monitoring solution for a containerized application named **agri-app**. The architecture is built on **Kubernetes** and leverages the **GitOps** methodology for seamless application delivery and infrastructure management.

### Key Components:

* **Infrastructure & Orchestration**: Powered by **Minikube (Kubernetes)** to manage application lifecycle and services.
* **Continuous Integration (CI)**: **GitHub Actions** automates the build and push process of Docker images to **Docker Hub**.
* **Continuous Delivery (CD)**: **ArgoCD** ensures the cluster state matches the desired state defined in the **Helm-based** `agri-chart` repository.
* **Observability Stack**:
* **Prometheus**: Collects and stores real-time performance metrics like CPU and Memory usage.
* **Loki**: Aggregates live application logs for efficient troubleshooting.
* **Grafana**: Provides professional, visualized dashboards for monitoring the overall health and performance of the application.

### Project Structure

```text
├── .github/
│   └── workflows/
│       └── docker-build.yml      # CI pipeline for Docker build and push
├── agri-chart/                   # Primary Helm Chart directory
│   ├── templates/                # Kubernetes manifest templates
│   │   ├── deployment.yaml       # Application deployment configuration
│   │   └── service.yaml          # Kubernetes service configuration
│   └── values.yaml               # Values for Helm chart customization
├── Dockerfile                    # Instructions for building the Docker image
├── app.py                        # Main application source code (Flask/Python)
└── README.md                     # Project documentation

```

---

### File Descriptions:

* **`.github/workflows/docker-build.yml`**: Automates the Continuous Integration (CI) process by building and pushing the application image to Docker Hub whenever changes are pushed to GitHub.
* **`agri-chart/templates/`**: Contains the Kubernetes manifests that ArgoCD monitors to ensure the cluster state is synchronized with the GitHub repository.
* **`app.py`**: The core application logic that generates the live metrics and logs visualized in the Prometheus and Loki dashboards.
* **`Dockerfile`**: Defines the environment and dependencies required to containerize the **agri-app**.

<img width="560" height="475" alt="image" src="https://github.com/user-attachments/assets/c3012296-fd88-44d3-8f1b-5946b79917cc" />

### **ArgoCD Continuous Delivery Status**

This screenshot showcases the **ArgoCD** dashboard, confirming the successful deployment and synchronization of the **agri-app**.

**Key details visible in the status card include:**

* **Application Health**: The application is in a **Healthy** state, meaning all Kubernetes pods and services are running as expected.
* **Synchronization**: The status is **Synced**, indicating that the live cluster state perfectly matches the desired state defined in the GitHub repository.
* **Deployment Path**: The application is deployed using the Helm chart located at the `agri-chart/templates/` directory.
* **Destination**: It is currently running in the `default` namespace within the Kubernetes cluster.
* **Last Sync**: The most recent successful synchronization was completed on **01/30/2026**.

<img width="2274" height="710" alt="image" src="https://github.com/user-attachments/assets/b0e4f7ef-9654-4383-9398-0836a68110bf" />

### **ArgoCD Application Topology and Resource Hierarchy**

This visualization provides a comprehensive view of the **agri-app** resource hierarchy within the Kubernetes cluster, as managed by **ArgoCD**.

**Key Architectural Insights:**

* **Live Infrastructure Health**: The entire application stack is confirmed as **Healthy** and **Synced**, with green icons indicating that every component is running optimally and matches the Git configuration.
* **Resource Mapping**:
* **Service (svc)**: Shows the `agri-app-service`, which manages network traffic for the application.
* **Deployment**: The root deployment object that ensures the desired number of application instances are maintained.
* **ReplicaSet (rs)**: The controller responsible for the lifecycle of specific pod versions (currently running version `rev:1`).
* **Pod**: The individual running instance (`agri-app-6b7df5f68-z92nd`) where the application code is executed.


* **GitOps Validation**: The dashboard confirms a successful sync to the specific Git commit `a140829`, titled **"Update deployment.yaml"**, proving that the latest changes were automatically deployed via the CD pipeline.

<img width="2559" height="1424" alt="image" src="https://github.com/user-attachments/assets/f755aedc-181d-4ee9-b8ff-5281bf8060f8" />

### **Agriculture Platform: Professional Monitoring Dashboard**

This high-level overview demonstrates the complete observability stack for the **agri-app**, integrating real-time metrics and logs into a single, unified view.

#### **1. Full Dashboard Overview**

The comprehensive dashboard provides a "single pane of glass" view into the application's health, combining availability, resource consumption, and live execution logs.

* **Application Availability (Uptime)**: A discrete timeline tracking the operational status of the `agri-app` pod over time.
* **Resource Utilization**: Side-by-side graphs for CPU and Memory, allowing for quick correlation between performance spikes and resource limits.
* **Live Application Logs**: A bottom-panel stream powered by **Loki**, providing immediate context for the metrics shown above.

#### **2. Performance Metrics (CPU & Memory)**

* **CPU Usage (%)**: Tracks the processing power consumed by the application. The cleaned legend (right) identifies specific pods and system components, ensuring the `agri-app` is monitored without technical clutter.
* **Memory Usage (MB)**: Provides a clear visualization of the application's memory footprint (approx. 42 MB). The simplified legend shows the specific pod instance (`agri-app-6b7df5f68-z92nd`), facilitating precise capacity planning.

#### **3. Log Aggregation (Loki)**

* **Live Application Logs**: This panel captures and formats real-time logs directly from the container.
* **Clean Formatting**: Using the `| json | line_format` parser, raw JSON data is converted into human-readable text (e.g., tracking `GET /update` requests with `200 OK` status).
* **Incident Response**: Critical warnings and errors are highlighted, enabling rapid debugging directly from the Grafana interface.

<img width="2559" height="1269" alt="image" src="https://github.com/user-attachments/assets/ac69afe1-7f8c-4ef0-9299-d56bc0410135" />

### **Kubernetes Cluster Health and Resource Monitoring**

This comprehensive dashboard provides a high-level overview of the global health and resource allocation of the Kubernetes cluster hosting the **agri-app**.

**Key Infrastructure Insights:**

* **Cluster Capacity and Usage**: Real-time gauges monitor global Pod, CPU, Memory, and Disk usage across the entire cluster.
* **Deployment Management**:
* **Active Replicas**: The cluster is currently managing **12 active deployment replicas**, all of which are confirmed as up-to-date.
* **Service Availability**: Core monitoring services, such as the `loki-stack-prometheus-server`, are verified as operational with a 1:1 replica-to-value ratio.


* **Node and Pod Status**:
* **Compute Resources**: The infrastructure consists of **1 active node** (Minikube), showing no disk pressure or unavailability.
* **Pod Orchestration**: There are **23 pods currently running** in the cluster. The dashboard confirms **0 pending, failed, or unknown pods**, ensuring a stable environment for application delivery.

<img width="2559" height="1200" alt="image" src="https://github.com/user-attachments/assets/c9c4ea59-ba80-4f12-a5b0-0475c4932711" />

### **Cluster Resource and Network Monitoring**

This dashboard provides detailed metrics on network throughput and aggregate resource consumption across the entire Kubernetes infrastructure.

**Key Monitoring Insights:**

* **Network I/O Pressure**: A real-time timeline tracks network ingress and egress traffic, monitoring for throughput spikes or connectivity issues.
* **Total Cluster Resource Usage**:
* **Memory Usage**: The cluster is currently utilizing **1.95 GiB** (approximately **12.6%**) of its total **15.47 GiB** memory capacity.
* **CPU Utilization**: The aggregate CPU usage is maintained at a very efficient level of **0.87%** (utilizing **0.28 cores** out of **32.00** available).


* **Filesystem Status**: Integrated gauges monitor cluster filesystem usage to prevent storage-related outages, ensuring smooth data persistence for containerized workloads.
* **Centralized Observability**: Global filters allow for seamless switching between different **Prometheus data sources** and specific **Cluster Nodes**, ensuring the monitoring setup is scalable as the infrastructure grows.

<img width="2559" height="1315" alt="image" src="https://github.com/user-attachments/assets/ba8c2931-c436-4230-9d8f-9854bf61688e" />

### **ArgoCD Controller Operational Logs**

This visualization provides a detailed view of the **argocd-application-controller** logs, captured and managed through **Loki**. It serves as a critical diagnostic tool for monitoring the background processes of the GitOps synchronization engine.

**Key Operational Insights:**

* **Continuous Synchronization Monitoring**: The logs track real-time events such as **"Update successful"** and **"Refreshing app status"**, confirming that the controller is actively maintaining the desired state of the `agri-app`.
* **Automated GitOps Reconciliation**: Detailed entries record the comparison between the live cluster state and the Git repository (`https://kubernetes.default.svc`), ensuring that any manual drift is automatically detected and corrected.
* **Resource Health Validation**: The controller logs verify that the application status is consistently marked as **Synced**, with specific timestamps and metadata provided for every reconciliation cycle.
* **Event Timeline**: An integrated bar chart at the top allows for quick identification of log volume spikes, helping administrators correlate background controller activity with application deployment events.


### **Conclusion**

The **Agriculture Platform** successfully demonstrates a complete, production-grade DevOps lifecycle using modern Cloud-Native technologies. By integrating **GitHub Actions** for CI, **ArgoCD** for GitOps-based CD, and a full **Prometheus/Loki/Grafana** stack for observability, the project ensures that the application is not only delivered automatically but also remains healthy and performant in a Kubernetes environment.

The automated synchronization between the GitHub repository and the cluster minimizes manual errors and ensures a "Single Source of Truth" for both application code and infrastructure configuration.

### **Future Improvements**

To further enhance this platform, the following features are planned for future development:

* **Auto-Scaling**: Implementing **Horizontal Pod Autoscaler (HPA)** to automatically adjust the number of `agri-app` instances based on the CPU/Memory metrics captured by Prometheus.
* **Alert Management**: Configuring **Grafana Alerting** or **Prometheus Alertmanager** to send real-time notifications (e.g., via Slack or Telegram) when critical errors are detected in the Loki logs or when resource usage exceeds predefined thresholds.
* **Security Scanning**: Integrating security tools like **Trivy** into the GitHub Actions pipeline to scan Docker images for vulnerabilities before they are pushed to the registry.
* **Ingress Controller**: Transitioning from port-forwarding to a proper **Ingress Controller** (like Nginx) for more secure and scalable external access to the platform services.
