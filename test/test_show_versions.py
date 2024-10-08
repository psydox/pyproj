from pyproj._show_versions import (
    _get_deps_info,
    _get_proj_info,
    _get_sys_info,
    show_versions,
)


def test_get_proj_info():
    pyproj_info = _get_proj_info()
    assert "pyproj" in pyproj_info
    assert "PROJ (runtime)" in pyproj_info
    assert "PROJ (compiled)" in pyproj_info
    assert "data dir" in pyproj_info
    assert "user_data_dir" in pyproj_info
    assert "PROJ DATA (recommended version)" in pyproj_info
    assert "PROJ Database" in pyproj_info
    assert "EPSG Database" in pyproj_info
    assert "ESRI Database" in pyproj_info
    assert "IGNF Database" in pyproj_info


def test_get_sys_info():
    sys_info = _get_sys_info()

    assert "python" in sys_info
    assert "executable" in sys_info
    assert "machine" in sys_info


def test_get_deps_info():
    deps_info = _get_deps_info()

    assert "pip" in deps_info
    assert "setuptools" in deps_info
    assert "certifi" in deps_info
    assert "Cython" in deps_info


def test_show_versions_with_proj(capsys):
    show_versions()
    out, err = capsys.readouterr()
    assert "System" in out
    assert "python" in out
    assert "PROJ (runtime)" in out
    assert "PROJ (compiled)" in out
    assert "data dir" in out
    assert "Python deps" in out
