# CloudDb Benchmarking
Benchmarking AWS, Google cloud, and azure database options | Computer Systems Performance 2024 | Project 2

## Running HammerDB on VM's via CLI
### Setting up vm with HammmerDB via docker.
Create and ssh into linux VM

Set up Docker's apt repository.
```bash
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

Install docker
```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
```bash
docker --version
```
Pull and tag hammerdb image
```bash
sudo docker pull tpcorg/hammerdb
```

```bash
sudo docker tag  tpcorg/hammerdb hammerdb
```

Run the image
```bash
sudo docker run -it --name hammerdb hammerdb bash
```

### Setup HammerDB
```bash
cd scripts/python/mssqls/tprocc
```
We need to set connection settings in all py files!
```python
diset('connection','mssqls_tcp','false')
diset('connection','mssqls_port','1433')
diset('connection','mssqls_azure','true')
diset('connection','mssqls_encrypt_connection','true')
diset('connection','mssqls_trust_server_cert','true')
diset('connection','mssqls_authentication','sql')
diset('connection','mssqls_server','<IP ADRESS OF DATABASE>')
diset('connection','mssqls_linux_server','<IP ADRESS OF DATABASE>')
diset('connection','mssqls_linux_authent','sql')
diset('connection','mssqls_linux_odbc','{ODBC Driver 18 for SQL Server}')
diset('connection','mssqls_uid','azureuser')
diset('connection','mssqls_pass','<DB PASSWORD>')
```
**Set mssqls_tprocc_buildschema.py**
Set virtual users and warehouses:
```python
vu = <AMOUNT OF VUs>
warehouse = int(vu) * 5
diset('tpcc','mssqls_count_ware',warehouse)
diset('tpcc','mssqls_num_vu',vu)
```


**Set mssqls_tprocc_deleteschema.py**

**Set mssqls_tprocc_result.py**

**Set mssqls_tprocc_run.py**
Set virtual users.
```python
diset('tpcc','mssqls_dbase','tpcc')
diset('tpcc','mssqls_driver','timed')
diset('tpcc','mssqls_total_iterations','10000000')
diset('tpcc','mssqls_rampup','2')
diset('tpcc','mssqls_duration','5')
diset('tpcc','mssqls_allwarehouse','true')
diset('tpcc','mssqls_timeprofile','true')
diset('tpcc','mssqls_checkpoint','false')
...
loadscript()
print("TEST STARTED")
vuset('vu','<AMOUNTVUs>')
vucreate()
tcstart()
tcstatus()
jobid = tclpy.eval('vurun')
vudestroy()
tcstop()
...
```



### Execute HammerDB
Move script to source folder.
```bash
mv mssqls_tprocc_py.sh ../../../../
```
```bash
./mssqls_tprocc_py.sh
```

### Consoles

1. Azure: https://portal.azure.com/#home
2. Google Cloud: https://console.cloud.google.com/welcome/

### Offers
1. Azure: (100$ credits for students)  https://azure.microsoft.com/en-us/free/students
2. Google cloud: (new customers 300$ credits) https://cloud.google.com/free?hl=en
