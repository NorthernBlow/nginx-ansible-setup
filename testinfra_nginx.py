#####################################################################################
### TEST FOR NGINX, NGINX CONFIG, CERTBOT AND WHY ARE YOU LOOCKING AT??????????? ####
#####################################################################################
import pytest


def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.2")


def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled
