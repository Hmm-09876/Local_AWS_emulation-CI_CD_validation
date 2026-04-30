import threading, time, urllib.request, os, json, sys, socket

sys.path.insert(0, os.path.abspath("src/demo_app"))

from urllib.error import HTTPError, URLError
from app import run

def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]

def start_local_server(port=8080):
    ready_event = threading.Event()
    thr = threading.Thread(target=run, kwargs={"port": port, "ready_event": ready_event}, daemon=True)
    thr.start()
    if not ready_event.wait(timeout=5):
        time.sleep(1)
    return thr


def test_health_check():
    port = get_free_port()
    thr = start_local_server(port)
    try:
        deadline = time.time() + 5
        resp = None
        while time.time() < deadline:
            try:
                resp = urllib.request.urlopen(f"http://localhost:{port}/health", timeout=1)
                break
            except Exception:
                time.sleep(0.1)
        assert resp is not None, "Failed to connect to the server"
        body = resp.read().decode()
        data = json.loads(body)
        assert resp.status == 200
        assert data.get("status") == "ok"
    finally:
        pass

def test_root_endpoint_returns_ok():
    port = get_free_port()
    start_local_server(port)
    deadline = time.time() + 5
    resp = None
    while time.time() < deadline:
        try:
            resp = urllib.request.urlopen(f"http://localhost:{port}/", timeout=1)
            break
        except Exception:
            time.sleep(0.1)
    assert resp is not None, "Failed to connect to the server"
    body = resp.read().decode()
    data = json.loads(body)
    assert resp.status == 200
    assert data == {"status": "ok"}

def test_unknown_path_returns_404():
    port = get_free_port()
    start_local_server(port)
    deadline = time.time() + 5
    while time.time() < deadline:
        try:
            urllib.request.urlopen(f"http://localhost:{port}/not-found", timeout=1)
        except HTTPError as e:
            assert e.code == 404
            return 
        except URLError:
            time.sleep(0.1)
    assert False, "Server did not respond in time"

