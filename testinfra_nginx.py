#####################################################################################
### TEST FOR NGINX, NGINX CONFIG, CERTBOT AND WHY ARE YOU LOOCKING AT??????????? ####
#####################################################################################
import pytest
import os


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed


def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_nginx_site_been(host):
    localhost = host.addr("localhost")

    assert host.file("/etc/nginx/sites-available/sitename.conf").exists
    assert host.file("/etc/nginx/sites-enabled/sitename.conf").is_symlink
    assert localhost.port(443).is_reachable
    assert localhost.port(80).is_reachable
    assert host.socket("tcp://0.0.0.0:80").is_listening
    assert host.socket("tcp://0.0.0.0:443").is_listening

def test_nginx_is_working_optimized(host):
    workers = host.process.filter(ppid=host.process.get(user="root", comm="nginx"))
    assert len(workers) < 10
    assert sum([w.pmem for w in workers]) < 2

def test_certbot_is_successfully(host):
    cmd = host.run("ls /etc/letsencrypt/")

    assert cmd.rc == 0


def test_certbot_daemons(host):
    certbot_timer = host.service("certbot-semi-automatic.timer")

    assert certbot_timer.is_running
    assert certbot_timer.is_enabled
