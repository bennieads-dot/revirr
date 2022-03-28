# revirr

## Dev Environment

1. Install pre-reqs if applicable

- virtualbox
  ```bash
  https://www.virtualbox.org/wiki/Downloads
  ```

- homebrew
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

- vagrant
  ```bash
  brew install vagrant
  ```

2. Add the ubuntu box locally
  ```bash
  vagrant box add bento/ubuntu-20.04
  ```

3. Bring up the box 
  ```bash
  vagrant up
  ```

4. ssh into the box
```bash
vagrant ssh
```

5. Change to dev directory: this is the revirr directory (the repo) on your local machine.
  ```bash
  cd /revirr
  ```

6. Activate revirr venv
  ```bash
  source /revirr/revirr_env/bin/activate
  ```

