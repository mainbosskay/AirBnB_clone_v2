#!/usr/bin/python3
"""Deploying web application with Fabric"""
from fabric.api import *
from datetime import datetime
from os.path import exists, basename

env.hosts = ["54.175.72.70", "54.227.195.244"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """Creating archive of static files"""
    if not os.path.exists("versions"):
        os.mkdir("versions")
    currentdt = datetime.utcnow()
    reslt = f"versions/web_static_{currentdt.strftime('%Y%m%d%H%M%S')}.tgz"
    try:
        print(f"Packing web_static to {reslt}")
        local(f"tar -cvzf {reslt} web_static")
        file_size = os.path.getsize(reslt)
        print(f"web_static packed: {reslt} -> {file_size} Bytes")
    except Exception as e:
        print(f"Error: {e}")
        reslt = None
    return reslt


@task(default=True)
def do_deploy(archive_path):
    """Distributing archives to web servers
    Args: archive_path: path to static files"""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filenm = basename(archive_path)
        filenmxt = filenm.split(".")[0]
        filedpath = f"/data/web_static/releases/{filenmxt}/"
        sudo(f"mkdir -p {filedpath}")
        sudo(f"tar -xzf /tmp/{filenm} -C {filedpath}")
        sudo(f"rsync -a {filedpath}web_static/* {filedpath}")
        sudo(f"rm -rf {filedpath}web_static")
        sudo(f"rm -rf /tmp/{filenm}")
        sudo(f"rm -rf /data/web_static/current")
        sudo(f"ln -sf {filedpath} /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
