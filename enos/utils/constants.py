# -*- coding: utf-8 -
import os

# PATH constants
ENOS_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
SYMLINK_NAME = os.path.join(os.getcwd(), 'current')
TEMPLATE_DIR = os.path.join(ENOS_PATH, 'templates')
ANSIBLE_DIR = os.path.join(ENOS_PATH, 'ansible')

# IP constants
INTERNAL_IP = 0
REGISTRY_IP = 1
INFLUX_IP = 2
GRAFANA_IP = 3
NEUTRON_IP = 4

# NIC constants
NETWORK_IFACE = 0
EXTERNAL_IFACE = 1

# KOLLA SPECIFIC
KOLLA_REPO = 'https://git.openstack.org/openstack/kolla'
KOLLA_REF = 'stable/newton'

# ENOS Setup
VERSION = '1.0.0'
