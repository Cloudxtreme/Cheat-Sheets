# Start using git with the current directory
git init

# Add external(remote) repo named origin
git remote add origin git@github.com:__user__/__repo__.git
#   By convention, "origin" is the original remote repository, 
#     it is the 'primary' centralized repository as well. 
#     In other words is the local name given to the remote centralized server.
 
* You can check the URL of origin with this: 
```git remote show origin```
 
* Scheduling the addition of all files to the next commit
```git add __file__```

* Committing files (-a: all, -v: view diff)
```git commit -m "comments"```

* Push changes to remote repo "origin" from local "master" 
```git push -u origin master```

* Pull (checkout) to local "master" from remote repo "origin"
```git pull origin master```

* Define the git user (email or name)
```git config --global user.email "don@gmail.com"```

* Check user (email or name)
```git config --global user.email```

### Cloning ###

- Cloning a git repo, remote or local
```
git clone git@github.com:__user__/__repo__.git
git clone hello hello-clone
```

- Do things... changes new files... 
```git add ejemplo.txt```

- Adding to the local repo
```git commit -m "now in local repo"```

- Push changes into the remote repo
```git push git@github.com:__user__/__repo__.git```

- Get changes from other users
- You do not need to specify the local branch if you are already sitting in it.
```git pull```

- Clone specific branch
```
git clone <url> --branch <branch> --single-branch [<folder>]
git clone user@git-server:project_name.git -b branch_name /some/folder
git clone user@git-server:project_name.git -b branch_name --single-branch /some/folder
```


### Ignoring files ###

- Create a file in the root directory called ```.gitignore```
- then add ignore restrictions like: ```*.log db/schema.rb```

- If you want a ```log/``` directory, but want to ignore all the files in it: ```log/*```
- Then add an empty .gitignore in the empty directory: ```touch log/.gitignore```

- Lines beginning with ```!``` are exceptions ```!.gitignore```

### Basic Commands ###

- Checking the status of your repository ```git status```
- Seeing what files have been committed ```git ls-files```
- Scheduling deletion of a file ```git rm __file__```
- Viewing a log of your commits ( -v: pagination ) ```git log``` or ```git log --stat```
- Visualizing git changes ```git --all```
- Creating a new tag and pushing it to the remote branch
```git tag "v1.3"```, then ```git push --tags```
```
- SVN revert
```
git log # search the SHA1_HASH where you want to go
git reset --hard SHA1_HASH # SHA1_HASH must me something like: 85102eac830990afa60136419bd09ffeea7eb646

git clone -b <branch> <remote_repo>
git clone -b my-branch git@github.com:user/myproject.git

With Git 1.7.10 and later, add --single-branch to prevent fetching of all branches. Example, with OpenCV 2.4 branch:
git clone -b 2.4 --single-branch https://github.com/Itseez/opencv.git opencv-2.4


# merge differente remotes
git remote add openshift git@github.com:__user__/__repo__.git
git fetch openshift
git merge openshift/master
git commit

