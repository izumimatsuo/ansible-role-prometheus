import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_prometheus_user(host):
    assert host.user("prometheus").exists


def test_node_exporter_is_installed(host):
    assert host.exists('node_exporter')


def test_node_exporter_running_and_enabled(host):
    service = host.service('node_exporter')
    assert service.is_running
    assert service.is_enabled


def test_node_exporter_is_listen(host):
    assert host.socket('tcp://0.0.0.0:9100').is_listening


def test_prometheus_is_installed(host):
    assert host.exists('prometheus')


def test_prometheus_running_and_enabled(host):
    service = host.service('prometheus')
    assert service.is_running
    assert service.is_enabled


def test_prometheus_is_listen(host):
    assert host.socket('tcp://0.0.0.0:9090').is_listening


def test_alertmanager_is_installed(host):
    assert host.exists('alertmanager')


def test_alertmanager_running_and_enabled(host):
    service = host.service('alertmanager')
    assert service.is_running
    assert service.is_enabled


def test_alertmanager_is_listen(host):
    assert host.socket('tcp://0.0.0.0:9093').is_listening


def test_blackbox_exporter_is_installed(host):
    assert host.exists('blackbox_exporter')


def test_blackbox_exporter_running_and_enabled(host):
    service = host.service('blackbox_exporter')
    assert service.is_running
    assert service.is_enabled


def test_blackbox_exporter_is_listen(host):
    assert host.socket('tcp://0.0.0.0:9115').is_listening
