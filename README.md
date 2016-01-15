#Flink
flink your life!

*Proper fancy docs coming soon :)*

-------------------------------------------

## Requirements
###**node.js 4+ and npm**

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

###**Supported Databases**
- MySQL/MariaDB
- SQLite

##Usage

- Clone this repository
- In the repo directory, run ``` npm install ```
- Run migrations using ``` sequelize --env production|test|[development] db:migrate ```
- run the app using ``` node --harmony index --env production|test|[development] ``` on port 8000
