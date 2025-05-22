# 🚀 FastAPI Hello World

A simple but complete "Hello World" project using **FastAPI** for the backend, **PostgreSQL** for database management, **Flet** for the animated user interface, **Traefik** for routing and HTTPS, and **Terraform** for infrastructure as code. This project demonstrates a full-stack setup with CI/CD powered by GitHub Actions.

The entire deployment and setup process on the target AWS instance is fully automated using **Ansible**. Once the infrastructure is provisioned, Ansible handles installation and service configuration without any manual steps.

---

## 📸 Screenshot
![App screen](./ui/hello_world/src/assets/app_test.png)

---

## 🧹 Features

* **FastAPI**: Modern, high-performance web framework for building APIs with Python.
* **PostgreSQL**: Powerful relational database for storing messages.
* **Flet**: Python UI framework for creating interactive and animated frontends.
* **Traefik**: Handles routing, HTTPS, and HTTP challenges automatically.
* **Terraform**: Manages AWS infrastructure using Infrastructure as Code.
* **Ansible**: Automates server configuration and service deployment on AWS.
* **GitHub Actions**: Implements CI/CD for automated testing and deployment.
* **Docker Compose**: Manages local and production services with ease.

---

## 📁 Project Structure

```
fastapi_hello_world/
├── .github/workflows/       # GitHub Actions CI/CD workflows
├── ansible/                 # Ansible roles and configurations
├── app/                     # FastAPI backend and database models
├── ui/                      # Flet user interface
├── terraform/               # Terraform infrastructure files
├── letsencrypt/             # SSL-related files
├── traefik.yml              # Traefik routing and HTTPS config
├── docker-compose.yml       # Docker Compose service definitions
├── requirements.txt         # Python dependencies
├── Dockerfile.dev           # Dockerfile for development
├── Dockerfile.ui            # Dockerfile for UI
└── README.md                # Project documentation
```

---

## ⚙️ Prerequisites

* Python 3.10+
* Docker & Docker Compose
* Terraform
* Ansible
* AWS CLI (for infrastructure deployment)
* SSH key pair for server access

---

## 🛠️ Setup & Deployment

### 1. Clone the Repository

```bash
git clone https://github.com/sepehrmdn77/fastapi_hello_world.git
cd fastapi_hello_world
```

### 2. Export AWS Credentials

Before running Terraform:

```bash
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
```

### 3. Deploy Infrastructure with Terraform

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

After deployment, note the server's IP address.

### 4. Configure Ansible

Update the server IP in `ansible/hosts`, then run:

```bash
cd ansible
ansible-playbook -i hosts playbook.yml
```

This step will automatically install all dependencies and run services on the AWS instance.

---

## 🌐 Service Access

* **Flet UI**: `https://your-domain.com/`
* **FastAPI API**: `https://api.your-domain.com/`
* **Swagger Docs**: `https://api.your-domain.com/docs`
* **Traeik Panel**: `https://your-domain.com/8080`


---

## 🔒 HTTPS & Security

* **Traefik** automatically handles HTTPS with Let's Encrypt.
* Uses **HTTP challenge** to verify domain ownership.
* Ensure ports 80 and 443 are open on the server.

---

## 🚀 CI/CD with GitHub Actions

* On every push, GitHub Actions automatically runs tests.
* If successful, the project is deployed to the server.
* Workflows are defined under `.github/workflows/`

---

## 📅 Notes

* **Default user**: The default user for the instance is `ubuntu`. If you're using a different user or OS, modify `ansible/roles/`, `ansible.cfg`, and `docker-compose.yml` accordingly.
* **Domain**: Update the domain in the `traefik` section of `docker-compose.yml` to route correctly.
* **SSH Key**: After applying Terraform, update the IP in `ansible/hosts` to match your provisioned instance.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve or extend this project:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please make sure your changes follow the existing code style and are well-tested.

---

## 📬 Contact
For issues or feature requests, please open an issue in the repository or reach out at [sepehrmaadani98@gmail.com].

---

## 📄 License

This project is licensed under the MIT License.
