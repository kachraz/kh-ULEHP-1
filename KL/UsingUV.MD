
1. [Commands for UV](#commands-for-uv)
   1. [Installing just as script](#installing-just-as-script)
   2. [Add a package](#add-a-package)
   3. [Running A Script](#running-a-script)


# Commands for UV 

## Installing just as script 

```sh 
uv init --script <name.py>
```

## Add a package 

```sh 
uv add --script example.py 'requests<3' 'rich'
```

## Running A Script 

```sh 
uv run --script example.py
```