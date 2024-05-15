# CloudDb Benchmarking
Benchmarking AWS, Google cloud, and azure database options | Computer Systems Performance 2024 | Project 2

## Running HammerDB on VM's via CLI
### Setting up vm with HammmerDB via docker.
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:**
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
```
docker --version
```

```sudo docker pull tpcorg/hammerdb```
```docker tag  tpcorg/hammerdb hammerdb```
```sudo docker run -it --name hammerdb hammerdb bash
```



### Consoles

1. Azure: https://portal.azure.com/#home
2. Google Cloud: https://console.cloud.google.com/welcome/

### Offers
1. Azure: (100$ credits for students)  https://azure.microsoft.com/en-us/free/students
2. Google cloud: (new customers 300$ credits) https://cloud.google.com/free?hl=en
