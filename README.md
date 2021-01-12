# ginit
## Automating GitHub initial setup

---
**Note**
This is for Linux, I have no idea about other OSes, but you will need Bourne Again SHell (BASH) to run the script
---

### Installation
1. Clone the repo & change directory :

```
git clone https://github.com/H4RSH-K/ginit.git
cd ginit
```
2. Install the requirements :
```
pip install -r requirements.txt
```


3. Add the github email, username, password and path to your github projects folder in the .env file (so your credentials remain hidden) :
```
touch .env
```
### Format :
```
USERNAME="your-github-username"
EMAIL="your-github-email-address"
PASSWORD="your-github-password"
FILEPATH="/path/to/your/projects/folder/"
```
4. Add execution permissions to ginit script :

```
chmod +x ginit
```
5. Make the GitHub and Local Repo by initiating the script as :
```
./ginit RepoNameHere
```


- You will be asked to enter your github username and password to validate the initial commit push request
# Test : Generated using the ginit script
