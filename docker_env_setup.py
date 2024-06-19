# docker_env_setup.py
import os

def create_docker_compose(file_path):
    compose_content = """
    version: '3'
    services:
      kali:
        image: kalilinux/kali-rolling
        container_name: kali
        tty: true
      web:
        image: vulnerable/web:latest
        container_name: vulnerable_web
        ports:
          - "80:80"
    """
    with open(file_path, 'w') as f:
        f.write(compose_content)
    print(f"Docker Compose file created at {file_path}")

def deploy_environment(compose_file):
    os.system(f"docker-compose -f {compose_file} up -d")
    print("Docker environment deployed.")

if __name__ == "__main__":
    compose_path = "docker-compose.yml"
    create_docker_compose(compose_path)
    deploy_environment(compose_path)
