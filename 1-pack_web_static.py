#!/usr/bin/python3
"""Deploying web application with Fabric"""
from fabric.api import local, runs_once
from datetime import datetime
import os


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
