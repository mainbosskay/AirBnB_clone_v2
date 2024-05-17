#!/usr/bin/python3
"""Deploying web application with Fabric"""
from fabric.api import local, runs_once, env, put, run
from datetime import datetime
import os

env.hosts = ["54.175.72.70", "54.227.195.244"]


@runs_once
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


def do_deploy(archive_path):
    """Distributing archives to web servers
    Args: archive_path: path to static files"""
    if not os.path.exists(archive_path):
        return False
    filenm = os.path.basename(archive_path)
    filednm = filenm.replace(".tgz", "")
    filedpath = f"/data/web_static/releases/{filednm}/"
    output = False
    try:
        put(archive_path, f"/tmp/{filenm}")
        run(f"mkdir -p {filedpath}")
        run(f"tar -xzf /tmp/{filenm} -C {filedpath}")
        run(f"rm -rf /tmp/{filenm}")
        run(f"mv {filedpath}web_static/* {filedpath}")
        run(f"rm -rf {filedpath}web_static")
        run("test -L /data/web_static/current && rm /data/web_static/current")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {filedpath} /data/web_static/current")
        print('New version deployed!')
        output = True
    except Exception as e:
        output = False
    return output


def deploy():
    """Creating and distributing archives to web servers"""
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False


def do_clean(number=0):
    """Deleting out-of-date archives
    Args: number (int): number of archives to keep"""
    archfield = 'versions/'
    archlist = os.listdir(archives_folder)
    archlst.sort(reverse=True)
    startindx = int(number)
    if not startindx:
        startindx += 1
    if startindx < len(archlist):
        archdel = archlist[startindx:]
    else:
        archdel = []
    for arch in archdel:
        archpath = os.path.join(archfield, arch)
        os.unlink(archpath)
    cmdpts = [
            "rm -rf $(",
            "find /data/web_static/releases/ -maxdepth 1 -type d -iregex",
            " '/data/web_static/releases/web_static_.*'",
            f" | sort -r | tr '\\n' ' ' | cut -d ' ' -f{start_index + 1}-)"
    ]
    run(''.join(cmpts))
