# Flink
flink your life!

*Proper fancy docs coming soon :)*

-------------------------------------------

## Requirements
### **node.js 4+ and npm**

**Install for**

**Mac**
```
brew install node
```
**RHEL and its flavors**
```
sudo yum install nodejs
```
**Debian and its flavors**
```
sudo apt-get install nodejs
```
**Others**
https://nodejs.org/en/download/

### **sequelize-cli NPM module** (run with root/admin privileges)
```
[sudo] npm install -g sequelize-cli
```

### **Supported Databases**
- MySQL/MariaDB
- SQLite
- Postgres

## Usage

- Clone this repository
- In the repo directory, run ``` npm install ```
- Run migrations using ``` sequelize --env production|test|[development] db:migrate ```

### For development 
- Run ``` gulp ``` in the root folder.
- Will start as ``` node --harmony index --db development ``` with file watchers on 8000

### Others
- run the app using ``` node --harmony index --db production|test|[development] ``` on port 8000

## Running Tests
- Run ``` gulp test ```
