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

3. Add execution permissions to ginit script :
- I guess that this step will be unnecessary, check permissions ```ls -l ginit``` look for -rwxr-xr-x, if not like this then, do this step otherwise skip this
```
chmod +x ginit setupenv
```

4. To setup the environment variables run the setupenv file and follow along :
```
./setupenv
```

5. Make the GitHub and Local Repo by initiating the script as :
```
./ginit RepoNameHere
```
- To make this command accessible from anywhere in the system :
```
echo "export PATH:$PATH:/path/to/the/cloned/repo" >> ~/.bash_profile
```

- You will be asked to enter your github username and password to validate the initial commit push request
